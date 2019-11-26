def recursivePower(base, exponent):
    if(exponent == 1):
        return base
    else:
        return base * recursivePower(base, (exponent-1))


exponent = ''
base = ''
c = 1
while(not base.isdigit() or not exponent.isdigit()):
    base = input(f"({c})Enter the base:\n")
    c += 1
    exponent = input(f"({c})Enter the exponent:\n")
    c = 1

print(f"\n{base}^{exponent}:")
print(recursivePower(int(base), int(exponent)))
