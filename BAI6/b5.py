print("sinh viên : Nguyen Phuoc Hung")
print("mssv: 205751030110042")
print("###############")
#################
class daochuoi:
    def __init__ (self,ch):
        self.chuoi=ch
    def dao (self):
        return ' '.join(reversed(self.chuoi.split())) 
a='hello .py'
t=daochuoi(a)
print(t.dao())
