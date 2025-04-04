import tkinter as tk
import random

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=400, height=400)
    self.pack()

    master.geometry('400x400')
    master.title('計算ゲーム')
    self.q_index = 1
    self.answer = 0
    self.ok = 0
    self.no = 0
    

    self.create_widgets()
    self.master.bind('<KeyRelease>', self.click_event)


  def create_widgets(self):
    if self.q_index < 11:        #10問出題
      num_a, num_b, random_symbol = self.random_num()
      
      self.label_question = tk.Label(self, text=f'第{self.q_index}問', font=('', 20))
      self.label_question.place(x=30, y=20)
      
      self.label_a = tk.Label(self, text=num_a, font=('', 20))
      self.label_a.place(x=140, y=100)
      
      self.label_b = tk.Label(self, text=num_b, font=('', 20))
      self.label_b.place(x=230, y=100)
      
      self.label_symbol = tk.Label(self, text=random_symbol, font=('', 20))
      self.label_symbol.place(x=180, y=100)
      
      self.entry = tk.Entry(self)
      self.entry.place(x=135, y=170)
      self.entry.focus()
      
      self.label_ok_no = tk.Label(self, text='', font=('', 17))
      self.label_ok_no.place(x=170, y=250)
      
      if random_symbol == '+':
        self.answer = num_a + num_b
      elif random_symbol == '-':
        self.answer = num_a - num_b
      elif random_symbol == '×':
        self.answer = num_a * num_b  
      else:
        self.answer = num_a // num_b  
    else:
      self.label_question.configure(text='終了です。')
      
      self.label_ok = tk.Label(self, text=f'正解数 : {self.ok} 問', font=('', 20))
      self.label_no = tk.Label(self, text=f'不正解数 : {self.no} 問', font=('', 20))    
      self.label_ok.place(x=120, y=100)
      self.label_no.place(x=120, y=150)   
      
      self.button_quit = tk.Button(self, text='終了', command=lambda: self.quit())
      self.button_quit.place(x=180, y=210)
         
  
  def random_num(self):
    self.num_b = random.randint(1, 10)
    self.num_a = random.randint(self.num_b, 10)

    symbol = ['+', '-', '×', '÷']
    self.random_symbol = random.choice(symbol)
    
    return self.num_a, self.num_b, self.random_symbol


  # 計算結果をだして入力欄の数字と比較
  def click_event(self, event):
    if event.keysym == 'Return':
      input_num = self.entry.get()   #入力された数字
      
      if int(input_num) == self.answer:
        self.label_ok_no.configure(text='正解', fg='red')
        self.ok += 1
     
      elif int(input_num) != self.answer:
        self.label_ok_no.configure(text='不正解', fg='blue')
        self.no += 1
        
      self.q_index += 1
      self.answer = 0   #次の問題のために０を代入
      self.label_a.configure(text='')
      self.label_b.configure(text='')
      self.label_symbol.configure(text='')
      self.after(1000, lambda: self.label_ok_no.configure(text=''))
      self.entry.destroy()
      self.after(1300, self.create_widgets)
    

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()