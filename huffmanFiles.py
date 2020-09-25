import os
import classBased as cb
Huffboth = cb.Huffboth()

file = "sample-file.txt"


def _to_Bytes(data):
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i+8], 2))
    return bytes(b)


with open(file, 'rb') as r:
    content = r.read()
    encoded_text = Huffboth.Encode(str(content))

    decoded_text = Huffboth.Decode(encoded_text)
    if(str(content) == decoded_text):
        print("File Compression and Decompression Sucessful!")
    else:
        print("Failed!")

    fileOP = open("compressed_file.bin", "wb")
    fileOP.write(_to_Bytes(encoded_text))

    _o = os.path.getsize('sample-file.txt')
    _c = os.path.getsize('compressed_file.bin')
    print(f'Original file: {_o} bytes')
    print(f'Compressed file: {_c} bytes')
    print('Compressed file to about {}% of original'.format(
        round((((_o-_c)/_o)*100), 0)))
    fileOP.close()

#####################################################################33

def encodeHuffFile(fileID):
    ip_file = f'decode/{fileID}.txt'
    op_file = f'encodedCompressed/{fileID}.bin'
    with open(ip_file, 'rb') as r:
        content = r.read()
        encoded_text = Huffboth.Encode(str(content))

        decoded_text = Huffboth.Decode(encoded_text)
        if(str(content) == decoded_text):
            print("File Compression and Decompression Sucessful!")
        else:
            print("Failed!")

        fileOP = open(op_file, "wb")
        fileOP.write(_to_Bytes(encoded_text))

        _o = os.path.getsize(ip_file)
        _c = os.path.getsize(op_file)
        print(f'Original file: {_o} bytes')
        print(f'Compressed file: {_c} bytes')
        print('Compressed file to about {}% of original'.format(
            round((((_o-_c)/_o)*100), 0)))
        fileOP.close()


def decodeHuffFile(fileID):
    op_file = f'decode/{fileID}.txt'
    ip_file = f'encodedCompressed/{fileID}.bin'
    with open(ip_file, 'rb') as r:
        content = r.read()
        encoded_text = Huffboth.Decode(str(content))

        decoded_text = Huffboth.Decode(encoded_text)
        if(str(content) == decoded_text):
            print("File Compression and Decompression Sucessful!")
        else:
            print("Failed!")
        
        fileOP = open(op_file, "wb")
        fileOP.write(_to_Bytes(decoded_text))
        fileOP.close()

        _o = os.path.getsize(ip_file)
        _c = os.path.getsize(op_file)
        print(f'Original file: {_o} bytes')
        print(f'Compressed file: {_c} bytes')
        print('Compressed file to about {}% of original'.format(
            round((((_o-_c)/_o)*100), 0)))
        fileOP.close()
#############################################################