def digitar(text):
    a = True
    while a:
        try:
            v = -1
            v = int(input(text))
        except ValueError:
            print("digite um valor válido")
        else:
            return v
        if v >= 0:
            a = False

c = digitar("capital inicial: R$")

i = digitar("juros de: ")
t = digitar("tempo de: ")

def juros(c, i, t):
    if c >=0 and i >=0 and t >= 0:
        j = c * (i / 100) * t
    return j



m = c + juros(c, i, t)
print(m)