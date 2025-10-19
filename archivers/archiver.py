from pathlib import Path
from typing import Protocol


class ArchiverInterface(Protocol):
    def archive(self, indir: Path, outdir: Path) -> None: ...

    def unarchive(self, indir: Path, outdir: Path) -> None: ...
