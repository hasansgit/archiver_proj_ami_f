from archivers.archiver import ArchiverInterface
from archivers.huffman import HuffmanArchiver
from archivers.rle import RleArchiver
from archivers.tar import TarArchiver
from archivers.zip import ZipArchiver


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


def outdir_suff(outdir: str, type_: str, mode: str) -> str:
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
    if type_ == "tar":
        return outdir[:-7]
    return outdir[: outdir.rfind(".")]
