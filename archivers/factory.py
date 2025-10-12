from archiver import ArchiverInterface
from zip import ZipArchiver
from tar import TarArchiver
from rle import RleArchiver
from huffman import HuffmanArchiver


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
