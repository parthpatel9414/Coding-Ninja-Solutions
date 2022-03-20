def longestPalindrome(s: str) -> str:
    p = ''
    for i in range(len(s)):
        p1 = get_palindrome(s, i, i+1)
        p2 = get_palindrome(s, i, i)
        p = max([p, p1, p2], key=lambda x: len(x))
    return p
    
def get_palindrome(s: str, l: int, r: int) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]