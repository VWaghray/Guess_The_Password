from tkinter import *
import random 

root = Tk()

root.geometry("400x400")
root.title('3d arrays')

label = Label(root)
text = Entry(root)
label2 = Label(root)

Array_3d = [[[0,1,2,3,4,5,6,7,8,9], ['Apple', 'Bannana'], ['A','B','C','D','E','F','G','H','I','J','K']]]

print(Array_3d[0][1][1])

def password():
    r1 = random.randint(0, 8)
    r2 = random.randint(0, 1)
    r3 = random.randint(0, 10)
    
    letter1 = str(Array_3d[0][0][r1])
    letter2 = str(Array_3d[0][1][r2])
    letter3 = str(Array_3d[0][2][r3])
    
    word = text.get()
    
    label2["text"] = "Guessed Password: " + str(word)
    
    label["text"] = letter1 + "" + letter2 + "" + letter3
    





btn = Button(text = 'New Password', command=password, relief=GROOVE)
btn.place(relx=0.5, rely= 0.5, anchor=CENTER)
label.place(relx = 0.5, rely = 0.6, anchor=CENTER)
text.place(relx=0.5, rely=0.3, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.4, anchor=CENTER)

root.mainloop()
