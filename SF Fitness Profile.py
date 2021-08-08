from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Fitness Profile")
root.resizable(width=False,height=False)

# ==================== Variables ====================

userGender = StringVar()
userAge = StringVar()
userHeight = StringVar()
userWeight = StringVar()

# ==================== Functions ====================


def frame_maker(side,root=root):
    frame = Frame(root,borderwidth=6)
    frame.pack(side=side,fill=BOTH,pady=5)
    return frame


def label_maker(root,text,side):
    label = Label(root,text=text)
    label.pack(side=side)
    return label


def entry_maker(root,side,variable):
    entry = Entry(root,width=5,textvariable=variable)
    entry.pack(side=side,padx=5)
    return entry

def submit():
    try:
        BMI = float(userWeight.get())/(((float(userHeight.get()))/100)**2)
        if userGender.get() == "male":
            BMR = 66.47+13.7*float(userWeight.get())+5*float(userHeight.get())-6.8*float(userAge.get())
        elif userGender.get() == "female":
            BMR = 655.1+9.6*float(userWeight.get())+1.8*float(userHeight.get())-4.7*float(userAge.get())
        messagebox.showinfo("Results",f"BMI = {round(BMI,1)}\nBMR = {round(BMR)} Calories")
    except:
        messagebox.showerror("ERROR","Check your inputs and try again")


# ==================== Overview ====================

genderFrame = frame_maker(TOP)
genderLabel = label_maker(genderFrame,"Select your gender:",TOP)
maleButton = Radiobutton(genderFrame,text="Male",variable=userGender,value="male")
maleButton.pack(side=LEFT,padx=30,pady=5)
femaleButton = Radiobutton(genderFrame,text="Female",variable=userGender,value="female")
femaleButton.pack(side=LEFT,padx=30,pady=5)

ageFrame = frame_maker(TOP)
ageLabel = label_maker(ageFrame,"Enter your age:",LEFT)
ageEntry = entry_maker(ageFrame,LEFT,userAge)

weightFrame = frame_maker(TOP)
weightLabel = label_maker(weightFrame,"Enter your weight:",LEFT)
weightEntry = entry_maker(weightFrame,LEFT,userWeight)
kgLabel = label_maker(weightFrame,"Kgs",LEFT)

heightFrame = frame_maker(TOP)
heightLabel = label_maker(heightFrame,"Enter your height:",LEFT)
heightEntry = entry_maker(heightFrame,LEFT,userHeight)
cmLabel = label_maker(heightFrame,"Cms",LEFT)

submitFrame = frame_maker(TOP)
submitButton = Button(submitFrame,text="SUBMIT",command=submit)
submitButton.pack(fill=BOTH)


root.mainloop()
