if __name__ == '__main__':
    
#     solution a
#     这 a 是我抄来的
    str = input()
    print(any(c.isalnum()  for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))
    
#     solution b
    
    s = input()
    # first define 5 var for the outcomes
    anyAlphanumeric  = 0
    anyAlphabetical  = False
    anyDig = 0
    anyLower = 0
    anyUpper = 0
    for i in range(len(s)):
        if s[i].isalnum() and anyAlphanumeric == 0:
            anyAlphanumeric = 1

        if s[i].isalpha() and anyAlphabetical == 0:
            anyAlphabetical = True

        if s[i].isdigit() and anyDig == 0:
            anyDig = 1

        if s[i].isupper() and anyUpper == 0:
            anyUpper = 1

        if s[i].islower() and anyLower == 0:
            anyLower = 1

    print(bool(anyAlphanumeric))
    print(anyAlphabetical)
    print(bool(anyDig))
    print(bool(anyLower))
    print(bool(anyUpper))

#  remember the most important thing is to do the lian-lian-look
#  dont you ever make a silly mistake while typing the if statements