#for

#for x in iterable 객체:
# ...

for i in range(5):
    print(i,end=" ")
print()
a = range(5)
print(a.start,a.stop,a.step)

# 1 ~ 5
for i in range(1,6):
    print(i,end=" ")
print()
for i in range(1,10,2):
    print(i,end=" ")
print()

for i in range(5,0,-1):
    print(i,end=" ")
print()

tot=0
for i in range(1,11):
    tot+=i
print(f"sum: {tot}")

print(sum(range(1,11)))

s = "hi한글韓國💾ϗ"
for c in s:
    print(c,end=" ")
print()

for i in range(2,10):
    for j in range (1,10):
        print(f"{i} * {j} = {i*j}",end="\t")
    print()
else:
    print("End")