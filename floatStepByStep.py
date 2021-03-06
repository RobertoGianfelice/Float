def calcolaSegno(num):
	if num[0]=="-":
		return "1",num[1:]
	return "0",num[1:]

def getIntDec(num):
	parteInt,parteDec=num.split(".")
	parteDec="0."+parteDec
	return(int(parteInt),float(parteDec))

def int2bin(num):
	if num==0:
		return "0"
	codifica=""
	while (num!=0):
		resto=num%2
		codifica=str(resto)+codifica
		num=num//2
	return(codifica)

def dec2bin(dec):
	codifica="0."
	while (dec!=0 and len(codifica)<25):
		n=dec*2
		parteIntera,dec=getIntDec(str(n))
		codifica=codifica+str(parteIntera)
	return (codifica)


numInserito=input("Inserisci il numero: ")
segno,num=calcolaSegno(numInserito)
parteInt,parteDec=getIntDec(num)
print(parteInt,parteDec)
numerointerobinario=int2bin(parteInt)

print(f"{parteInt} in binario vale {numerointerobinario}")

#numBinario=int2bin(parteInt)+dec2bin(parteDec)[1:]
#numBinNorm,esp=normalizza(numBinario)
#numBinNorm=riempiMantissa(numBinNorm)
#esponente=riempiEsponente(int2bin(127+esp))

#print(f"La codifica in floatingPoint di {numInserito} è {segno} {esponente} {numBinNorm[2:]}")
