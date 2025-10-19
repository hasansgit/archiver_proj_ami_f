import heapq
import pickle
from collections import Counter
from pathlib import Path


class HuffmanArchiver:
    def archive(self, indir: Path, outdir: Path) -> None:
        with open(indir, "rb") as input:
            frequency = []
            while True:
                c = input.read(1)
                frequency.append(c)
                if not c:
                    break
            heap = [
                [freq, [char, ""]]
                for char, freq in Counter(frequency).items()
            ]
            heapq.heapify(heap)
            while len(heap) > 1:
                left = heapq.heappop(heap)
                right = heapq.heappop(heap)

                for pair in left[1:]:
                    pair[1] = "0" + pair[1]

                for pair in right[1:]:
                    pair[1] = "1" + pair[1]

                new_node = [left[0] + right[0]] + left[1:] + right[1:]
                heapq.heappush(heap, new_node)

            codes = {char: code for char, code in heap[0][1:]}
        with open(indir, "rb") as input:
            with open(outdir, "wb") as output:
                pickle.dump(codes, output)
                while True:
                    b = input.read(1)
                    if not b:
                        break
                    output.write(bytes(codes[b], "utf-8"))

    def unarchive(self, indir: Path, outdir: Path) -> None:
        with open(indir, "rb") as input:
            codes = pickle.load(input)
            ncodes = {}
            for key, value in codes.items():
                ncodes[value] = key
            with open(outdir, "wb") as output:
                while True:
                    b1 = input.read(1).decode("utf-8")
                    if not b1:
                        break
                    while b1 not in ncodes:
                        b1 = b1 + input.read(1).decode("utf-8")
                    output.write(ncodes[b1])
