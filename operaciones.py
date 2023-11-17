def sumar(a, b):
 return a + b

def restar(a,b):
 return a-b

def producto(a,b):
 return a*b

def division(a,b):
 if b == 0:
    return "¡DIV/0!"
 else:
  return a/b
 
if __name__ == "__main__":
 print(sumar(5, 3))
 print(restar(1,1))
 print(producto(1,2))
 print(division(1,2))