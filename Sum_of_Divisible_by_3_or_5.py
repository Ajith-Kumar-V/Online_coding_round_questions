def solution(number):
    sums=0
    for i in range(number):
        if i%3==0 or i%5==0:
            sums+=i
    print(sums)
number=int(input())
solution(number)
