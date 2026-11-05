#1
# [maria,2],[ion,4],[ana,3]

def f(clasa):
    gr = set(i[1] for i in clasa)
    gr1 = list(gr)
    gr1.sort()
    rez = []
    minim = gr1[1]
    for i in clasa:
        if i[1]==minim:
            rez.append(i)
    rez.sort()
    return rez

#2
def front(str):
    rez = []
    if len(str) < 3:
        rez.append(str)
        rez.append(str)
        rez.append(str)
    else:
        rez.append(str[0:3])
        rez.append(str[0:3])
        rez.append(str[0:3])
    return rez

#3
def dif(a,b):
    if abs(a-b)==1:
        return True
    else:
        return False

def fct(a,b):
    n = len(a)
    m = len(b)
    for x in range (n-2):
        if dif(a[x],a[x+1])==1 and dif(a[x+1],a[x+2])==1:
            for y in range (m-2):
                if b[y]==a[x] and b[y+1]==a[x+1] and b[y+2]==a[x+2]:
                    return True
    return False

#4
with open ('file.txt', "r") as f:
    dic = {}
    for line in f:
        words = line.split()
        for word in words:
            dic = {word: dic.get(word,0) + 1 for word in words}

#5
n = int(input())
def c (l):
    dic = {}
    lista = []
    for i in l:
        dic[i] = dic.get(i,0) + 1
    lista = list(dic.keys())
    lista.sort(key=lambda x: dic[x], reverse=True)
    rez = []
    rez = list[0:n]
    return rez

#sau:
from collections import Counter
def varianta_scurta(l, n):
    numaratoare = Counter(l) # Face automat dictionarul cu numarul de aparitii!
    print(numaratoare.most_common(n)) # Returneaza automat o lista sortata cu primele n


#6
a = [1,2,3]
b= ["a", "b", "c"]
for i in range(len(a)):
    print(a[i], b[i])

#8
class GeometricForm:
    def getArea(self):
        pass
    def getPerimeter(self):
        pass

class Rectangle(GeometricForm):
    def __init__(self, length, width):
        self.length = length
        self.width =  width
    def getArea(self):
        return self.length * self.width
    def getPerimeter(self):
        return 2* (self.width+self.length)

class Circle(GeometricForm):
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius * self.radius
    def getPerimeter(self):
        return 2 * 3.14 * self.radius

