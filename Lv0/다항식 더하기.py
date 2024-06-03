def solution(polynomial):
    answer = ''
    poly_list = polynomial.split(' ')
    print(poly_list)
    
    coefficient = 0
    constant = 0
    for i in range (len(poly_list)) :
        if ('x' in poly_list[i]) :
            c = poly_list[i].replace('x', '')
            print(c)
            if (len(c) == 0) :
                coefficient += 1
            else :
                coefficient += int(c)
        else :
            if (poly_list[i] != '+') :
                constant += int(poly_list[i])
    
    if coefficient != 0 :
        if coefficient != 1:
            answer += str(coefficient)
        answer += 'x'
    if constant != 0 :
        if coefficient != 0 :
            answer += ' + '
        answer += str(constant)
    
    return answer