import argparse
import pathlib

import huffman
import rle
from archiver import ArchiverInterface


def main():
    parser = argparse.ArgumentParser("Simple archiver")
    parser.add_argument("mode", choices=["compress", "decompress", "zip", "unzip", "tar", "untar"], help="Mode to use")
    parser.add_argument("-a", "--algorithm", choices=["rle", "huffman"], default="rle",
                        help="Algorithm to use (default: rle)")
    parser.add_argument("-c", "--chunksize", default=1024 * 1024 * 64, type=int,
                        help="Chunk size in MBs (default: 64MB)")
    parser.add_argument("-cb", "--chunksizebytes", default=1024 * 1024 * 64, type=int,
                        help="Chunk size in bytes (default: 64MB)")
    parser.add_argument("-sp", "--setpassword", choices=[True, False], default=False,
                        help="Set password to use (default: False)")
    parser.add_argument("indir", help="file or directory")
    parser.add_argument("outdir", help="output directory")

    args = parser.parse_args()
    indir: str = args.indir
    outdir: str = args.outdir
    chunksize = args.chunksize
    algorithm: str = args.algorithm

    if args.mode == "compress":
        archiver: ArchiverInterface = rle.RLE() if algorithm == "rle" else huffman.Huffman()
        compress(indir, outdir, archiver)
    elif args.mode == "decompress":
        archiver: ArchiverInterface = rle.RLE() if algorithm == "rle" else huffman.Huffman()
        decompress(indir, outdir, archiver)
    else:
        pass


def compress(indir: str, outdir: str, archiver: ArchiverInterface) -> None:
    indir = pathlib.Path(indir)
    outdir = pathlib.Path(outdir)
    archiver.archive(indir, outdir)


def decompress(indir: str, outdir: str, archiver: ArchiverInterface) -> None:
    indir = pathlib.Path(indir)
    outdir = pathlib.Path(outdir)
    archiver.unarchive(indir, outdir)


if __name__ == '__main__':
    main()
