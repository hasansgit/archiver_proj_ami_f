from typing import Protocol


class ArchiverInterface(Protocol):
    def archive(self, indir: str, outdir: str, chunksize: int) -> None: ...

    def unarchive(self, indir: str, outdir: str, chunksize: int) -> None: ...
