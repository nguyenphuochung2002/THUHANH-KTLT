print("sinh viên : Nguyen Phuoc Hung 205751030110042")
###########################
def benefit(t: float, n: float, k: int) -> float:

    p = n * (t/100) * k

    return p

n = float(input("Nhập số vốn ban đầu: "))

t = float(input("Nhập % lãi suất/tháng: "))

k = int(input("Nhập số tháng gửi: "))

print("Lãi cuối kỳ: {:,}".format(benefit(t, n, k)))
