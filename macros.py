import urllib.parse as url

BASE_URL_FOR_CIRCUITJS = """http://www.falstad.com/circuit/circuitjs.html"""


def define_env(env):
    """This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    @env.macro
    def embed_schematic(schematic_filename: str, height: int = 480) -> str:
        """Generate HTML to embed circuit.js diagram in the document.

        Args:
            schematic (str): filename of schematic

        Returns:
            str: HTML
        """
        IFRAME_TEMPLATE = (
            r"""<iframe width="100%" height="480" src="{url}">OH NOES!</iframe>"""
        )
        full_filename = f"{schematic_filename}.circuit"
        circuit_url = f"{env.conf.site_url}circuits/{full_filename}"

        # These options are derived from circuitjs documentation.
        # https://github.com/pfalstad/circuitjs1#embedding
        EMBED_OPTIONS = {
            "hideMenu": "true",
        }

        query_string = url.urlencode(
            dict(startCircuitLink=circuit_url) | EMBED_OPTIONS, 
            doseq=True, safe=":/", quote_via=url.quote
        )

        final_url = BASE_URL_FOR_CIRCUITJS + "?" + query_string

        return IFRAME_TEMPLATE.format(url=final_url)
