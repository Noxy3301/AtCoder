a = input()
b = input()
 
length = len(a)
 
i = 0
count = 0
 
while i < length:
  if a[i] != b[i]:
    count = count + 1
  i = i + 1
 
print(count)