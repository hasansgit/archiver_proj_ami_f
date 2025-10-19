import tarfile
from pathlib import Path


class TarArchiver:
    def archive(self, indir: Path, outdir: Path) -> None:
        try:
            with tarfile.open(indir, "w:bz2") as archive:
                archive.add(indir, arcname=indir.name)
            print(f"Архив создан: {outdir}")

        except tarfile.TarError as e:
            print(f"Ошибка при работе с tar-архивом {e}")

    def unarchive(self, indir: Path, outdir: Path) -> None:
        try:
            with tarfile.open(indir) as archive:
                archive.extractall(path=outdir)
            print(f"Архив распакован в {outdir}")

        except tarfile.ReadError:
            print("Ошибка: повреждённый или неподдерживаемый архив")
        except PermissionError:
            print("Ошибка: нет прав для записи в указанную папку")
        except tarfile.TarError as e:
            print(f"Ошибка при чтении tar-архива {e}")
