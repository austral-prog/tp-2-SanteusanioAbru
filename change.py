def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    cents = int((vuelto-pesos)*100)
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}") 
    print(f"Centavos:\n{cents}")
change()
