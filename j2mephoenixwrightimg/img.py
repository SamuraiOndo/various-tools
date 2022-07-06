from binary_reader import BinaryReader
import sys
from pathlib import Path
import os

Mypath = Path(sys.argv[1])
directory = str(Mypath.resolve().parent)
Myfilename = Mypath.name
path = Mypath.open("rb")
reader = BinaryReader(path.read())
w = BinaryReader()
w.set_endian(True)
reader.set_endian(True) # big endian
isFile = os.path.isfile(sys.argv[1])
unique_id = 0
for i in range(80):
    pointer1 = reader.read_uint32()
    stay = reader.pos()
    pointer2 = reader.read_uint32()
    output_path = directory / Path(Myfilename + ".unpack")
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / (str(i) + ".png")
    fe = open(output_file, "wb")
    reader.seek(pointer1)
    fe.write(reader.read_bytes(pointer2 - pointer1))
    fe.close()
    reader.seek(stay)
pointer3 = reader.read_uint32()
output_path = directory / Path(Myfilename + ".unpack")
output_path.mkdir(parents=True, exist_ok=True)
output_file = output_path / ("80" + ".png")
fe = open(output_file, "wb")
reader.seek(pointer3)
fe.write(reader.read_bytes(12624))
fe.close()