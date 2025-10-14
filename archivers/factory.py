from archivers.archiver import ArchiverInterface
from archivers.zip import ZipArchiver
from archivers.tar import TarArchiver
from archivers.rle import RleArchiver
from archivers.huffman import HuffmanArchiver


def create_archiver(type_: str, password: str | None = None) -> ArchiverInterface:
    match type_:
        case "zip":
            return ZipArchiver(password)
        case "tar":
            return TarArchiver()
        case "rle":
            return RleArchiver()
        case "huffman":
            return HuffmanArchiver()
        case _:
            raise ValueError(f"Unknown archiver type: {type_}")
