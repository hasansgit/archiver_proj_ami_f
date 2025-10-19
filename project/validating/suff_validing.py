def decompress(outdir: str, type: str) -> bool:
    suff = outdir.split(".")[-1]
    if (
        (type == "zip" and suff != "zip")
        or (type == "tar" and suff != "gz")
        or (type == "rle" and suff != "rle")
        or (type == "huffman" and suff != "huff")
    ):
        print(suff, type)
        res = input("File suffix is wrong.\nDo you want to continue?(yes/no)")
        return res.lower() != "yes"
    return False
