# bài 2
def tinhmua(n):
    if n == 1 or n == 2 or n == 3:
        print("Mùa Xuân")
    if n == 4 or n == 5 or n == 6:
        print("Mùa Hạ") 
    if n == 7 or n == 8 or n == 9:
        print("Mùa Thu")
    if n == 10 or n == 11 or n == 12:
        print("Mùa Đông")           
n = int(input("Nhap vào 1 tháng"))
tinhmua(n)