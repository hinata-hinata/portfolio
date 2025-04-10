import tkinter as tk
import add_spell
import game_start

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=400, height=400)
    self.master = master
    self.pack()

    master.geometry('600x400')
    master.title('単語帳')

    self.create_widgets()


  def create_widgets(self):
    self.button_start = tk.Button(self, text='スタート', font=('', 20), command=self.start_event)
    self.button_start.place(x=150, y=90)

    self.button_add = tk.Button(self, text='単語の追加', font=('', 20), command=self.add_event)
    self.button_add.place(x=125, y=180)


  def add_event(self):
    self.destroy()
    add_spell.Add(self.master)
    
  def start_event(self):
    self.destroy()
    game_start.Start(self.master)
    

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()