def NameToId(ss):
    if ss[0]=='*':
        return ss.replace('*cqupc18_team','100')
    else:
        return ss.replace('cqupc18_team','')