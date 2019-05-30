def computeLPSArray(string, M, lps):
    length = 0        # length of the previous longest prefix suffix
    i = 1

    lps[0] = 0    # lps[0] is always 0

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        print(f"i = {i} j = {length}")
        print(f"LPS = {lps}")
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # This is tricky. Consider the example AAACAAAA
                # and i = 7.
                length = lps[length-1]
                print(i,length,length-1)

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
        

string = "abcabcabxcabcabc"
M = len(string)
lps = [0]*M
computeLPSArray(string,M,lps)