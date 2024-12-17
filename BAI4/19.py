print("sinh viên : Nguyen Phuoc Hung 205751030110042")
t=tuple()
for i in range(1,100):
    dem=0
    for j in range (1,i+1):
        if(i%j == 0):
            dem = dem + 1
    if(dem == 2):
        t=t+(i,)
print(t)
