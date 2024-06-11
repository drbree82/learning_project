import tkinter

formMain = tkinter.Tk(className="Test")

formLabel = tkinter.Label(formMain, text="Hello there")
formLabel.pack()

formButton = tkinter.Button(formMain, text="Stop", width=25, command=formMain.destroy)
formButton.pack()

formMain.title("Counting Seconds")

formMain.mainloop()