import tkinter as tk


class Start(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=400, height=400)
    self.master = master
    self.pack()

    master.geometry('600x400')
    master.title('単語帳')

    self.create_widgets()


  def create_widgets(self):
    self.ask_spell = tk.Label(self, text='mean', font=('', 25))
    self.ask_spell.place(x=150, y=50)
    
    self.entry_spell = tk.Entry(self)
    self.entry_spell.place(x=130, y=150)
    self.entry_spell.focus()


if __name__ == '__main__':
  root = tk.Tk()
  app = Start(master=root)
  app.mainloop()