#9
class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def sub(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    def mul(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    def div(self, other):
        denominator = other.a ** 2 + other.b ** 2
        return Complex((self.a * other.a + self.b * other.b) / denominator, (self.b * other.a - self.a * other.b) / denominator)

#test gr 10
rez_concurs = [["test_start",10], ["robox",85],["autobot",92],["robox",85],["cyberRo",78],["test_stop",15]]
l = rez_concurs[1:-1]
print(l)
l = sorted(l,key = lambda x: x[1], reverse = False)

def elimina(l):
    rez =[]
    i=[]
    for i in l:
        if i not in rez:
            rez.append(i)
            rez[len(rez)-1][1]+=5
    return rez

with open('rezultate.txt',"w") as f:
    for i in rez_concurs:
        f.write(i[0] + " " + str(i[1]) + "\n")

class PacMan:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    __nr_instante = 0

    def __init__(self,current_position,previous_position,grid,max_x,max_y,accumulated_cost):
        self.current_position = current_position
        self.previous_position = previous_position
        self.grid = grid
        self.max_x = max_x
        self.max_y = max_y
        self.accumulated_cost = accumulated_cost
        PacMan.__nr_instante += 1

    def print(self):
        print(f" [{self.current_position}]; Previous position: [{self.previous_position}]; Grid: {self.grid}; Max X: {self.max_x}; Max Y: {self.max_y}; Accumulated cost: {self.accumulated_cost}")

    def __eq__(self, other):
        return self.current_position == other.current_position and self.previous_position == other.previous_position and self.grid == other.grid and self.max_x == other.max_x and self.max_y == other.max_y and self.accumulated_cost == other.accumulated_cost



#test alta grupa
class Graf:
    def __init__(self,listaNoduri,listaArce):
        self.listaNoduri = listaNoduri
        self.listaArce = listaArce

class GrafOrientat(Graf):
    def reach(self,x,y):
        for arc in self.listaArce:
           if arc[0] == x and arc[1] == y:
               return True
        return False

class GrafNeorientat(Graf):
    def __init__(self,listaNoduri,listaArce):
        super().__init__(listaNoduri,listaArce)
        for arc in listaArce:
            self.listaArce.append([arc[1],arc[0]])
            print("simetric")

    def isConnected(self):
        frecv = {}
        for arc in self.listaArce:
            frecv[arc[0]] = frecv.get(arc[0],0) + 1
            frecv[arc[1]] = frecv.get(arc[1],0) + 1
        for nod in self.listaNoduri:
            if nod not in frecv:
                return False
        return True

#grafuri arbori etc
from collections import deque
import heapq


# ==========================================
# 1. GRAFURI (Reprezentare prin dicționar / liste de adiacență)
# Exemplu graf: graf = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
# ==========================================

def bfs(graf, start):
    """Parcurgere în lățime (Breadth-First Search)"""
    vizitat = set([start])
    coada = deque([start])
    rezultat = []

    while coada:
        nod = coada.popleft()
        rezultat.append(nod)
        for vecin in graf.get(nod, []):
            if vecin not in vizitat:
                vizitat.add(vecin)
                coada.append(vecin)
    return rezultat


def dfs(graf, nod, vizitat=None, rezultat=None):
    """Parcurgere în adâncime (Depth-First Search) - Varianta recursivă"""
    if vizitat is None:
        vizitat = set()
        rezultat = []

    vizitat.add(nod)
    rezultat.append(nod)

    for vecin in graf.get(nod, []):
        if vecin not in vizitat:
            dfs(graf, vecin, vizitat, rezultat)
    return rezultat


# ==========================================
# 2. ARBORI BINARI
# ==========================================

class NodArbore:
    def __init__(self, valoare):
        self.valoare = valoare
        self.stanga = None
        self.dreapta = None


def inordine(radacina, rezultat=None):
    """Parcurgere Inordine: Stânga -> Rădăcină -> Dreapta (Sortare în BST)"""
    if rezultat is None:
        rezultat = []
    if radacina:
        inordine(radacina.stanga, rezultat)
        rezultat.append(radacina.valoare)
        inordine(radacina.dreapta, rezultat)
    return rezultat


def preordine(radacina, rezultat=None):
    """Parcurgere Preordine: Rădăcină -> Stânga -> Dreapta (Copiere arbore)"""
    if rezultat is None:
        rezultat = []
    if radacina:
        rezultat.append(radacina.valoare)
        preordine(radacina.stanga, rezultat)
        preordine(radacina.dreapta, rezultat)
    return rezultat


def postordine(radacina, rezultat=None):
    """Parcurgere Postordine: Stânga -> Dreapta -> Rădăcină (Ștergere arbore)"""
    if rezultat is None:
        rezultat = []
    if radacina:
        postordine(radacina.stanga, rezultat)
        postordine(radacina.dreapta, rezultat)
        rezultat.append(radacina.valoare)
    return rezultat


# ==========================================
# 3. ALGORITMI SUPLIMENTARI UTILI
# ==========================================

def dijkstra(graf_ponderat, start):
    """
    Drumul minim de la un nod sursă către toate celelalte.
    Exemplu graf: graf = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}
    """
    distante = {nod: float('inf') for nod in graf_ponderat}
    distante[start] = 0
    pq = [(0, start)]  # stochează tupluri de forma (cost_cumulat, nod)

    while pq:
        cost_curent, nod_curent = heapq.heappop(pq)

        if cost_curent > distante[nod_curent]:
            continue

        for vecin, cost_muchie in graf_ponderat.get(nod_curent, {}).items():
            cost_nou = cost_curent + cost_muchie
            if cost_nou < distante.get(vecin, float('inf')):
                distante[vecin] = cost_nou
                heapq.heappush(pq, (cost_nou, vecin))

    return distante


def componente_conexe(graf):
    """Găsește toate componentele conexe dintr-un graf neorientat."""
    vizitat = set()
    componente = []

    for nod in graf:
        if nod not in vizitat:
            componenta_curenta = []
            dfs(graf, nod, vizitat, componenta_curenta)
            componente.append(componenta_curenta)

    return componente