from collections import Counter
from joblib import Parallel, delayed
import multiprocessing
import time


def getCommon ( item ):

	lista = item ['palabras']
	most_common,num_most_common = Counter(lista).most_common(1)[0]
	

	return {'id':item['id'], 'nombre':item['nombre'], 'palabras':most_common}

lista = []

lista.append ({'id':0, 'nombre':'pepe', 'palabras':['casa', 'casa', 'camion', 'coche']})
lista.append ({'id':1, 'nombre':'pepex', 'palabras':['hola', 'adios', 'adios', 'adios']})

print (lista)

#total = [ getCommon (item) for item in lista]

#total = map ( getCommon , lista)
num_cores = multiprocessing.cpu_count()
total = Parallel(n_jobs=num_cores )(delayed(getCommon)(item) for item in lista)

print ( total )
