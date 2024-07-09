first = int(input("первое число"))
deystvie = (input("выберете действие +,-,/,*"))
second = int(input("второе число"))
def calculator(first,deystvie,second):
 if deystvie == '+':
  return first + second
 elif deystvie == '-':
  return first - second
 elif deystvie == '/':
  return first / second
 elif deystvie == '*':
  return first * second
 else:
  print("неподходяший символ")
print (calculator(first,deystvie,second))