from tkinter import *

class Text_editor(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.winfo_toplevel().title('My editor')
    self.grid()
    # self.main_menu()
    self.add_text_area()

  def main_menu(self):
    self.left = Button(text='Left', width=10, height=3)
    self.right = Button(text='Right', width=10, height=3)
    self.left.grid(row=0, column=0, pady=20, sticky='N')
    self.right.grid(row=0, column=1, pady=20, sticky='N')

  def add_text_area(self):

    def align_center(text, align):
      text.tag_configure('text-align', justify=align)
      text.tag_add('text-align', 1.0, "end")

    def font_settings(text, align):
      try:
        text.tag_configure("bt", font=("Georgia", "12", "bold"))
        text.tag_add("bt", "sel.first", "sel.last")
      except:
        pass
    
    self.text = Text(width=50, height=10, bg="white", fg='black', wrap=WORD)
    self.text.grid(row=1, column=0, columnspan=15, sticky='N')

    self.left = Button(text='Left', width=10, height=3, command= lambda: align_center(self.text, 'left'))
    self.right = Button(text='Right', width=10, height=3, command= lambda: align_center(self.text, 'right'))
    self.center = Button(text='Center', width=10, height=3, command= lambda: align_center(self.text, 'center'))
    self.bold = Button(text='B', width=10, height=3, command= lambda: font_settings(self.text, 'center'))
    self.left.grid(row=0, column=0, pady=20, sticky='N')
    self.right.grid(row=0, column=2, pady=20, sticky='N')
    self.center.grid(row=0, column=1, pady=20, sticky='N')
    self.bold.grid(row=0, column=3, pady=20, sticky='N')


if __name__ == "__main__":
  root = Tk()
  Text_editor(root)
  root.geometry('500x500')
  root.mainloop()

