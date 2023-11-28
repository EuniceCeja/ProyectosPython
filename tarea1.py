pregunta_1 = input("Está lloviendo? (si/no) \n")
pregunta_1 = str.lower(pregunta_1)


if pregunta_1 == 'si':
    ventoso = input("Está ventoso? \n")
    ventoso = str.lower(ventoso)
    if ventoso == 'si':
        print("Hace demasiado viento para un paraguas")
    else:
        print("Toma un paraguas")
else:
    print("Disfruta tu día")

