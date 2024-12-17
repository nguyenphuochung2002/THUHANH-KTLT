print("sinh viên : Nguyen Phuoc Hung")
print("mssv: 205751030110042")
print("###############")
class IOString:
    def __init__ (self):
        self.chuoi=""
    def get_String(self):
        self.chuoi=input()
    def print_String(self):
        print(self.chuoi.upper())
chuoi=IOString()
chuoi.get_String()
chuoi.print_String()
