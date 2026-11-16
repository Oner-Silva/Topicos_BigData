print("Estructuras condicionales")

# 1. Condicional simple
nota = 17
if nota >= 10.51:
    print("Aprobado")

# 2. Condicional doble
edad = 17
if edad >= 18:
    print("Tomar bebidas en exceso es malo")
else:
    print("No apto para menores")

# 3. Condicionales anidadas (if - elif - else)
nota = 17
if nota > 17 and nota <= 20:
    print("Alumno brillante")
elif nota >= 14 and nota <= 17:
    print("Alumno bueno")
elif nota >= 10.5 and nota < 14:
    print("Alumno regular")
else:
    print("Alumno con déficit")

# 4. Condicional múltiple (match-case en Python 3.10 o superior)
num = 4
match num:
    case 1:
        print("Vocal A")
    case 2:
        print("Vocal E")
    case 3:
        print("Vocal I")
    case 4:
        print("Vocal O")
    case 5:
        print("Vocal U")
    case _:
        print("No es una vocal")