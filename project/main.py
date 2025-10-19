import os
from pathlib import Path

from project.archivers import factory
from project.archivers.archiver import ArchiverInterface
from project.arg_parse.arg_parse import arg_parser
from project.encryption import encryption
from project.validating.encrypt import is_encrypted
from project.validating.suff_validing import decompress as suff_val_dec


def main():
    parser = arg_parser()
    args = parser.parse_args()
    indir = args.indir
    decrypted = False

    if not Path(indir).exists():
        print("Input directory does not exist")
        return

    if is_encrypted(indir):
        in_path = Path(indir)
        indir = indir[:-4]
        out_path = Path(indir)
        password = input("Password: ")
        encryption.encrypt(in_path, out_path, password)
        os.remove(in_path)
        decrypted = True

    in_path = Path(indir)

    type_ = args.type
    mode = args.mode

    if mode == "decompress" and suff_val_dec(indir, type_):
        return

    outdir = args.outdir \
        if args.outdir \
        else factory.outdir_suff(indir, type_, mode)
    out_path = Path(outdir)
    if out_path.exists():
        out_path = Path("(1)" + outdir)

    if mode:
        archiver: ArchiverInterface = factory.create_archiver(type_)
        if mode == "compress":
            archiver.archive(in_path, out_path)
        else:
            archiver.unarchive(in_path, out_path)
        in_path = out_path

    password = True if args.setpassword == "True" else False

    if not decrypted and password:
        password = input("Password: ")
        out_path = Path(outdir + ".enc")
        encryption.encrypt(in_path, out_path, password)
        if mode == "compress":
            os.remove(in_path)


if __name__ == "__main__":
    main()
