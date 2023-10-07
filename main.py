A = float(input("Veuillez saisir la valeur de A :"))
op = input("Veuillez saisir l'opérateur: op ")
B = float(input("Veuillez saisir la valeur de B: "))
if op == "+" :
    print("A + B = ", A+B)
elif op == "-" :
      print("A - B = ", A-B)
elif op == "/" :
    if B != 0 :
     print("A / B = ", A/B)
    else:
      print("La division par 0 est impossible")
elif op == "*" :
    print("A * B = ", A*B )

else:
     print("L'opérateur est incorrect")