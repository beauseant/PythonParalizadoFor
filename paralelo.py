from joblib import Parallel, delayed
import multiprocessing
import time



#nmax = 40000 #Número máximo hasta el que queremos buscar primos
nmax = 400000 #Número máximo hasta el que queremos buscar primos
inputs = range(0, nmax)


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


starttime = time.time()

num_cores = multiprocessing.cpu_count()

#Si accedemos a zonas de memoria comunes (listas diccionarios...) , require='sharedmem'
#pero el rendimiento cae mucho:
results = Parallel(n_jobs=num_cores )(delayed(isPrime)(i) for i in inputs)


print ('encontrados en si %s' % results.count(True))
print ('encontrados en no %s' % results.count(False))

print('That took {} seconds'.format(time.time() - starttime))
