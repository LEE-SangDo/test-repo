print('이 프로그램은 _______를 구하기 위한 프로그램입니다.')
print('두 수를 입력해주세요')

a,b=map(int, input().split())

print('결과는 다음과 같습니다 :')

if a<=24 and b<=60:
    if b>=40:
        print(a,b-40)
    else:
        print(a-1, 60-abs(b-40))
else:
    print('X')
