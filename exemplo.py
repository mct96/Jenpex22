import numpy as np
np.random.seed(0)
t = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
N = 12
POP_SIZE = 8
GEN = 10000

def hamming(a, b):
    return np.abs(a - b).sum()

def eval_fitness(a):
    dist = hamming(a, t)
    return N - dist
    
def init(qnt):
    return np.random.randint(low=0, high=1+1, size=(qnt, N))

def select(fitness):
    prob = fitness / fitness.sum()
    return np.random.choice(range(POP_SIZE), p=prob)
    
P = init(qnt=POP_SIZE)
fitness = np.array([eval_fitness(i) for i in P])

def mutation(P, pm):
    Pnew = np.copy(P)
    for i in range(len(P)):
        idx = np.random.randint(low=0, high=N)
        if np.random.rand() < pm:
            v = np.random.randint(low=0, high=1+1)
            Pnew[i, idx] = v
    return Pnew
    
def crossover_point(ch1, ch2):
    r = np.random.randint(low=0, high=N)
    child1 = np.concatenate((ch1[:r], ch2[r:]))
    child2 = np.concatenate((ch2[:r], ch1[r:]))
    return child1, child2
    
def crossover(P, fitness, pc):
    Pnew = list()
    for i in range(len(P) // 2):
        p1 = select(fitness)
        p2 = select(fitness)
        if np.random.rand() < pc:
            ch1, ch2 = crossover_point(P[p1], P[p2])
            Pnew.append(ch1)
            Pnew.append(ch2)
        else:
            Pnew.append(P[p1])
            Pnew.append(P[p2])
    return np.array(Pnew)
        
pc = 0.99
pm = 0.01
P = init(POP_SIZE)
print(P)
print("\n"*3)
for i in range(GEN):
    fitness = np.array([eval_fitness(i) for i in P])
    
    if np.any(fitness == 12):
        print(f"\nSolução encontrada na geração {i}\n")
        print(P)
        break
        
    P = crossover(P, fitness, pc)
    P = mutation(P, pm)
    

    
        
