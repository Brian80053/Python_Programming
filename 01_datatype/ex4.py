# 문자열
# "", ''

a="python"
print(a,type(a))

# I'll be back
a="I'll be back."
print(a)

#"The Cake is a lie"
a='"The Cake is a lie"'
print(a)

multiline = """
Life is Short
You need Python
"""

print(multiline)

#docstring
def func():
    """이 함수는 multiline의 필요성을 굳이 의도하려 만든 함수입니다."""
    pass

print(func.__doc__)

# 문자열 연결
print("Hello"+" "+"Python")

#문자열 반복
print("Hello " * 10)
print("-" * 10)

# 문자열끼리만 + 가능
# print("Hello " + 10)

print("Hello" + str(10))

print(int("10") + int("2"))