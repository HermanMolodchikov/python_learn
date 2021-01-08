import random
from tkinter import *


def clicked():
    lbl.configure(text="Я же просил...")


window = Tk()
window.title("Титочки")
window.geometry('400x400')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!")
btn.grid(column=1, row=0)
window.mainloop()

number = random.randint(1, 100)
guess = 0
cnt = 0


while True:
    guess = int(input("Input number from 1 to 100: "))
    cnt += 1
    if guess == number:
        print(f'congratulations you guessed it {cnt} approaches . this {number}')
        print('''
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡠⠢⠏⣉⣉⠣⢦⡀⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣐⢪⠅⣱⣟⢛⢧⠄⣷⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣬⣀⣢⣕⡽⢯⣩⣳⣷⠧⡆⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⡭⡾⣆⢿⡙⢟⢻⣿⡿⡹⣶⠅⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣔⠄⡗⢫⠘⠷⠾⠿⠟⠙⣡⢢⢖⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⢫⠺⠁⡹⢸⣿⣿⣿⡟⠲⣦⣌⢄⡇⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⢀⡈⢛⠨⠥⡄⣿⣿⣿⣧⢯⡻⡇⠨⣁⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⢠⡤⢠⣶⣿⣿⣿⣿⣿⣿⣿⣷⢗⠵⡐⡣⡄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠸⢡⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⡄⢶⡇⡇⠄
            ⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⠟⢸⣿⣿⣿⡟⡻⣿⠘⠧⡇⠄
            ⠄⠄⠄⠄⠄⠄⠄⢳⣿⣿⣿⡿⣫⣾⣜⢿⣿⣿⣷⣶⡿⢀⠗⡇⠄
            ⠄⠄⠄⠄⠄⠄⠄⣦⡝⣭⣵⣾⣿⣿⣿⣦⣍⣛⣛⣫⠡⣼⢾⣿⠄
            ⠄⠄⠄⠄⠄⠄⢰⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠨⣿⡟⠄
            ⠄⠄⠄⠄⠄⢀⣿⡿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢆⣶⣿⠇⠄
            ⠄⠄⠄⠄⠄⢸⣿⣷⠎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣷⣻⡆⠄
            ⠄⠄⠄⠄⢀⣿⣿⠏⢸⡟⢿⣿⣿⣸⣿⣿⣿⣿⢏⣾⣿⣿⣏⣷⠄
            ⠄⠄⠄⠄⣸⣿⠏⢀⣼⣿⣎⡻⢿⣿⣿⣿⠿⣣⣾⣿⣿⣿⣿⣽⠄
            ⠄⠄⠄⠄⣿⡿⣰⣿⣿⣿⣿⣿  ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
        ''')
        if input('Will we play again? "y|n":') == 'y':
            number = random.randint(1, 100)
            guess = 0
        else:
            print('Thank you for game')
            break
    elif guess < number:
        print(f'sorry. My number more your')
    else:
        print(f'sorry. My number less your')


