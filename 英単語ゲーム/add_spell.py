import tkinter as tk
import db
from tkinter import messagebox

class Add(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=400, height=400)
    self.master = master
    self.pack()

    master.geometry('600x400')
    master.title('単語帳')

    self.create_widgets()


  def create_widgets(self):
    self.label_eng = tk.Label(self, text='英語')
    self.label_eng.place(x=130, y=50)
    
    self.label_jp = tk.Label(self, text='日本語')
    self.label_jp.place(x=120, y=100)
    
    self.entry_spell = tk.Entry(self)
    self.entry_spell.place(x=170, y=50)
    
    self.entry_mean = tk.Entry(self)
    self.entry_mean.place(x=170, y=100)
    
    self.button_add = tk.Button(self, text='追加', command=self.add_event)
    self.button_add.place(x=170, y=150)
    
    self.button_return = tk.Button(self, text='戻る', command=self.return_main)
    self.button_return.place(x=230, y=150)
    
  def add_event(self):
    spell = self.entry_spell.get()
    mean = self.entry_mean.get()
    
    db.insert_spell(spell, mean)
    
    messagebox.showinfo('完了', '登録が完了しました。')
    
    self.entry_spell.delete(0, tk.END)
    self.entry_mean.delete(0, tk.END)
    
  def return_main(self):
    import main
    self.destroy()
    main.Application(self.master)

    

if __name__ == '__main__':
  root = tk.Tk()
  app = Add(master=root)
  app.mainloop()