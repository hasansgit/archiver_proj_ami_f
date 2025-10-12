from pathlib import Path


class HuffmanArchiver:
    def archive(self, indir: Path, outdir: Path) -> None: ...

    def unarchive(self, indir: Path, outdir: Path) -> None: ...
