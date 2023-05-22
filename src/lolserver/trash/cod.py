def solution(N):
    N = bin(N).replace("0b", "")
    longest = 0
    i = 0
    while i < len(N):
        one = N.find("1")
        sec = N[one:].find("1") - one + 1
        N = N[one+1:]
        i = sec
        if sec > longest:
            longest = sec
    return longest

print(solution(int(input())))
