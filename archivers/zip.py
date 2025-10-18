import zipfile

from pathlib import Path


class ZipArchiver:

    def archive(self, indir: Path, outdir: Path) -> None:
        with zipfile.ZipFile(outdir, "w", zipfile.ZIP_DEFLATED) as zf:
            if indir.is_file():
                zf.write(indir)
            else:
                for file in indir.rglob("*"):
                    if file.is_file():
                        zf.write(file, arcname=file.relative_to(indir))

    def unarchive(self, indir: Path, outdir: Path) -> None:
        try:
            with zipfile.ZipFile(indir, "r") as zf:
                if outdir.exists() and not outdir.is_dir():
                    outdir = outdir.with_name(outdir.name + "_unpacked")
                outdir.mkdir(parents=True, exist_ok=True)
                zf.extractall(outdir)
        except zipfile.BadZipFile:
            print("Ошибка: файл не является ZIP-архивом или поврежден")
        except RuntimeError as e:
            if "password" in str(e).lower():
                print("Ошибка: неверный пароль")
            else:
                print(f"Ошибка: {e}")
