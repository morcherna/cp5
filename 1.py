print("Введите N ")
try:
 N = int(input())
except ValueError:
 print('Ошибка ')
else:
  M = 0
while N>0:
   N_1 = N % 10
   if N_1 % 2 == 1:
    M = M + N_1
    N = N // 10
   else:
    N = N // 10
print(M)
  
 