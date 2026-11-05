#1
import math
def softmax(x):
    sum_x = sum([math.exp(j) for j in x])
    rez = [(math.exp(i) / sum_x) for i in x]
    return rez
print("Funcția mea: ", softmax(a))

#2
