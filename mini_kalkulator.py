a_txt = input("Jep numrin A: ")
b_txt = input("Jep numrin B: ")

if not (a_txt.lstrip("-").isdigit() and b_txt.lstrip("-").isdigit()):
    print("Gabim: te dhenat duhet te jene numra te plote (p.sh. 7, -3).")
    raise SystemExit(1)

a = int(a_txt)
b = int(b_txt)

print("Shuma:", a + b)
print("Produkti:", a * b)
