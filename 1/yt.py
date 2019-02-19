import turtle

t1 = turtle.Turtle()
t1.speed(10000)
t1.width(2)
red = "red"
orr = "orange"
yell = "yellow"
gree = "green"
blu = "blue"
ind = "indigo"
vio = "violet"
test = 0
flip = 0
smp = 0

def form(t,pl,pi,pu,py, smol):
        smol**=2
        t.color(pl, pi)
        t.begin_fill()
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.left(smol)
        t.forward(50)
        t.right(45)
        t.forward(25)
        
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()
        t.right(6)
        t.right(2)

        t.color(pu, py)
        t.begin_fill()
        t.forward(90)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(90)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()
        t.right(8)
        t.right(4)
def flippy(flp, tst):
    if flp == 0:
        tst+=1
        return tst
    elif flp == 1:
        tst-=1
        return tst
    
for petal in range(28):
    test = flippy(flip, test)
    if test == 0:
        flip = 0
        one = red
        two = orr
        three = yell
        four = gree
    elif test == 1:
        one = orr
        two = yell
        three = gree
        four = blu
    elif test == 2:
        one = yell
        two = gree
        three = blu
        four = ind
    elif test == 3:
        one = gree
        two = blu
        three = ind
        four = vio
    elif test == 4:
        one = blu
        two = ind
        three = vio
        four = red
    elif test == 5:
        one = ind
        two = vio
        three = red
        four = orr
    elif test == 6:
        one = vio
        two = red
        three = orr
        four = yell
        flip = 1
    
    #test +=1
        
    form(t1,one,two,three,four,test)
