from pathlib import Path


class RLE:
    def archive(self, indir: Path, outdir: Path) -> None:
        chunksize: int = 256
        with open(indir, "rb") as input:
            while True:
                chunk = input.read(chunksize)
                if not chunk:
                    break
                out = self.compress(chunk)
                with open(outdir, "ab") as output:
                    output.write(out)

    def unarchive(self, indir: Path, outdir: Path):
        with open(indir, "rb") as input:
            while True:
                byte = input.read(1)
                if not byte:
                    break
                num: int = int.from_bytes(byte) + 1
                with open(outdir, "ab") as output:
                    output.write(input.read(1) * num)

    def compress(self, chunk: bytes) -> bytes:
        data = bytearray(chunk)
        result: data = bytearray()
        sequenceLength: int = 0
        for i in range(1, len(data)):
            if data[i] != data[i - 1]:
                result.append(sequenceLength)
                result.append(data[i - 1])
                sequenceLength = -1
            sequenceLength += 1
        result.append(sequenceLength)
        result.append(data[-1])
        return result
