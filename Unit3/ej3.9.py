#NOTA: la funcion *sum* de python suma solo numeros, no listas o cadenas de caracteres como dice el libro.

def mysum(l):
  s=0
  for el in l:
    s+=el
  return s

print mysum([1,2,3])
print mysum([1.,2,3])
print mysum([-1,2.,3])
print mysum([1,2,3+1j])
print mysum([1-1j,2-1j,3+2j])
print mysum([4])
print mysum((5,1-1j))
