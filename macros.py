import urllib.parse as url
from lzstring import LZString
import os


BASE_URL_FOR_CIRCUITJS = """https://www.falstad.com/circuit/circuitjs.html"""


def define_env(env):
    """This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    def compress_to_url(s: str) -> str:
        """Convert an input string to URL-encoded compressed string."""
        output = LZString()

        return output.compressToEncodedURIComponent(s)

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

        full_filename = os.path.join(env.project_dir, "circuits", schematic_filename)
        with open(full_filename, "r") as f:
            schematic = f.read()
        print(schematic)
        # These options are derived from circuitjs documentation.
        # https://github.com/pfalstad/circuitjs1#embedding
        EMBED_OPTIONS = {
            "hideMenu": "true",
        }

        # This will already be base64 URL-safe encoded
        compressed_schematic = compress_to_url(schematic)
        merged_options = dict(ctz=compressed_schematic) | EMBED_OPTIONS
        query_string = url.urlencode(merged_options, doseq=True)

        final_url = BASE_URL_FOR_CIRCUITJS + "?" + query_string
        return IFRAME_TEMPLATE.format(url=final_url)
