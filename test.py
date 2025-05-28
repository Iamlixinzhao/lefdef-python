from lefdef import C_LefReader
from lefdef import C_DefReader

import sys
from contextlib import redirect_stdout


class Tee:
    """Helper class to duplicate output to stdout and a file."""

    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for f in self.files:
            f.write(data)

    def flush(self):
        for f in self.files:
            f.flush()


# Example usage with the sample files shipped in the ``test`` directory
lef_reader = C_LefReader()
_lef = lef_reader.read("test/NanGate_15nm_UTDA.tech.lef")

def_reader = C_DefReader()
_def = def_reader.read("test/simple.def")

# Export the printed output of the LEF and DEF objects to ``output.txt``
with open("output.txt", "w") as f:
    with redirect_stdout(Tee(sys.stdout, f)):
        _lef.print()
        _def.print()
