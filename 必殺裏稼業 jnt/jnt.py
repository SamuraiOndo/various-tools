from ctypes import pointer
from fileinput import filename
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
w.set_endian(False)
reader.set_endian(False) # little endian
isFile = os.path.isfile(sys.argv[1])
unique_id = 0
if(Mypath.is_file()):
    reader.seek(0x04)
    filecount = reader.read_uint32()
    reader.seek(reader.read_uint32())
    for i in range(filecount):
        size = reader.read_uint32()
        reader.read_uint32()
        pointer = reader.read_uint32()
        namePointer = reader.read_uint32()
        stay = reader.pos()
        reader.seek(namePointer)
        filename = reader.read_str()
        reader.seek(pointer)
        print(f'Extracting {filename}...')
        output_path = directory / Path(Myfilename + ".unpack")
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / (filename)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        fe = open(output_file, "wb")
        fe.write(reader.read_bytes(size))
        fe.close()
        reader.seek(stay)
