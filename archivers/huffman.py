import heapq
import pickle
from collections import Counter
from pathlib import Path


class HuffmanArchiver:
    def archive(self, indir: Path, outdir: Path) -> None:
        fin = open(indir, "rb")
        frequency = []
        while True:
            c = fin.read(1)
            frequency.append(c)
            if not c:
                break
        heap = [[freq, [char, ""]] for char, freq in Counter(frequency).items()]
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
        fin.close()
        fin1 = open(indir, "rb")
        fout = open(outdir, "wb")
        pickle.dump(codes, fout)
        while True:
            b = fin1.read(1)
            if not b:
                break
            fout.write(bytes(codes[b], "utf-8"))
        fin1.close()
        fout.close()

    def unarchive(self, indir: Path, outdir: Path) -> None:
        fin = open(indir, "rb")
        codes = pickle.load(fin)
        ncodes = {}
        for key, value in codes.items():
            ncodes[value] = key
        fout = open(outdir, "wb")
        while True:
            b1 = fin.read(1).decode("utf-8")
            if not b1:
                break
            while b1 not in ncodes:
                b1 = b1 + fin.read(1).decode("utf-8")
            fout.write(ncodes[b1])
        fin.close()
        fout.close()
