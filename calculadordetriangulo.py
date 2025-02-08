import math


print(' ---------- Bem-Vindo à Calculadora de Triângulos ---------- ')
print()

def calcular_angulos(base, ladoD, ladoE):
    angulo_A = math.degrees(math.acos((ladoD**2 + ladoE**2 - base**2) / (2 * ladoD * ladoE)))
    angulo_B = math.degrees(math.acos((base**2 + ladoE**2 - ladoD**2) / (2 * base * ladoE)))
    angulo_C = math.degrees(math.acos((base**2 + ladoD**2 - ladoE**2) / (2 * base * ladoD)))
    
    return angulo_A, angulo_B, angulo_C

def triangulo_valido(base, ladoD, ladoE):
    return (ladoD + ladoE > base) and (ladoD + base > ladoE) and (ladoE + base > ladoD)

base = float(input('Digite o comprimento da base do Triângulo: '))
ladoD = float(input('Digite a altura do lado direito do Triângulo: '))
ladoE = float(input('Digite a altura do lado esquerdo do Triângulo: ')) 


while not triangulo_valido(base, ladoD, ladoE):
    print('O triângulo é invalido!')
    base = float(input('Digite o comprimento da base do Triângulo: '))
    ladoD = float(input('Digite a altura do lado direito do Triângulo: '))
    ladoE = float(input('Digite a altura do lado esquerdo do Triângulo: '))
    
print('O triângulo é válido.')

x = str(input('Deseja calcular a área do triângulo? (S/N) ')).upper()

if x == "S":
    s = (base + ladoD + ladoE) / 2
    area = math.sqrt(s * (s - base) * (s - ladoD) * (s - ladoE))
    print(f'A área do triangulo é: {area:.2f}')
  
y = str(input('Deseja calcular o ângulo do triângulo? (S/N) ')).upper()

if y == "S":
    angulos = calcular_angulos(base, ladoD, ladoE)
    print(f'Os ângulos do triângulo são: A = {angulos[0]:.2f}°, B = {angulos[1]:.2f}°, C = {angulos[2]:.2f}°')
