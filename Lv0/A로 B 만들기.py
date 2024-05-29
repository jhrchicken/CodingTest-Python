def solution(before, after):
    sorted_before = ''.join(sorted(before))
    sorted_after = ''.join(sorted(after))

    if sorted_before == sorted_after :
        return 1
    else :
        return 0