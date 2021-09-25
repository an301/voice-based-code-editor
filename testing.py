from tkinter import *

def checkkey(event):
    value = event.widget.get()
    print(value)

    if value == '':
        data = l
    else:
        data = []
        for item in l:
            if value.lower() in item.lower():
                data.append(item)

    update(data)


def update(data):

    lb.delete(0, 'end')

    for item in data:
        lb.insert('end', item)



l = ('C', 'C++', 'Java',
     'Python', 'Perl',
     'PHP', 'ASP', 'JS')

root = Tk()
def click():
    for i in lb.curselection():
        print(lb.get(i))



e = Entry(root)
e.pack()
e.bind('<KeyRelease>', checkkey)

lb = Listbox(root)
lb.pack()
lb.bind("<Button-3>", leftClick)

update(l)

root.mainloop()
