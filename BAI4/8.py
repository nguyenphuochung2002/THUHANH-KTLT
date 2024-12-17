def tu_dai_nhat(s):
    tudainhat = ""
    dscactu = s.split()
    for tu in dscactu:
        if (len(tu) > len(tudainhat)) or (len(tu) == len(tudainhat) and tu < tudainhat):
            tudainhat = tu
    return tudainhat
s = input()
print(tu_dai_nhat(s))
