#bài 3
def tinhtong(n):
    s = 0
    while n <= 0:
        n = int(input("moi ban nhap lại: "))
    for i in range(1,n + 1):
        if i == 13:
            break
        s +=i
    print("s = ",s)    
n = int(input("moi ban nhap 1 so nguyen duong N: "))
tinhtong(n)