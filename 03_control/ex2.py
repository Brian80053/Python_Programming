# 반복문: while문, for문

#while문
i=1
while i<=10:
    print(i)
    i+=1
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2

i=0
while i<len(nums):
    if(nums[i]==target):
        print("1")
    i+=1
else:
    print("0")

i=2
tot=0
while i<=10:
    tot+=i
    i+=2
print(f"sum: {tot}")