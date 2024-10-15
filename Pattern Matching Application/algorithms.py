def naive_pattern_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    
    return matches


def rabin_karp_pattern_matching(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    matches = []
    d = 256  
    h = pow(d, m-1) % prime
    p = 0  
    t = 0  

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t = t + prime

    return matches
