import random,math,sys

def get_num():
    while True:
        n,k = input().split()
        
        if int(n) >= int(k):
            break
    k = int(k) - 1
    n = int(n)
    dif = int(n)-int(k)
    #print(dif)
    money = 2**dif + int(k)*2
    print(money)


def main():
    number_of_times = int(input())
    times = 0
    while times< number_of_times:
        times += 1
        get_num()
        
main()
