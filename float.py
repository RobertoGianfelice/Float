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
	while (dec!=0 and len(codifica)<100):
		n=dec*2
		parteIntera,dec=getIntDec(format(n,'.100f'))
		codifica=codifica+str(parteIntera)
	return (codifica)

def normalizza(numBin):
	posVirgola=numBin.index(".")
	posPrimo1=numBin.index("1")

	if posPrimo1<posVirgola:    #111.000011 -> esp=3-0-1=2
		numBinNorm="1." + numBin[1:posVirgola] + numBin[posVirgola+1:]
		esp=posVirgola-posPrimo1-1
	else:                       #0.000001111 -> esp=1-7=6
		numBinNorm="1." + numBin[posPrimo1+1:]
		esp=posVirgola-posPrimo1
	return(numBinNorm,esp)

def riempiMantissa(num):
	if len(num)>23:
		return(num[0:24])

	while(len(num)<23):
		num=num+"0"
	return(num)

def riempiEsponente(esponente):
  while(len(esponente)<8):
    esponente="0"+esponente
  return(esponente)


numInserito=input("Inserisci il numero: ")
segno,num=calcolaSegno(numInserito)
parteInt,parteDec=getIntDec(num)
numerointerobinario=int2bin(parteInt)
numBinario=int2bin(parteInt)+dec2bin(parteDec)[1:]
numBinNorm,esp=normalizza(numBinario)
numBinNorm=riempiMantissa(numBinNorm)
esp=esp+127
espBin=int2bin(esp)
print(espBin)
esponente=riempiEsponente(espBin)

print(f"La codifica in floatingPoint di {numInserito} è {segno} {esponente} {numBinNorm[2:]}")
