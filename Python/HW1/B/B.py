def solution(n):
    ### YOUR SOLUTION ###
    if n == 0:
        return ''
    else:
        a = '   _~_   ' *n
        b = '  (o o)  ' *n
        c = ' /  V  \ ' *n
        d = '/(  _  )\\' *n
        e = '  ^^ ^^  ' *n
        penguin = (a + '\n' + b+ '\n'+ c+ '\n'+ d+ '\n'+ e)
        return penguin