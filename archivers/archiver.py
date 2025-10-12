from typing import Protocol
from pathlib import Path


class ArchiverInterface(Protocol):
    def archive(self, indir: Path, outdir: Path) -> None:
        ...

    def unarchive(self, indir: Path, outdir: Path) -> None:
        ...
