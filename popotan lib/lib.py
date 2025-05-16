from binary_reader import BinaryReader
import sys
from pathlib import Path
def extract(reader, directory, Myfilename):
    if reader.read_str(3).lower() != "lib":
        return
    reader.seek(8)
    count = reader.read_uint32()
    reader.seek(0x10)
    for _ in range(count):
        filename = reader.read_str(36).strip('\x00')
        size = reader.read_uint32()
        origpointer = reader.read_uint32()
        pointer = origpointer
        stay = reader.pos()
        reader.seek(pointer)
        print(filename)
        output_path = directory / Path(Myfilename + ".unpack")
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / filename
        file_bytes = reader.read_bytes(size)
        with open(output_file, "wb") as fe:
            fe.write(file_bytes)
        sub_reader = BinaryReader(file_bytes)
        sub_reader.set_endian(False)
        extract(sub_reader, output_path, Path(filename).stem)
        reader.seek(stay + 4)

if __name__ == "__main__":
    Mypath = Path(sys.argv[1])
    directory = Mypath.resolve().parent
    Myfilename = Mypath.name
    with Mypath.open("rb") as path:
        reader = BinaryReader(path.read())
    reader.set_endian(False) # little endian
    if Mypath.is_file():
        extract(reader, directory, Myfilename)
