from typing import Callable

class RLE:
    def archive(self, indir: str, outdir: str, chunksize: int) -> None:
        self.read_and_write(indir, outdir, chunksize, self.compress)

    def unarchive(self, indir: str, outdir: str, chunksize: int):
        self.read_and_write(indir, outdir, chunksize, self.decompress)

    def read_and_write(self, indir: str, outdir: str, chunksize: int, func: Callable[[bytes], bytes]) -> None:
        with open(indir, "rb") as input:
            while True:
                chunk = input.read(chunksize)
                if not chunk:
                    break
                out = func(chunk)
                with open(outdir, "ab") as output:
                    output.write(out)

    def compress(self, chunk: bytes) -> bytes:
        pass

    def decompress(self, chunk: bytes) -> bytes:
        pass
