from tkinter import *
import random
import time



# def display():
#     horizontal_line_vertx = 20
#     horizontal_space = horizontal_line_vertx-2
#     horizontal_line = print("-"*horizontal_line_vertx)
    
#     horizontal_line
#     vertical_line = [["|" for _ in range(2)] for _ in range(10)]
#     for row in vertical_line:
#         print((" "*horizontal_space).join(row))
#     horizontal_line

# snake = ['-','-','-','>']
# x=0
# while x<5:
#     time.sleep(1)
#     x+=1
#     snake.insert(0,'   ')
#     print(''.join(snake))

#graphics UI
count=0
def click():
    global count
    count+=1
    label.config(text=count)


window = Tk()
window.geometry("540x540")
window.title("Snake Game")
icon = PhotoImage(file='Snake_game/snake_icon.png')
window.iconphoto(True,icon)
window.config(background="")

label = Label(text=count, font=('Bahnschrift',40,'bold'),fg='red',width=9)
label.pack()
scale = Scale(window,
              )
scale.pack()
button = Button(window,
                text="Click Here",
                command=click,
                font=('Bahnschrift',40))
button.pack()

window.mainloop()


