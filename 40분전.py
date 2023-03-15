a,b=map(int, input().split())
if a<=24 and b<=60:
    if b>=40:
        print(a,b-40)
    else:
        print(a-1, 60-abs(b-40))
else:
    print('X')