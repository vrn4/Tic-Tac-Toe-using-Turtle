import turtle,time

trtl = turtle.Turtle()
scr = turtle.Screen()
trtl.pensize(4)
scr.setup(width=0.9,height=0.9)
scr.title("Tic-Tac-Toe")

class game():
    
    def __init__(self,d,c):
        self.d = d
        self.c = c

    def start(self):
        if self.c == 9:
            trtl.clear()
            trtl.penup()
            trtl.goto(-200,100)
            trtl.pendown()
            trtl.write("It's a Draw",font = ('Courier',50,"italic"))
            trtl.penup()
            trtl.goto(-160,-150)
            trtl.pendown()
            trtl.write("Press r to restart",font=('Courier',20,'italic'))
            va.win_ip()
        else:
            if self.c % 2 == 0:
                va.ip()
            else:
                va.ip()

    def ip(self):
        turtle.listen()

        turtle.onkey(va.fill_1,"1")         
        turtle.onkey(va.fill_2,"2")
        turtle.onkey(va.fill_3,"3")
        turtle.onkey(va.fill_4,"4")
        turtle.onkey(va.fill_5,"5")
        turtle.onkey(va.fill_6,"6")
        turtle.onkey(va.fill_7,"7")
        turtle.onkey(va.fill_8,"8")
        turtle.onkey(va.fill_9,"9")

        turtle.mainloop()
                    
    def setup(self):
        #horizontal lines
        trtl.speed(0)        
        trtl.pu()
        trtl.goto(50,-150)
        trtl.pd()
        trtl.left(90)
        trtl.forward(300)
        trtl.pu()
        trtl.goto(-50,-150)
        trtl.pd()
        trtl.forward(300)
        #vertical lines
        trtl.pu()
        trtl.goto(-150,50)
        trtl.pd()
        trtl.right(90)
        trtl.forward(300)
        trtl.pu()
        trtl.goto(-150,-50)
        trtl.pd()
        trtl.fd(300)
        trtl.speed(6)

    def check(self,a):
        if self.d[1]==a and self.d[2]==a and self.d[3]==a:
            return True
        elif self.d[1]==a and self.d[4]==a and self.d[7]==a:
            return True
        elif self.d[1]==a and self.d[5]==a and self.d[9]==a:
            return True
        elif self.d[2]==a and self.d[5]==a and self.d[8]==a:
            return True
        elif self.d[3]==a and self.d[6]==a and self.d[9]==a:
            return True
        elif self.d[3]==a and self.d[5]==a and self.d[7]==a:
            return True
        elif self.d[4]==a and self.d[5]==a and self.d[6]==a:
            return True
        elif self.d[7]==a and self.d[8]==a and self.d[9]==a:
            return True

    def winner(self,win):
        trtl.clear()
        trtl.penup()
        trtl.goto(-200,100)
        trtl.pendown()
        trtl.write(f"{win} has won",font = ('Courier',50,"italic"))
        trtl.penup()
        trtl.goto(-160,-150)
        trtl.pendown()
        trtl.write("Press r to restart",font=('Courier',20,'italic'))
        trtl.penup()
        trtl.goto(-160,-180)
        trtl.pendown()
        va.win_ip()
    
    def win_ip(self):
        turtle.listen()

        turtle.onkey(va.restart,"r")

        turtle.mainloop()

    def restart(self):
        trtl.clear()
        self.c = 0
        self.d = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
        va.setup()
        va.start()

    def fill_1(self):
        trtl.penup()
        trtl.goto(-100,60)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[1] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[1] = "O"
            trtl.circle(40)
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()            

    def fill_2(self):
            trtl.penup()
            trtl.goto(0,60)
            trtl.pendown()
            if self.c % 2 == 0:
                self.d[2] = "X"
                trtl.circle(40,steps=4)
                if va.check("X"):
                    va.winner("X")
                else:
                    self.c += 1
                    va.start()
            else:
                self.d[2] = "O"
                trtl.circle(40)          
                if va.check("O"):
                    va.winner("O")
                else:
                    self.c += 1
                    va.start()  

    def fill_3(self):
        trtl.penup()
        trtl.goto(100,60)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[3] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[3] = "O"
            trtl.circle(40)   
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()         

    def fill_4(self):
        trtl.penup()
        trtl.goto(-100,-40)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[4] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[4] = "O"
            trtl.circle(40)            
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()

    def fill_5(self):
            trtl.penup()
            trtl.goto(0,-40)
            trtl.pendown()
            if self.c % 2 == 0:
                self.d[5] = "X"
                trtl.circle(40,steps=4)
                if va.check("X"):
                    va.winner("X")
                else:
                    self.c += 1
                    va.start()
            else:
                self.d[5] = "O"
                trtl.circle(40)            
                if va.check("O"):
                    va.winner("O")
                else:
                    self.c += 1
                    va.start()

    def fill_6(self):
        trtl.penup()
        trtl.goto(100,-40)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[6] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[6] = "O"
            trtl.circle(40)            
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()

    def fill_7(self):
        trtl.penup()
        trtl.goto(-100,-140)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[7] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[7] = "O"
            trtl.circle(40)            
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()

    def fill_8(self):
            trtl.penup()
            trtl.goto(0,-140)
            trtl.pendown()
            if self.c % 2 == 0:
                self.d[8] = "X"
                trtl.circle(40,steps=4)
                if va.check("X"):
                    va.winner("X")
                else:
                    self.c += 1
                    va.start()
            else:
                self.d[8] = "O"
                trtl.circle(40)            
                if va.check("O"):
                    va.winner("O")
                else:
                    self.c += 1
                    va.start()

    def fill_9(self):
        trtl.penup()
        trtl.goto(100,-140)
        trtl.pendown()
        if self.c % 2 == 0:
            self.d[9] = "X"
            trtl.circle(40,steps=4)
            if va.check("X"):
                va.winner("X")
            else:
                self.c += 1
                va.start()
        else:
            self.d[9] = "O"
            trtl.circle(40)            
            if va.check("O"):
                va.winner("O")
            else:
                self.c += 1
                va.start()

#----------------------------------------------------

def load():
    trtl.pensize(2)
    trtl.hideturtle()

    trtl.penup()
    trtl.goto(-230,100)
    trtl.pendown()
    trtl.write("Tic-Tac-Toe",font=('Courier',50,'italic'))
    trtl.penup()
    trtl.goto(-150,-130)
    trtl.pendown()
    trtl.speed(0)
    for i in range(2):
        trtl.forward(300)
        trtl.left(90)
        trtl.forward(20)
        trtl.left(90)

    time.sleep(1)

    trtl.speed(6)
    for i in range(6):
        trtl.begin_fill()
        for j in range(2):
            trtl.fd(50*(i+1))
            trtl.left(90)
            trtl.pu()
            trtl.forward(20)
            trtl.pd()
            trtl.left(90)
        trtl.end_fill()

    time.sleep(1)
    trtl.clear()

#----------------------------------------------------------

e = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
load()
trtl.pensize(3)
va = game(e,0)
va.setup()
va.start()
