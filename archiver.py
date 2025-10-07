from abc import ABC, abstractmethod

from huffman import Huffman
from rle import RLE


class Archiver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def archive(self, indir: str, outdir: str, chunksize: int) -> None:
        pass

    @abstractmethod
    def unarchive(self, indir: str, outdir: str, chunksize: int) -> None:
        pass

    @classmethod
    def create(cls, algorithm: str):
        if algorithm == "rle":
            return RLE()
        return Huffman()
