import os, subprocess
import shutil 


directory = "/home/diokoanchan/Downloads/GoodNES_3.14_goodmerged2/Nes"
directory2 = "/home/diokoanchan/Downloads/GoodNES_3.14_goodmerged2/J"
directory3 = "/home/diokoanchan/Downloads/GoodNES_3.14_goodmerged2/USA"

listaRomsE = []
listaRomsU = []
listaRomsJ = []
listaRomsNone = []

f = open('listaDeJogos.txt','w')
listaNes = open('/home/diokoanchan/Downloads/GoodNES_3.14_goodmerged2/ListaDeJogosNes.txt','r')

for item in listaNes:
	listaRomsU.append(item[0:len(item)-2])



for i in listaRomsU:
	for arq in os.listdir(directory):
		if(i == arq[0:arq.find("(")-1]):
			if("[T+" in arq):
				continue
			else:			
				listaRomsE.append(arq)			
				listaRomsNone.append(arq)
				break

for item in listaRomsE:
	print "____ COPIANDO " + item + " Para outra pasta!"
	shutil.copy(directory + "/"+ item, directory3)



print "Operacao Completa!"


'''
for arq in os.listdir(directory):
	if("(U)" in arq.upper()):
		print "Arquivo Americano ====> " + arq
		listaRomsU.append(arq)
		f.write(arq + '\n')
	elif("(E)" in arq.upper()):
		print "Arquivo Europeu ====> " + arq
		listaRomsE.append(arq)
		f.write(arq + '\n')
	elif("(J)" in arq.upper()):
		print "Arquivo Japones ====> " + arq
		listaRomsJ.append(arq)
		shutil.copy(directory + "/"+ arq, directory2)
#		os.remove(directory +"/"+ arq)	
	else:
		listaRomsNone.append(arq)
		f.write(arq + '\n')

print "Roms Japonesas Copiadas com sucesso!!"

print "LISTA SEM REFERENCIA"
print listaRomsNone
	





# copia os arquivos de um diretorio para o outro
count = 0
for arq in os.listdir(directory):
	if ("(U)" in arq.upper() or "(E)" in arq.upper()):
		shutil.copy(directory+"/"+arq, directory2)
		#subprocess.call(['cp',arq,directory2])
		count += 1
		print arq + " --> " , len(arq)

print count
'''

'''exclui os arquivos que possuem [alguma versao que nao seja !]
for arch in os.listdir(directory2):
	if("[" in arch.upper()):
		if("[!]" in arch.upper()):
			pass
		else:
			print arch
			os.remove(directory2 +"/"+ arch)


#verifica se existe essa string no nome do arquivo	
for arch in os.listdir(directory2):
	if("(U)" in arch):
		print arch , arch.find("U")
	elif("(E)" in arch):
		print arch , arch.find("E")
	
#print os.listdir("/home/diokoanchan/Downloads/Genesis")

listaarquivosU = []
listaarquivosE = []
listaarquivosNone = []
listaarquivosValidos = []
todelete = []

for arch in os.listdir(directory2):
	if("U" in arch):
		listaarquivosU.append(arch)
		print arch[0:arch.find("U")-1]
	elif("E" in arch):
		listaarquivosE.append(arch)
		print arch[0:arch.find("E")-1]
	else:
		listaarquivosNone.append(arch)

for item in listaarquivosU:
	itemName = item[0:item.find("U")-1]
	countItem = 0	
	for archtest in os.listdir(directory2):
		if(archtest[0:len(itemName)] == itemName):
			countItem = countItem + 1
	if(countItem > 1 ):
		todelete.append(item)		
		print "O arquivo ---> " + itemName + "Repete ", countItem , " Vezes!"

for ar1 in todelete:
	arname = ar1[0:ar1.find("U")-1]
	eCount = 0
	for arfinal in listaarquivosE:
		if(arname == arfinal[0:arfinal.find("E")-1]):
			eCount = eCount + 1
			print "Arquivo repetido +++++> " + arname
	if(eCount == 0):
		todelete.remove(ar1)

print "\n \n"
print "____arquivos para serem deletados_____"


for arquivo in sorted(todelete):
	print "Removendo arquivo --> " + arquivo 
	shutil.copy(directory2 +"/"+ arquivo, directory3)
	os.remove(directory2 +"/" + arquivo)
		


print "______ Arquivos sem localizacao ________"
print listaarquivosNone
print "______ Arquivos USA ________"
print listaarquivosU
print "______ Arquivos EU ________"
print listaarquivosE
'''






