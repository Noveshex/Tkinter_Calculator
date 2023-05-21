from tkinter import *

app = Tk()
app.title("calculator")

textLabel1 = Label(app, text="Number 1")
textLabel1.grid(row=0, column=0)

textLabel2 = Label(app, text="Number 2")
textLabel2.grid(row=1, column=0)

text = Entry(app, width=20)
text.grid(row=0, column=1)

text1 = Entry(app, width=20)
text1.grid(row=1, column=1)

simpleText = StringVar()
result_label = Label(app, textvariable=simpleText)
result_label.grid(row=2, column=1)


def calculate_result():
	res = int(text.get().strip()) + int(text1.get().strip())
	simpleText.set(str(res))


textLabel3 = Label(app, text="+")
textLabel3.grid(row=0, column=2)


btn1 = Button(app,text="=", width=10, command=calculate_result)
btn1.grid(row=1, column=2)

app.mainloop()