def decompress(outdir: str, type: str, password: str, mode: str) -> bool:
    suff = outdir.split('.')[-1]
    if mode == "decompress":
        if (password == "True" and suff != "enc"):
            res = input("File suffix is not .enc\nDo you want to continue?(yes/no)")
            return res.lower() == "yes"
        elif password == "False" and (
                (type == "zip" and suff != "zip")
                or (type == "tar" and suff != "gz")
                or (type == "rle" and suff != "rle")
                or (type == "huffman" and suff != "huff")
        ):
            res = input("File suffix is wrong.\nDo you want to continue?(yes/no)")
            return res.lower() == "yes"
