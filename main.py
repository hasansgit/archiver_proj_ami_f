from pathlib import Path

from archivers.archiver import ArchiverInterface
from archivers.factory import create_archiver, outdir_dot
from encryption import encryption
from arg_parse.arg_parse import arg_parser
import validating


def main():
    parser = arg_parser()
    args = parser.parse_args()
    indir: Path = Path(args.indir)
    mode: str = args.mode
    password = args.setpassword
    # chunksize: int = args.chunksize
    type: str = args.type
    outdir = (outdir_dot(args.outdir if args.outdir else args.indir, type))
    if not validating.suff_validing.decompress(outdir, type, password):
        return
    if password == "True" and suff == "enc":
        outdir = outdir[:-4]

    try:
        f = open(indir)
        f.close()
    except FileNotFoundError:
        print(f"{indir} no such file or directory")
        return
    if mode:
        archiver: ArchiverInterface = create_archiver(type)
        if mode == "compress":
            archiver.archive(indir, outdir)
        else:
            archiver.unarchive(indir, outdir)
    if password == 'True':
        password = input("Password: ")
        encryption.encrypt(indir, outdir, password)


if __name__ == '__main__':
    main()
