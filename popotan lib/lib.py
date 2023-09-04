from ctypes import pointer
from fileinput import filename
from binary_reader import BinaryReader
import sys
from pathlib import Path
import os
def extract(reader,directory,Myfilename):
    reader.seek(8)
    count = reader.read_uint32()
    reader.seek(0x10)
    for i in range(count):
        filename = reader.read_str(36)
        size = reader.read_uint32()
        origpointer = reader.read_uint32()
        pointer = (origpointer)
        stay = reader.pos()
        reader.seek(pointer)
        print(filename)
        output_path = directory / Path(Myfilename + ".unpack")
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / (filename)
        fe = open(output_file, "wb")
        fe.write(reader.read_bytes(size))
        fe.close()
        reader.seek(stay+4)
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
    extract(reader,directory,Myfilename)
#        j = str(i)
#        fe = open(directory + "\\" + "TLFD" + "\\" + j + ".dat","wb")S
#        fe.write(reader.read_bytes(size1))
#        fe.close
    
