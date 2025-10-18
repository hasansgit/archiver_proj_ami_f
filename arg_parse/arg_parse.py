import argparse


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser("Simple archiver")
    parser.add_argument("-m", "--mode", choices=["compress", "decompress"], help="Mode to use")
    parser.add_argument("-t", "--type", choices=["zip", "tar", "rle", "huffman"], default="zip",
                        help="Archive type to use (default: zip)")
    # parser.add_argument("-c", "--chunksize", default=1024 * 1024 * 64, type=int,
    #                     help="Chunk size in MBs (default: 64MB)")
    # parser.add_argument("-cb", "--chunksizebytes", default=1024 * 1024 * 64, type=int,
    #                     help="Chunk size in bytes (default: 64MB)")
    parser.add_argument("-sp", "--setpassword", choices=['True', 'False'], default='False',
                        help="Set password to use (default: False)")
    parser.add_argument("indir", help="file or directory")
    parser.add_argument("-o", "--outdir", help="output directory")
    return parser
