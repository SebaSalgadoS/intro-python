primero = input('Ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'no son numeros'
    
if primero == 'no son numeros':
    print('el valor ingresado no es un numero')
    exit()
    
segundo = input('Ingrese segundo numero')

try:
    segundo = int(segundo)
except:
    segundo = 'no son numeros'
    
if segundo == 'no son numeros':
    print('el valor ingresado no es un numero')
    exit()

if primero == 'no son numeros' or segundo == 'no son numeros':
    print('ingresaste mal un numero, prueba de nuevo solo con numeros')
    
simbolo = input('Ingrese operacion: ')

if simbolo == '+':
    print('La suma es: ', primero + segundo)
elif simbolo == '-':
    print('La resta es: ', primero - segundo)
elif simbolo == '*':
    print('La multiplicacion es: ', primero * segundo)
elif simbolo == '/':
    print('La division es: ', primero / segundo)
else:
    print('El simbolo ingresado no es valido')