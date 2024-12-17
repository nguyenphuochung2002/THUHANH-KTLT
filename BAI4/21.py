print("sinh viên : Nguyen Phuoc Hung 205751030110042")
day=[]
ct=[x for x in input("nhap các số nhị phân: ").split(',')]
for p in ct:
    intp=int(p,2)
    if not intp%5:
        day.append(p)
print("cac so : ", ','.join(day))
