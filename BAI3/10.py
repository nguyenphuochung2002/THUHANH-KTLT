print("sinh viên : Nguyen Phuoc Hung 205751030110042")
###########################
import math
try:
    print("Hãy nhập bán kính hình tròn:")
    r = float(input())
    if r<0:
        print("nhap lại r")
    else:
        cv = 2*math.pi*r
        dt = pow(r,2)
        print("Chu vi hình tròn bằng: ", cv)
        print("Diện tích hình tròn bằng: ", dt)
except AttributeError as er:
    print("Lối không tồn tại số PT",str(er))
except ValueError as va:
    print("Lỗi định dạng", str(va))
