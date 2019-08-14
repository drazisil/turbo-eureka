import argparse
import os
from .lib_object import LibObject

parser = argparse.ArgumentParser(description='Peel a file.')
parser.add_argument('file_path', help='the file path to act on')


def get_file_sig(file_path, num_chars):
    try:
        file_stat = os.stat(file_path)
    except FileNotFoundError as e:
        raise e

    fo = open(file_path, 'rb')
    bytes = fo.read(num_chars)
    fo.close()
    return bytes


def is_ar_archive(file_sig):
    n = 2
    [file_sig[i:i + n] for i in range(0, len(file_sig), n)]
    # The file signature of an ar archive - https://en.wikipedia.org/wiki/Ar_(Unix)
    magic_sig = set([0x21, 0x3C, 0x61, 0x72, 0x63, 0x68, 0x3E, 0x0a])
    return magic_sig == set(file_sig)


def say_hello():
    return 'Like an onion.'


def main():
    print(say_hello())
    args = parser.parse_args()
    try:
        file_sig = get_file_sig(args.file_path, 8)
    except FileNotFoundError as e:
        print('File {} not found, please check it exists.'.format(
            args.file_path))
        quit(-1)
    if is_ar_archive(file_sig):
        lib = LibObject()
