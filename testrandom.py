import time
import nolds
import random

class MyRandom:
    def __init__(self, seed):
        # Inicializa a matriz de estado com a semente
        self.mt = [0]
        self.index = 0
        self.mt[0] = seed
        for i in range(1, 100):
            if i > 0:
                self.mt.append((7 * self.mt[i-1] / 7* self.mt[ i - 2])*13.0/11.0)
            else: 
                self.mt.append((7 * self.mt[i] )*13.0/11.0)

    def extract_number(self):
        if self.index == 0:
            self.index = (self.index + 1)
            y = self.mt[self.index]
        x = y * 1/1e28 # normalizando
        last_two_digits_str = str(x)[-2:] # transformando e string e pegando os ultimos 2 digitos 
        last_two_digits = int(last_two_digits_str)
        last_two_digits = (60 * last_two_digits)/100 # transformando de 0 a 99 para 1 a 60
        rand = int(last_two_digits)
        return rand

sena = list(range(1, 1000)) # Lista com os números de 1 a 60
n = 0
pick = []
seed = MyRandom(int(time.perf_counter_ns()))
test = 0
while n < 1000:
    x = seed.extract_number()
    try:
        pick.append(x)
        n += 1
        time.sleep(0.003)
        seed = MyRandom(int(time.perf_counter_ns()))
    except:
       pass
        
result = [sena[x] for x in (pick)]
rand_list = (result)
print(rand_list)

#--------------------------------------------- teste -----------------------------------------#
entropy = nolds.sampen(rand_list, emb_dim=2, tolerance=0.2)

print(f"Entropia aproximada: {entropy}")


weaktest = (1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6)
entropy2 = nolds.sampen(weaktest, emb_dim=2, tolerance=0.2)

print(f"Entropia aproximada fraca: {entropy2}")

hardtest = []
while len(hardtest) < 1000:
    hardtest.append(random.randint(1,60))
    
entropy3 = nolds.sampen(hardtest, emb_dim=2, tolerance=0.2)
print(f"Entropia aproximada forte da biblioteca radom: {entropy3}")