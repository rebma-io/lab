import urllib.parse as url
from datetime import datetime
from pathlib import Path

import humanfriendly


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

        # Set up a bunch of paths
        path = Path("files") / filename
        file_path = Path("docs") / path
        file_url = f"{site_url}{path}"

        # First, let's make sure the file exists
        try:
            stat = file_path.stat()
        except FileNotFoundError:
            return "FILE_NOT_FOUND"

        annotation = ANNOTATION_TEMPLATE.format(
            size=humanfriendly.format_size(stat.st_size),
            ts=datetime.fromtimestamp(stat.st_mtime).isoformat(
                sep=" ", timespec="minutes"
            ),
            license=license,
        )
        markdown = f'[{filename} {icon}]({path.absolute} "{annotation}")'
        return markdown
