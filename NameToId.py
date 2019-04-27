def NameToId(ss):
    if ss[0]=='*':
        return ss.replace('*cqupc19_','100')
    else:
        return ss.replace('cqupc19_','')