def get_column_with_highest_sum(path):
    with open(path, "r") as file:
        
        lines = file.readlines()
        meta = lines[0].split()
        rows = int(meta[0])+1
        cols = int(meta[1])
        
        csums = [0]*cols
        for line in lines[1::]:
            values = line.split()
            for c in range(cols):
                csums[c] += int(values[c])
        
        mincsum = max(csums)
        mi = None
        for i in range(cols):
            s = csums[i]
            if s < mincsum:
                mincsum = s
                mi = i

    return mi