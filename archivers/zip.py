import zipfile

from pathlib import Path


class ZipArchiver:

    def __init__(self, password: str = None) -> None:
        self.password = password

    def archive(self, indir: Path, outdir: Path) -> None:
        with zipfile.ZipFile(outdir, "w", zipfile.ZIP_DEFLATED) as zf:
            if self.password is not None:
                zf.setpassword(bytes(self.password, "utf-8"))
            zf.write(indir)

    def unarchive(self, indir: Path, outdir: Path = None) -> None:
        try:
            with zipfile.ZipFile(indir, "r") as zf:
                if self.password is not None:
                    zf.setpassword(bytes(self.password, "utf-8"))
                zf.extractall(outdir)
        except zipfile.BadZipFile:
            print("Ошибка: файл не является ZIP-архивом или поврежден")
        except RuntimeError as e:
            if "password" in str(e).lower():
                print("Ошибка: неверный пароль")
            else:
                print(f"Ошибка: {e}")
