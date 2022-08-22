import turtle

def drawSquare(t,sz,c):
    t.color("black")
    t.fillcolor(c)
    t.left(90)
    t.begin_fill()
    for i in range(4):
        t.forward(sz)
        t.right(90)
    t.right(90)
    t.forward(sz)
    t.end_fill()

def newRow(t,sz,n):
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz*n)
    t.right(180)


def main():
    wn=turtle.Screen()
    grace=turtle.Turtle()
    grace.speed(1000)
    grace.left(180)
    grace.forward(170)
    grace.left(90)
    grace.forward(70)
    grace.left(90)
    for a in range(10):                 #start of row 1
        drawSquare(grace,10,"yellow")
    for b in range(3):
        drawSquare(grace,10,"black")
    for c in range(5):
        drawSquare(grace,10,"yellow")
    for d in range(3):
        drawSquare(grace,10,"black")
    for e in range(10):                 #end of row 1 (bottom row)
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for f in range(9):                  #start of row 2
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    for g in range(3):
        drawSquare(grace,10,"blue")
    for h in range(5):
        drawSquare(grace,10,"black")
    for i in range(3):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for j in range(9):                  #end of row 2
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for k in range(2):                  #start of rows 3 and 4
        for l in range(9):
            drawSquare(grace,10,"yellow")
        for m in range(3):
            drawSquare(grace,10,"black")
        drawSquare(grace,10,"blue")
        drawSquare(grace,10,"black")
        for n in range(3):
            drawSquare(grace,10,"light blue")
        drawSquare(grace,10,"black")
        drawSquare(grace,10,"blue")
        for o in range(3):
            drawSquare(grace,10,"black")
        for p in range(9):              #end of rows 3 and 4 
            drawSquare(grace,10,"yellow")
        newRow(grace,10,31)
    for q in range(9):                  #start of row 5
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    for r in range(3):
        drawSquare(grace,10,"blue")
    for s in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for v in range(2):
        drawSquare(grace,10,"black")
    for t in range(3):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for u in range(9):                  #end of row 5
        drawSquare(grace,10,"yellow")
    newRow (grace,10,31)
    for w in range(10):                 #start of row 6
        drawSquare(grace,10,"yellow")
    for x in range(3):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for y in range(3):
        drawSquare(grace,10,"black")
    for x in range(10):                 #end of row 6
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for z in range(11):                 #start of row 7
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    for aa in range(2):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    for ab in range(2):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for ac in range(11):                #end of row 7
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for ad in range(12):                #start of row 8
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for ae in range(3):
        drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for af in range(12):                #end of row 8
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for ag in range(8):                 #start of row 9
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"blue")
    for ah in range(13):
        drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"blue")
    for ai in range(8):                 #end of row 9
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for aj in range(7):                 #start of row 10
        drawSquare(grace,10,"yellow")
    for ak in range(17):
        drawSquare(grace,10,"blue")
    for al in range(7):                 #end of row 10
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for am in range(6):                 #start of row 11
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    for an in range(2):
        drawSquare(grace,10,"blue")
    for ao in range(2):
        drawSquare(grace,10,"light blue")
    for ap in range(3):
        drawSquare(grace,10,"blue")
    for aq in range(3):
        drawSquare(grace,10,"black")
    for ar in range(3):  
        drawSquare(grace,10,"blue")
    for av in range(2):
        drawSquare(grace,10,"light blue")
    for at in range(2):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for au in range(6):                 #end of row 11
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for aw in range(6):                 #start of row 12
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    for ax in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"blue")
    for ay in range(5):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    for az in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for ba in range(6):                 #end of row 12
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for bb in range(6):                 #start of row 13
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"white")
    for bc in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"blue")
    for bd in range(3):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    for be in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"white")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    for bf in range(6):                 #end of row 13
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for bg in range(5):                 #start of row 14
        drawSquare(grace,10,"yellow")
    for bh in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bi in range(4):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bj in range(5):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    for bk in range(4):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bl in range(2):
        drawSquare(grace,10,"black")
    for bm in range(5):                 #end of row 14
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for bl in range(5):                 #start of row 15
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bm in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"white")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bn in range(5):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"white")
    for bo in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light pink")
    for bp in range(5):                 #end of row 15
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for bq in range(4):                 #start of row 16
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for br in range(3):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bs in range(7):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    for bt in range(3):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"black")
    for bu in range(4):                 #end of row 16
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for bv in range(4):                 #start of row 17
        drawSquare(grace,10,"yellow")
    for bw in range(3):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for bx in range(9):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    for by in range(3):
        drawSquare(grace,10,"light pink")
    for bz in range(4):                 #end of row 17
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for ca in range(3):                 #start of row 18
        drawSquare(grace,10,"yellow")
    for cb in range(4):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"light blue")
    for cc in range(11):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"light blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for cd in range(4):
        drawSquare(grace,10,"light pink")
    for ce in range(3):                 #end of row 18
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for cf in range(3):                 #start of row 19
        drawSquare(grace,10,"yellow")
    for cg in range(4):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    for ch in range(11):
        drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"blue")
    for ci in range(4):
        drawSquare(grace,10,"light pink")
    for cj in range(3):                 #end of row 19
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for ck in range(3):                 #start of row 20
        drawSquare(grace,10,"yellow")
    for cl in range(4):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    for cm in range(2):
        drawSquare(grace,10,"yellow")
    for cn in range(2):
        drawSquare(grace,10,"black")
    for co in range(7):
        drawSquare(grace,10,"blue")
    for cp in range(2):
        drawSquare(grace,10,"black")
    for cq in range(2):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"blue")
    for cr in range(3):
        drawSquare(grace,10,"light pink")
    for cs in range(4):                 #end of row 20
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for ct in range(3):                 #start of row 21
        drawSquare(grace,10,"yellow")
    for cu in range(3):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for cv in range(4):
        drawSquare(grace,10,"yellow")
    for cw in range(2):
        drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for cx in range(2):
        drawSquare(grace,10,"black")
    for cy in range(4):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for cz in range(3):
        drawSquare(grace,10,"light pink")
    for da in range(3):                 #end of row 21
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for db in range(4):                 #start of row 22
        drawSquare(grace,10,"yellow")
    for dc in range(2):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for dd in range(6):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for de in range(4):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for df in range(3):
        drawSquare(grace,10,"light pink")
    for dg in range(3):                 #end of row 22
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for dh in range(3):                 #start of row 23
        drawSquare(grace,10,"yellow")
    for di in range(2):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for dj in range(8):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"yellow")
    for dk in range(2):
        drawSquare(grace,10,"black")
    for dl in range(5):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for dm in range(2):
        drawSquare(grace,10,"light pink")
    for dn in range(3):                 #end of row 23
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for do in range(3):                 #start of row 24
        drawSquare(grace,10,"yellow")
    for dp in range(2):
        drawSquare(grace,10,"light pink")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for dq in range(17):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for dr in range(2):
        drawSquare(grace,10,"light pink")
    for ds in range(3):                 #end of row 24
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for dt in range(4):                 #start of row 25
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"blue")
    drawSquare(grace,10,"black")
    for du in range(19):
        drawSquare(grace,10,"yellow")
    drawSquare(grace,10,"black")
    drawSquare(grace,10,"blue")
    for dv in range(4):                 #end of row 25
        drawSquare(grace,10,"yellow")
    newRow(grace,10,31)
    for dw in range(31):
        drawSquare(grace,10,"yellow")   #end of art!!!
   
main()
