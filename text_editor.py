from tkinter import *

class Text_editor(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.winfo_toplevel().title('My editor')
    self.pack()
    self.main_menu()
    self.add_text_area()

  def main_menu(self):
    self.left = Button(text='Left', width=10, height=3)
    self.right = Button(text='Right', width=10, height=3)
    self.left.pack()
    self.right.pack()

  def add_text_area(self):
    self.text = Text(width=50, height=10, bg="white", fg='black', wrap=WORD)
    self.text.pack()

# if __name__ == "__main__":
root = Tk()
Text_editor(root)
root.geometry('500x500')
root.mainloop()
