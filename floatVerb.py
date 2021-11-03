def segno(num):
	if num[0]=="-":
		return "1"
	return "0"

def getIntDec(num):
	posVirgola=num.find(".")
	parteInt=int(num[0:posVirgola])
	parteDec=float("0"+num[posVirgola:])
	return(parteInt,parteDec)

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
	while (dec!=0 and len(codifica)<13):
		n=dec*2
		parteIntera,dec=getIntDec(str(n))
		codifica=codifica+str(parteIntera)
	return (codifica)

def spostaVirgola(num):
	if num[0]=="0":
		pos=-1
		i=2
		while(num[i]=="0"):
			pos=pos-1
			i+=1
	else:
		pos=posVirgola=num.find(".")-1
	return(pos)

def riempiMantissa(num):
	while(len(num)<25):
		num=num+"0"
	return(num)


num=input("Inserisci il numero: ")
parteInt,parteDec=getIntDec(num)

print(f"Il numero inserito {num} è formato da {parteInt} e da {parteDec}")
print(f"La codifica binaria della parte intera {parteInt} è {int2bin(parteInt)}")
print(f"La codifica binaria della parte decimale {parteDec} è {dec2bin(parteDec)}")
numBinario=int2bin(parteInt)+dec2bin(parteDec)[1:]
print(f"La virgola in {numBinario} va spostata di {spostaVirgola(numBinario)}")
posVirgola=numBinario.index(".")
posPrimo1=numBinario.index("1")
print(f"il primo uno è in {posPrimo1} e la posizione della virgola è {posVirgola}")


if posPrimo1<posVirgola:
	numBinNorm="1." + numBinario[1:posVirgola]+numBinario[posVirgola+1:]
	esp=posVirgola-posPrimo1-1
else:
	numBinNorm="1." + numBinario[posPrimo1+1:]
	esp=posPrimo1-posVirgola

numBinNorm=riempiMantissa(numBinNorm)
print(f"Il numero normalizzato in binario è {numBinNorm}*2^{esp}")

esponente=127+esp
print(f"La codifica binaria dell'esponente {esponente} è {int2bin(esponente)}")

