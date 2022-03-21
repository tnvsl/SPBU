def solution(x1, y1, x2, y2):
    ### YOUR CODE ###
    if abs(x2 - x1) <= 1:
        if abs(y2 - y1) <= 1:
            return True

    return False
