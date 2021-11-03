num=input("Inserisci il numero: ")

posVirgola=num.find(".")

parteInt=int(num[0:posVirgola])
parteDec=float("0"+num[posVirgola:])

print(f"Il numero inserito {num} è formato da {parteInt} e da {parteDec}")
print(f"La codifica binaria di numero inserito {num} è formato {bin(parteInt)}")
