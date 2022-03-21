def solution(n, k):
    ### YOUR CODE HERE ###
    split = k // n
    left = k % n
    return split, left
