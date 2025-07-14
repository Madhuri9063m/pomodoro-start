from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
updated = 2
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 




# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#USE after()
def count_down(count):
    global reps
    global timer

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        display_count()
        work_sessions = reps // 2
        marks = "\n".join(["✔" for _ in range(work_sessions)])
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg = YELLOW)

#ADDING A TEXT CALLED timer
text_label = Label(text="Timer",font=(FONT_NAME,32,"bold"), fg=GREEN, bg=YELLOW)
text_label.grid(row=0,column=2)

#Place image using Canvas class
canvas = Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(150,150,image=tomato_image)
count_text = canvas.create_text(150,160,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=2)

def display_count():
    global reps

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        text_label.config(text = "Work Time", fg = GREEN)
        count_down(WORK_MIN*60)
        reps += 1
    elif reps == 1 or reps == 3 or reps == 5:
        text_label.config(text="Break Time", fg= PINK)
        count_down(SHORT_BREAK_MIN*60)
        reps += 1
    elif reps == 7:
        text_label.config(text="Long Break Time", fg= RED)
        count_down(LONG_BREAK_MIN*60)
        reps = 0

#CREATING start BUTTON
button = Button(text="start",width=5,height=1, font=("Arial",10,"normal"), command=display_count)
button.grid(row=2,column=1)

# def reset_timer():
#     global timer
#     window.after_cancel(timer)
#     canvas.itemconfig(count_text, "00:00")
#     text_label["text"] = "Timer"

def reset_timer():
    global timer, reps
    window.after_cancel(timer)  # Stop the countdown
    canvas.itemconfig(count_text, text="00:00")  # ⛔ You had a small typo here
    text_label.config(text="Timer", fg=GREEN)  # Reset the main label
    tick_label.config(text="")  # Clear checkmarks
    reps = 0  # Reset the repetition counter


#CREATING reset BUTTON
button = Button(text="reset",width=5,height=1, font=("Arial",10,"normal"), command=reset_timer)
button.grid(row=2,column=4)

#CREATING tick mark TO MARK 4 STAGES OF POMODORO
tick_label = Label(font=(FONT_NAME,20,"bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(row=2,column=2)







window.mainloop()