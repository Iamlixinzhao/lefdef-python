from lefdef import C_LefReader
from lefdef import C_DefReader

# Example usage with the sample files shipped in the ``test`` directory
lef_reader = C_LefReader()
_lef = lef_reader.read("test/NanGate_15nm_UTDA.tech.lef")
_lef.print()

def_reader = C_DefReader()
_def = def_reader.read("test/simple.def")
_def.print()
