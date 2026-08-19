# 입출력

# 1개 입력
a = input()
print(a)
print(type(a))

# 정수 변환
a = int(input())
print(type(a))

b = float(input())
print(b,type(b))

# 정수 2개 입력
a = int(input())
b = int(input())
print(a,b)

a,b = map(int,input().split())
a= input().split()
print(a)

# map 사용하기
# map (함수, 리스트)
a, b, c = map(int, input().split())
print(a)

# 리스트로 변환
a = list(map(int,input().split()))
print(a)