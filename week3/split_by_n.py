def split_by_n(fname, n=3):
    """
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    """
    assert isinstance(fname, str) and isinstance(n, int)
    with open(fname, "r") as file:
        content = file.read()
        target_size = len(content) // n
        print(target_size)
        file.seek(0)
        chunks = []
        buffer = []
        cur_size = 0

        while True:
            line = file.readline()
            if not line:
                chunks.append(buffer)
                break
            # line_size = len(line.encode("utf-8"))
            line_size = len(line)
            # print(line_size)

            if len(chunks) < n - 1 and cur_size + line_size > target_size:
                chunks.append(buffer)

                buffer = []
                cur_size = 0

            buffer.append(line)
            cur_size += line_size
        # print(len(chunks))

        for i, chunk in enumerate(chunks):
            with open(f"{fname.split('.')[0]}.txt_{i:03}.txt", "wt") as output_file:
                output_file.write("".join(chunk))
                # print(f"Wrote chunk {i}")


# split_by_n("week3/pg5200.txt", 8)
