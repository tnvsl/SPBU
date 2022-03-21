def solution(total):
    ### YOUR CODE HERE ###
    hours = (total // 60) % 24
    mins = total % 60

    return (f'{hours} {mins}')
