from tkinter import *
root = Tk()


def callback():
    print 'click!'


button1 = Button(root, text='ONE', command=callback, bg='Red',
                 fg='Green')
button2 = Button(root, text='TWO', command=callback, bg='Red',
                 fg='Green')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print ('Screen width: ', w)
print ('Screen height: ', h)
root.geometry(str(w) + 'x' + str(h))

button1.place(x=50, y=50)
button2.place(x=100, y=100)
