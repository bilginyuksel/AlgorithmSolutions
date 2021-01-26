def expand(s, idx, double= False):
    left = right = idx
    if double: right += 1
    if s[left] != s[right]: return 0
    
    count, left, right = 1, left-1, right+1
    const = s[left if not double else left + 1]
        
    while left >= 0 and right < len(s):
        valid = s[left] == s[right] and s[left] == const 
        if not valid: break
        count += 1
        left -= 1
        right += 1
        
    return count

def substrCount(n, s, count= 1):
    for idx in range(n-1): count += expand(s, idx) + expand(s, idx, True)
    return count
