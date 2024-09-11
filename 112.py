import heapq


with open('input.txt', 'r') as file:
    content = file.read()

a, b = [int(x) for x in content.splitlines()[0].split()]

l = []
for line in content.splitlines()[1:]:
    a, b, c = [int(x) for x in line.split()]
    l.append((a, b, c))

g = {}


for a, b, c in l:
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    if b in g[a]:
        g[a][b] = min(g[a][b], c)
    else:
        g[a][b] = c

def dij(g, s):
    udaljenosti = {v: float('infinity') for v in g}
    visited = set()
    udaljenosti[s] = 0
    prijasnji = {v: None for v in g}
    pq = [(0, s)]
    while pq:
        v, c = heapq.heappop(pq)
        if c in visited:
            continue
        visited.add(c)
        for sc, sv in g[c].items():
            novaUdaljenost = sv + v
            if novaUdaljenost < udaljenosti[sc]:
                prijasnji[sc] = c
                udaljenosti[sc] = novaUdaljenost
                heapq.heappush(pq, (novaUdaljenost, sc))
                
    return udaljenosti, prijasnji


def ispisPuta(prijasnji, dest):
    put = []
    while dest != None:
        put.append(dest)
        dest = prijasnji[dest]
    return put[::-1]


def alternativniput(g, s, dst):
    udaljenosti, prijasnji = dij(g, s)
    najkraciput = ispisPuta(prijasnji, dst)
    
    if len(najkraciput) <= 1:
        return None, "Nema alternativnog puta, samo jedan čvor"
    
   
    a, b = najkraciput[0], najkraciput[1]
    originalWeight = g[a].pop(b)
    
   
    noveUdaljenosti, noviPut = dij(g, s)
    
   
    g[a][b] = originalWeight
    
    alternativniPut = ispisPuta(noviPut, dst)
    return alternativniPut, noveUdaljenosti[dst]


def brojPutova(g, s, d, visited, trenutni_put, svi_putovi):
    trenutni_put.append(s)
    if s == d:
        svi_putovi.append(list(trenutni_put))  
    else:
        visited.add(s)
        for susjed in g[s]:
            if susjed not in visited:
                brojPutova(g, susjed, d, visited, trenutni_put, svi_putovi)
        visited.remove(s)
    trenutni_put.pop()


def brojAlternativnihPutova(g, s, d):
    visited = set()  
    svi_putovi = []  
    trenutni_put = []  
    
    brojPutova(g, s, d, visited, trenutni_put, svi_putovi)
    
    if len(svi_putovi) <= 1:
        return "Nema alternativnih putova."
    else:
        
        print(f"Ukupan broj putova: {len(svi_putovi)}")
        print("Svi mogući putovi:")
        for i, put in enumerate(svi_putovi, 1):
            print(f"Put {i}: {put}")
        return f"Broj alternativnih putova: {len(svi_putovi) - 1}"


udaljenosti, put = dij(g, 1)
print("Najkraće udaljenosti su: ", udaljenosti)
fput = ispisPuta(put, 10)
print("Najkraći put je:", fput)


alternativniPut, rezultat = alternativniput(g, 1, 10)
if alternativniPut:
    print("Alternativni put je:", alternativniPut)
else:
    print(rezultat)


broj_alt_putova = brojAlternativnihPutova(g, 1, 10)
print(broj_alt_putova)
