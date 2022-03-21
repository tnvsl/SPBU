def solution(a, b):
    ### YOUR CODE ###
    d = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            d.append(a[i])
            i += 1
        else:
            if b[j] in a:
                j += 1
            else:
                d.append(b[j])
                j += 1

    d += a[i:]
    d += b[j:]

    #with sort
    #for i in a:
        #d.append(i)
    #for n in b:
        #if n not in a:
            #d.append(n)
    #d.sort()
    return d
