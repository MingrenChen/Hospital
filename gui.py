from tkinter import*
from init import*

lst = PatientsList()
lst.new("Mingren", "male", 15)
lst.new("Mingren", "male", 20)
lst.new("Harry", "male", 20)

root = Tk()
root.geometry("300x400+500+500")
menubar = Menu(root)
for item in ['文件', "编辑", "试图"]:
    menubar.add_command(label = item)
lb = Listbox(root)
for item in lst.PatientList:
    lb.insert(0,item)
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

lb.bind('<<ListboxSelect>>', onselect)
lb.pack(side = 'left')

root['menu'] = menubar
root.mainloop()
