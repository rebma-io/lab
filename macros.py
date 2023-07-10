import urllib.parse as url
from lzstring import LZString
import os


# Example from https://github.com/pfalstad/circuitjs1/blob/master/tests/jfet1.txt
EXAMPLE_SCHEMATIC = """$ 1 0.000005 7.619785657297057 56 5 50
v 432 368 432 224 0 1 40 3 0 0 0.5
r 432 224 592 224 0 10
w 592 224 672 224 0
w 672 224 672 272 0
w 672 304 672 368 0
r 672 368 544 368 0 100
g 544 368 544 400 0
w 432 368 544 368 0
r 544 288 544 368 0 1
j 592 288 672 288 0 -3.15 0.00412
w 544 288 592 288 0
w 672 368 704 368 0
w 672 224 704 224 0
w 544 288 544 256 0
j 800 256 832 256 0 -4 0.00125
w 800 256 768 256 0
w 832 272 832 304 0
w 832 240 832 208 0
L 752 256 720 256 0 1 false 5 0
L 832 208 832 176 0 0 false 5 0
L 832 304 832 336 0 0 false 5 0
r 752 256 768 256 0 1000
o 5 64 0 12291 0.9681278252715998 0.009681278252715997 0 2 5 3
"""

BASE_URL_FOR_CIRCUITJS = """http://www.falstad.com/circuit/circuitjs.html"""

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
    def embed_schematic(schematic_filename: str = None, height: int = 480) -> str:
        """Generate HTML to embed circuit.js diagram in the document.

        Args:
            schematic (str): filename of schematic

        Returns:
            str: HTML
        """
        IFRAME_TEMPLATE = (
            r"""<iframe width="100%" height="480" src="{url}">OH NOES!</iframe>"""
        )

        if schematic_filename:
            full_filename = os.path.join(
                env.project_dir,
                "circuits",
                f"{schematic_filename}.circuit")
            with open(full_filename, "r") as f:
                schematic = f.read()
        else:
            schematic = EXAMPLE_SCHEMATIC

        # These options are derived from circuitjs documentation.
        # https://github.com/pfalstad/circuitjs1#embedding
        EMBED_OPTIONS = {}

        # This will already be base64 URL-safe encoded
        compressed_schematic = compress_to_url(schematic)

        query_string = url.urlencode(EMBED_OPTIONS | dict(ctz=compressed_schematic))

        final_url = BASE_URL_FOR_CIRCUITJS + "?" + query_string
        print(final_url)
        return IFRAME_TEMPLATE.format(url=final_url)