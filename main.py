import argparse
from pathlib import Path

from archivers.archiver import ArchiverInterface
from archivers.factory import create_archiver


def main():
    parser = argparse.ArgumentParser("Simple archiver")
    parser.add_argument("mode", choices=["compress", "decompress", "zip", "unzip", "tar", "untar"], help="Mode to use")
    parser.add_argument("-t", "--type", choices=["zip", "tar", "rle", "huffman"], default="zip",
                        help="Archive type to use (default: zip)")
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
    outdir: Path = Path(args.outdir if args.outdir else args.indir)
    mode: str = args.mode
    password = args.setpassword
    # chunksize: int = args.chunksize
    type: str = args.type

    try:
        f = open(indir)
        f.close()
    except FileNotFoundError:
        print(f"{indir} no such file or directory")
        return

    archiver: ArchiverInterface = create_archiver(type, password)
    if mode == "compress":
        archiver.archive(indir, outdir)
    else:
        archiver.unarchive(indir, outdir)


if __name__ == '__main__':
    main()
