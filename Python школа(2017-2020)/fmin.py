fmin(n):
    k = 0
    nmim = n[0]
    for i in range(len(n)):
        if nmim > n[i]:
            nmin = n[i]
            k = i
    return k, nmin
            