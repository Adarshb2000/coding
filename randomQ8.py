def solution(s: str): 
    next_ = s
    for c in ['AB', 'BA', 'CD', 'DC']:
        next_ = next_.replace(c, '')
    
    return s if next_ == s else solution(next_)


print(solution('ACBDACBD'))