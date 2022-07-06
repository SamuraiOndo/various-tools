from binary_reader import BinaryReader
import sys
from pathlib import Path
import os

Mypath = Path(sys.argv[1])
directory = str(Mypath.resolve().parent)
print(directory)
Myfilename = Mypath.name
path = Mypath.open("rb")
reader = BinaryReader(path.read())
w = BinaryReader()
w.set_endian(False)
reader.set_endian(False) # big endian
isFile = os.path.isfile(sys.argv[1])
reader.seek(0x100)
size1 = reader.read_uint32()
output_file = directory + "\\" + (Myfilename + ".bmp")
fe = open(output_file, "wb")
fe.write(reader.read_bytes(size1))
fe.close()