#七段数码管绘制+心脏V3.py
#优化为北京时间而非UTC时间
import turtle,time
from datetime import datetime, timedelta

def drawGap():      #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): #绘制单段数码管
    
    drawGap()
    
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(30)
    
    drawGap()

    turtle.right(90)
def drawDigit(digit):#根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date): #data为日期，格式为'%Y-%m=%d+'
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))

def drawTime(time):#time为时间，格式为'%H-%M=%S+'
    turtle.pencolor("purple")
    for i in time:
        if i == '-':
            turtle.write('时',font=("Arial",18,"normal"))
            turtle.pencolor("purple")
            turtle.fd(40)
        elif i == '=':
            turtle.write('分',font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.write('秒',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
        
#HeartDraw.py
def HeartDraw():

    turtle.setup(1440,900,200,200)
    turtle.pensize(16)
    turtle.color('red','red')

    # color('red','blue')
    # 颜色（‘画笔色’，‘填充色’）

    turtle.penup()
    turtle.seth(90)
    turtle.fd(300)
    turtle.pendown()
    turtle.seth(-90)

    turtle.seth(45)
    turtle.circle(-200,180)
    turtle.fd(400)
    turtle.right(90)
    turtle.fd(400)
    turtle.circle(-200,180)
def main():
    turtle.speed(5)
    HeartDraw()
    turtle.speed(0.1)
    turtle.left(45)
    turtle.right(90)
    turtle.up()
    turtle.fd(200)
    turtle.down()
    turtle.left(90)
    turtle.penup()
    turtle.fd(-270)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(-180)
    turtle.fd(500)
    turtle.seth(0)
    turtle.down()


    now_time = datetime.now()
    utc_time = now_time - timedelta(hours=8)              # UTC只是比北京时间提前了8个小时
    utc_time = utc_time.strftime("%H-%M-%S+")
    now_time = now_time.strftime("%H-%M-%S+")
    drawTime(now_time)

    turtle.hideturtle()
    turtle.done()

main()
