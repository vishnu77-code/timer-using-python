import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

#
# --------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

            global reps
            reps+=1
            if reps %8==0:
                count_down(60 * LONG_BREAK_MIN)

            elif  reps%2==0 and reps%8!=0:
                count_down(60 * SHORT_BREAK_MIN)


            else:
                count_down(60*WORK_MIN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



def count_down(count):
        cont=math.floor(count/60)
        contsec=count%60
        if contsec==0 :
            contsec="00"
        if int(contsec) < 10 and int(contsec)!=0:
            contsec=f"0{contsec}"

        canvas.itemconfig(timer_text,text=f'{cont}:{contsec}')
        if count>0:
            windows.after(1000,count_down,count-1)

        else:
            start_timer()
            marks=""
            rag=math.floor(reps/2)
            for _ in range(rag):
                marks+="✓"
                label1.config(text=marks, fg=GREEN)
                label1.grid(row=3, column=2)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
windows=Tk()
windows.config(bg=YELLOW,padx=20,pady=20)
canvas=Canvas(highlightthickness=0)
label=Label()
label.config(text="Timer",fg=GREEN,font=(FONT_NAME,"34","bold"),bg=YELLOW)
label.grid(row=1,column=2)
canvas.config(height=300,width=300,bg=YELLOW)
button=Button()

button.config(text="start",font=(FONT_NAME,"10","bold"),command=count_down)
button1=Button()
button1.config(text="Reset",font=(FONT_NAME,"10","bold"))
button1.grid(row=3,column=3)
button.grid(row=3,column=1)
image=PhotoImage(file="tomato.png")
canvas.create_image(150,150,image=image)


label1=Label()

# # label1.config(text=marks,fg=GREEN)
# label1.grid(row=3,column=2)
timer_text=canvas.create_text(150,170,text="00:00",fill="white",font=(FONT_NAME,"34","bold"))
canvas.grid(row=2,column=2)

button=Button()

button.config(text="start",font=(FONT_NAME,"10","bold"),command=start_timer)
button1=Button()
button1.config(text="Reset",font=(FONT_NAME,"10","bold"))
button1.grid(row=3,column=3)
button.grid(row=3,column=1)


windows.mainloop()
