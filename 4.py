renta_anual = int(input("Ingrese renta anual "))
if renta_anual < 500000:
    print("Impuesto del 5%")
elif renta_anual>= 500000 and renta_anual < 1000000:
    print("Impuesto del 15%")
elif renta_anual>= 1000000 and renta_anual < 1500000:
    print("Impuesto del 20%")
elif renta_anual>= 1500000 and renta_anual < 2500000:
    print("Impuesto del 30%")
else:
    print("Impuesto del 45%")