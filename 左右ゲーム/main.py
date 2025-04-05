import tkinter as tk
from tkinter import messagebox
import random

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=400, height=400)
    self.pack()

    master.geometry('400x400')
    master.title('左右ゲーム')
    self.muki = ''
    self.iro = ''
    self.input_muki = ''
    self.q_count = 0
    self.correct_count = 0

    self.create_widgets()
    self.master.bind('<KeyRelease>', self.key_event)


  def create_widgets(self):
    self.label = tk.Label(self, text='')
    self.label.place(x=130, y=50)
    
    self.random_arrow()

    
    
    # 矢印の向きと色を決定
  def random_arrow(self):
    if self.q_count < 10:   #問題数
    
      right_or_left = random.randint(0,1)
      random_color = random.randint(0, 1)
      if right_or_left == 0:
        self.muki = 'migi' 
        self.label.configure(text='→', font=('', 100))
      else:
        self.muki = 'hidari' 
        self.label.configure(text='←', font=('', 100))
        
          
      if random_color == 0:
        self.iro = 'red'
        self.label.configure(fg='red')
      else:
        self.iro = 'blue'
        self.label.configure(fg='blue')
        
    else:
      self.label.configure(text='')  
      
      self.label_2 = tk.Label(self, text=f'正解数 : {self.correct_count} 問', font=('', 15))
      self.label_2.place(x=130, y=100)

        
        
  def key_event(self, event):
    if event.keysym == 'Right':
      self.input_muki = 'migi' 
    else:
      self.input_muki = 'hidari'
      
      
    if self.input_muki == 'migi':
      if self.iro == 'red':
        if self.muki == 'migi':
          print('ok')
          self.correct_count += 1
        else:
          print('no')
      elif self.iro == 'blue':
        if self.muki == 'migi':
          print('no')
        else:
          print('ok')
          self.correct_count += 1
          
    elif self.input_muki == 'hidari':
      if self.iro == 'red':
        if self.muki == 'migi':
          print('no')
        else:
          print('ok')
          self.correct_count += 1
          
      elif self.iro == 'blue':
        if self.muki == 'migi':
          print('ok')
          self.correct_count += 1
          
        else:
          print('no')
      
    self.q_count += 1  
    self.random_arrow()
  

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()