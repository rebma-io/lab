import urllib.parse as url
from datetime import datetime
from pathlib import Path
from decimal import Decimal
import os
import humanfriendly


# Taken from https://docs.python.org/3/library/decimal.html#recipes
def moneyfmt(
    value: Decimal,
    places: int = 2,
    curr: str = "",
    sep=",",
    dp: str = ".",
    pos: str = "",
    neg: str = "-",
    trailneg: str = "",
):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
            only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places  # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else "0")
    if places:
        build(dp)
    if not digits:
        build("0")
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return "".join(reversed(result))


def define_env(env):
    """This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """
    site_url = env.conf.site_url or "https://lab.rebma.io/"

    @env.macro
    def embed_schematic(schematic_filename: str, height: int = 480) -> str:
        """Generate HTML to embed circuit.js diagram in the document.

        Args:
            schematic (str): filename of schematic

        Returns:
            str: HTML
        """
        BASE_URL_FOR_CIRCUITJS = """https://www.falstad.com/circuit/circuitjs.html"""

        IFRAME_TEMPLATE = (
            r"""<iframe width="100%" height="480" src="{url}">OH NOES!</iframe>"""
        )

        # Account for this not being defined in production because we're
        # not running a server, but instead doing static site generation.
        circuit_url = f"{site_url}circuits/{schematic_filename}"

        # These options are derived from circuitjs documentation.
        # https://github.com/pfalstad/circuitjs1#embedding
        EMBED_OPTIONS = {
            "hideMenu": "true",
        }

        query_string = url.urlencode(
            dict(startCircuitLink=circuit_url) | EMBED_OPTIONS,
            doseq=True,
            safe=":/",
            quote_via=url.quote,
        )

        final_url = BASE_URL_FOR_CIRCUITJS + "?" + query_string

        return IFRAME_TEMPLATE.format(url=final_url)

    @env.macro
    def link_for_download(
        filename: str,
        license: str,
        icon: str = ":material-download-circle-outline:",
    ) -> str:
        """Take the provided information and render a consistent view of
        a file download. The goal is to provide a display of the file
        name, license, size, and last touched.

        This only works for files in the $ROOT/docs/files directory.
        """
        # fmt: off
        ANNOTATION_TEMPLATE = r"""Size: {size}; Updated: {ts}; License: {license}"""
        # fmt: on

        # Set up a bunch of paths the ugliest way possible
        path = f"files/{filename}"
        file_path = f"docs/{path}"
        file_url = f"{site_url}{path}"

        # First, let's make sure the file exists
        try:
            stat = os.stat(file_path)
        except FileNotFoundError:
            return "FILE_NOT_FOUND"

        annotation = ANNOTATION_TEMPLATE.format(
            size=humanfriendly.format_size(stat.st_size),
            ts=datetime.fromtimestamp(stat.st_mtime).isoformat(
                sep=" ", timespec="minutes"
            ),
            license=license,
        )
        markdown = f'[{filename} {icon}]({file_url} "{annotation}")'
        return markdown

    @env.macro
    def usd(
        dollars: str,
        as_of: str = None,
        places: int = 2,
        icon: str = ":fontawesome-solid-money-bill-transfer:",
    ) -> str:
        """Take an input in USD and convert it to a proper notation,
        with link to exchange rate calculations on xr.com.

        By default, we just link to Euros since we had to choose
        something.
        """
        # Build exchange URL
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={dollars}&From=USD&To=EUR"

        # Convert to a Decimal
        usd = Decimal(dollars)

        as_of_str = f""":material-update:{{ title="as of {as_of}" }}""" if as_of else ""
        return f"""{moneyfmt(value=usd, places=places, curr='$')}
                {as_of_str} [{icon}]({url} "Convert to other currency")"""
