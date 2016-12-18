import string
arr = [
"\n+ + + + + + + + + +",
"\no + + + + + + + + +",
"\n+ o + + + + + + + +",
"\n+ + o + + + + + + +",
"\n+ + + o + + + + + +",
"\n+ + + + o + + + + +",
"\n+ + + + + o + + + +",
"\n+ + + + + + o + + +",
"\n+ + + + + + + o + +",
"\n+ + + + + + + + o +",
"\n+ + + + + + + + + o"
]
inp = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3" 
new = string.replace(inp, "R", "R(")
new1 = string.replace(new, ",", "),")
new2 = string.replace(new1, "L", "L(")
new3 = new2 + ")"
x = 0
y = 0
z = 0
gnomes = []

#R(2), L(3), R(2), R(2), R(2), R(5), L(5), R(5), R(3)

def draw(x, y):
    i = 0
    while i < 10:
        i = i + 1
        if (i == y):
            print arr[x]
        else:
            print arr[0]

def forward():
    global z
    global x
    global y
    global gnomes
    if z == 0:
        y = y - 1
    elif z == 1:
        x = x + 1
    elif z == 2:
        y = y + 1
    else:
        x = x - 1
    gnomes.append( pocketGnome(x, y))

def R(mult):
    global z
    z = z + 1
    if z > 3:
        z = 0
    elif z < 0:
        z = 3
    iR = 0
    while iR < mult:
        iR = iR + 1
        forward()

def L(mult):
    global z
    z = z - 1
    if z > 3:
        z = 0
    elif z < 0:
        z = 3
    iL = 0
    while iL < mult:
        iL = iL + 1
        forward()

class pocketGnome:
    littleHat = "red"
    gnomex = 0
    gnomey = 0
    def __init__(self, x2, y2):
        self.gnomex = x2
        self.gnomey = y2

for gnome in gnomes:
    for gnome2 in gnomes:
        if gnome.gnomex == gnome2.gnomex and gnome.gnomey == gnome2.gnomey and gnome != gnome2:
            print gnome.gnomex
            print gnome.gnomey






