
#引入GUI工具包
import tkinter
#引入隨機函數
import random
#引入定時器
import time

#定義木板類
class Paddle:
    #初始化
    def __init__(self,canvas,color):
        #導入我的大畫布
        self.canvas=canvas
        #先使用CANVAS模組建立一個長方形塊(要放到大畫布裡面所以也要用CANVAS模組先建立才不會有不相容的情況)
        self.id=self.canvas.create_rectangle(0,0,150,10,fill=color)
        #把方形塊擺到大畫布的裡面
        self.canvas.move(self.id,150,380)
        #給予遊戲的執行與停止定義一個狀態變數
        self.started=False
        #給予長方形板一個初始X軸位置
        self.x=0
        #讀取大畫布的寬存入self.canvas_width變數當中
        self.canvas_width=self.canvas.winfo_width()
        #針對在大畫布中發生的事件去執行相對應的FUCTION
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.canvas.bind_all("<KeyPress-Down>", self.game_start)
        self.canvas.bind_all("<KeyPress-Up>", self.game_stop)

    #evt是向系統註冊的事件
    #長方形板-左轉
    def turn_left(self,evt): 
        self.x=-4
    #長方形板-右轉
    def turn_right(self,evt): 
        self.x=4
    #遊戲狀態變數設定-開始
    def game_start(self,evt): 
        self.started=True
    #遊戲狀態變數設定-結束
    def game_stop(self,evt):
        self.started = False
    #畫出木板(PASS)
    def draw(self):  
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=500:
            self.x=0

class Ball():
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.hitbottom = False
            
        #把球擺到大畫布的裡面
        self.canvas.move(self.id,245,100)

        
        self.canvas_height=self.canvas.winfo_height()
        self.speed = 5
        starts=[-3,-2,-1,1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y = self.speed
        
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        
        pos=self.canvas.coords(self.id)
        #判斷板子與球
        if self.hit_paddle(pos)==True:
            self.y=-self.speed
        if pos[0]<=0:
            self.x=self.speed
        if pos[1]<=0:
            self.y=self.speed
        if pos[2]>=500:
            self.x=-self.speed
        if pos[3]>=self.canvas_height:
            self.hitbottom = True
            self.y=-self.speed
            
        

#創建一個界面和配置界面的一些基本屬性
tk = tkinter.Tk()
tk.title("Game")
#表示不能被拉伸
tk.resizable(0, 0) 
#通知管理器調整布局大小(視窗置頂)
tk.wm_attributes("-topmost", 1)

#創建畫布(GUI介面畫布)
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
#畫布架設
canvas.pack()


game_startsigal_text=canvas.create_text(430,10,text="DOWN:START",font=("Times",10),state="hidden")
game_endsigal_text=canvas.create_text(430,30,text="UP:END",font=("Times",10),state="hidden")
game_leftsigal_text=canvas.create_text(430,50,text="LEFT:LEFT",font=("Times",10),state="hidden")
game_rightsigal_text=canvas.create_text(430,70,text="RIGHT:RIGHT",font=("Times",10),state="hidden")

game_over_text=canvas.create_text(250,200,text="GAME OVER",font=("Times",30),state="hidden")
game_start_text=canvas.create_text(430,110,text="GAME START",font=("Times",10),state="hidden")
game_score_text=canvas.create_text(430,90,text="SCORE:",font=("Times",10),state="hidden")


#更新界面
tk.update() 


paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,"red")

while 1:
    if ball.hitbottom == False and paddle.started == True:
        paddle.draw()
        ball.draw()
        canvas.itemconfig(game_start_text, state="normal")
    elif ball.hitbottom == True:
        canvas.itemconfig(game_over_text, state="normal")
        canvas.itemconfig(game_start_text, state="hidden")
        break
    tk.update()
    time.sleep(0.01)
