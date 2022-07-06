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
    filecount = reader.read_uint32()
    for i in range(filecount):
        filename = reader.read_str(16)
        size = reader.read_uint32()
        origpointer = reader.read_uint32()
        pointer = (origpointer*2048)
        stay = reader.pos()
        reader.seek(pointer)
        output_path = directory / Path(Myfilename + ".unpack")
        output_path.mkdir(parents=True, exist_ok=True)
        print(filename)
        output_file = output_path / (filename)
        fe = open(output_file, "wb")
        fe.write(reader.read_bytes(size))
        fe.close()
        reader.seek(stay)
#        j = str(i)
#        fe = open(directory + "\\" + "TLFD" + "\\" + j + ".dat","wb")S
#        fe.write(reader.read_bytes(size1))
#        fe.close
    
