from archivers.archiver import ArchiverInterface
from archivers.zip import ZipArchiver
from archivers.tar import TarArchiver
from archivers.rle import RleArchiver
from archivers.huffman import HuffmanArchiver


def create_archiver(type_: str) -> ArchiverInterface:
    match type_:
        case "zip":
            return ZipArchiver()
        case "tar":
            return TarArchiver()
        case "rle":
            return RleArchiver()
        case "huffman":
            return HuffmanArchiver()
        case _:
            raise ValueError(f"Unknown archiver type: {type_}")


def outdir_dot(outdir: str, type_: str, mode: str) -> str:
    if mode == "compress":
        match type_:
            case "zip":
                return f"{outdir}.zip"
            case "tar":
                return f"{outdir}.tar.gz"
            case "rle":
                return f"{outdir}.rle"
            case "huffman":
                return f"{outdir}.huff"
