# 1
s=0
price = {"apples": 10, "milk": 12, "bread": 5}
mylist = [("apples", 2), ("milk", 2)]

for i in mylist:
    key = i[0]
    value = i[1]
    s = s +  price[key] * value

print(s)

# sau: s= sum([price[nume] * cant for nume,cant in mylist])

#2
friends = [ ("andrew", 10),("george ", 20),("andrew",5), ("ann",10)]
set_f = set(nume for nume,bani in friends)
print(set_f)

#3
n = int(input())
if n%2==0:
    rez = [i for i in range(n)]
else:
    rez = [i*i for i in range(n)]
print(rez)

#4
s_in = input()
num_in = int(input())
dicti = {}
for i in range(num_in):
    dicti[i] = s_in[i]
# sau
dicti = {k:s_in[k] for k in range(num_in)}
print(dicti)

#5
rez = ''
def fct(str):
    for i in str:
        ch = chr(ord(i) + 1)
        rez = rez + ch
    return rez

#6
with open ('file1' , "r") as f , open ('file2' , "a") as g:
    for line in f:
        new_line = line.title()
        g.write(new_line)


class Gate:
    def __init__(self,tip,inputs):
        if tip not in ['AND','OR','NOT', 'true', 'false']:
            self.tip = tip
        self.inputs = inputs
    def check(self):
        if self.tip == 'AND' or self.tip=='AND' and len(self.inputs) < 2:
            return False
        elif self.tip == 'OR' or self.tip=='OR' and len(self.inputs)

      ....

    def eval(self):
