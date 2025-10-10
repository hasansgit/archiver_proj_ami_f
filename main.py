import argparse
from pathlib import Path

import huffman
import rle


def main():
    parser = argparse.ArgumentParser("Simple archiver")
    parser.add_argument("mode", choices=["compress", "decompress", "zip", "unzip", "tar", "untar"], help="Mode to use")
    parser.add_argument("-a", "--algorithm", choices=["rle", "huffman"], default="rle",
                        help="Algorithm to use (default: rle)")
    # parser.add_argument("-c", "--chunksize", default=1024 * 1024 * 64, type=int,
    #                     help="Chunk size in MBs (default: 64MB)")
    # parser.add_argument("-cb", "--chunksizebytes", default=1024 * 1024 * 64, type=int,
    #                     help="Chunk size in bytes (default: 64MB)")
    parser.add_argument("-sp", "--setpassword", choices=[True, False], default=False,
                        help="Set password to use (default: False)")
    parser.add_argument("indir", help="file or directory")
    parser.add_argument("outdir", help="output directory")

    args = parser.parse_args()
    indir: Path = Path(args.indir)
    outdir: Path = Path(args.outdir)
    # chunksize: int = args.chunksize
    algorithm: str = args.algorithm

    if args.mode == "compress" or args.mode == "decompress":
        archiver = rle.RLE() if algorithm == "rle" else huffman.Huffman()
        if args.mode == "compress":
            archiver.archive(indir, outdir)
        else:
            archiver.unarchive(indir, outdir)
    else:
        pass


if __name__ == '__main__':
    main()
