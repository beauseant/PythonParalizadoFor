import time

    
starttime = time.time()

resultadoSi = []
resultadoNo = []

nmax = 400000 #Número máximo hasta el que queremos buscar primos


def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

results = []
for numero in range (0,nmax):
	results.append (isPrime (numero))

print ('encontrados en si %s' % results.count(True))
print ('encontrados en no %s' % results.count(False))
    
print('That took {} seconds'.format(time.time() - starttime))