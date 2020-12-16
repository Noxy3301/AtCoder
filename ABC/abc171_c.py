num = int(input())
data = []
dataAlpha = []
 
def div_sho(a):
  sho = a // 26
  if a % 26 == 0:
    sho -= 1
  return sho
 
def div_amari(a):
  amari = a % 26
  if amari == 0:
    amari = 26
  return amari
 
while num > 26:
  data.append(div_amari(num))
  num = div_sho(num)
  
data.append(num)
data.reverse()
 
for d in data:
  dataAlpha.append(chr(d + 96))
 
print("".join(dataAlpha))