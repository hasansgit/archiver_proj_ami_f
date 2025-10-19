import itertools
from pathlib import Path


def encrypt(indir: Path, outdir: Path, password: str) -> None:
    password = [ord(char) for char in password]
    with open(indir, "rb") as input:
        for ind in itertools.count():
            byte = input.read(1)
            if not byte:
                break
            byte = int.from_bytes(byte)
            byte = byte ^ password[ind % len(password)]
            with open(outdir, "ab") as output:
                output.write(byte.to_bytes())
