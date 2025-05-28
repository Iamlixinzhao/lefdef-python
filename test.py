from lefdef import C_LefReader
from lefdef import C_DefReader
#change the file address below
lef_reader = C_LefReader()
_lef = lef_reader.read("external/def/TEST/complete.5.8.def")
_lef.print()

def_reader = C_DefReader()
_def = def_reader.read("external/lef/TEST/complete.5.8.lef")
_def.print()
