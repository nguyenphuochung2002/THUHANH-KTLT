
print("sinh viên : Nguyen Phuoc Hung")
print("mssv: 205751030110042")
print("###############")
input_file=open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()
