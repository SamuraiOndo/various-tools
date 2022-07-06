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

reader.set_endian(False) # big endian
isFile = os.path.isfile(sys.argv[1])
unique_id = 0
if(reader.read_uint16()!=0):
    reader.seek(0)
    tlfdcount = reader.read_uint32()
    reader.seek(0x10)
    for i in range(tlfdcount):
        pointer = reader.read_uint32()
        size1 = reader.read_uint32()
        indices = reader.read_uint32()
        identifier = reader.read_str(4)
        stay = reader.pos()
        reader.seek(pointer)
        count = reader.read_uint32()
        indentifier = reader.read_str(4)
        print("Current id", identifier)
        reader.read_uint32(2)
        for j in range(count):
            pointer2 = reader.read_uint32()
            size2 = reader.read_uint32()
            stay2 = reader.pos()
            output_path = directory / Path(Myfilename + ".unpack") / (identifier + str(i))
            if (size2 != 0):
                output_path.mkdir(parents=True, exist_ok=True)
                output_file = output_path / (str(j) + ".dat")
                fe = open(output_file, "wb")
                offset = pointer + pointer2
                reader.seek(offset)
                print("writing to", output_file, offset, size2)
                fe.write(reader.read_bytes(size2))
                fe.close()
                unique_id += 1
            reader.seek(stay2)
            reader.read_uint32(2)
        reader.seek(stay)
#        j = str(i)
#        fe = open(directory + "\\" + "TLFD" + "\\" + j + ".dat","wb")S
#        fe.write(reader.read_bytes(size1))
#        fe.close
        reader.seek(stay)
    
