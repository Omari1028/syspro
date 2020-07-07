def fb(n):

if n % 3 == 0 and  n % 5 == 0:
 return "FuzzBizz"

elif n % 5 == 0:
 return "Bizz"

elif n % 3 == 0:
 return "Fuzz"

else:
 return ""


i = 1
while i <= 20:
print(i, fb(i))
i = i + 1
