m = int(input("Ievadi no kuras pakāpes jāapreķina: "))
N = int(input("Ievadi līdz kurai pakāpei jāapreķina: "))
for i in range(m,N+1):
  n = pow(2,i)
  print(n)