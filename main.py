import os
from pathlib import Path

import validating
from archivers import factory
from archivers.archiver import ArchiverInterface
from arg_parse.arg_parse import arg_parser
from encryption import encryption


def main():
    parser = arg_parser()
    args = parser.parse_args()
    indir = args.indir
    decrypted = False

    if not Path(indir).exists():
        print("Input directory does not exist")
        return

    if validating.encrypt.is_encrypted(indir):
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

    if mode == "decompress" and validating.suff_validing.decompress(indir, type_):
        return

    outdir = (args.outdir if args.outdir else factory.outdir_suff(indir, type_, mode))
    out_path = Path(outdir)

    if mode:
        archiver: ArchiverInterface = factory.create_archiver(type_)
        if mode == "compress":
            archiver.archive(in_path, out_path)
        else:
            archiver.unarchive(in_path, out_path)
        in_path = out_path

    password = (True if args.password == "True" else False)

    if not decrypted and password:
        password = input("Password: ")
        out_path = Path(outdir + ".enc")
        encryption.encrypt(in_path, out_path, password)
        if mode == "compress":
            os.remove(in_path)


if __name__ == "__main__":
    main()
