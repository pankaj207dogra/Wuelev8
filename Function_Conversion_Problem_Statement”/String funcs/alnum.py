def alnum(a):
    if a.regexMatch(a,'(\\d+),(\\a+),(\\A+)'):
        return True
    else:
        return False