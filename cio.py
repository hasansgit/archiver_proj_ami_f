from typing import Callable

from bitarray import bitarray


class ChunkIO:
    def __init__(self, input_path: str, output_path: str, chunk_size: int = 64 * 1024 * 1024) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.chunk_size = chunk_size

    def process(self, process_func: Callable[[bitarray], bitarray]) -> None:
        """Reads chunks from input path and write processed chunks to output path."""
        with open(self.input_path, "rb") as fin, open(self.output_path, "wb") as fout:
            while chunk := fin.read(self.chunk_size):
                # Read chunk and write it to bitarray
                bits = bitarray()
                bits.frombytes(chunk)

                # Processing
                processed_bits = process_func(bits)

                # Writing chunk to output file
                fout.write(processed_bits.tobytes())
