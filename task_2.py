import tkinter as tk
import random as rn
from tkinter import messagebox

listFilledFilds = []


def EndGame():
    messagebox.showinfo(
        'Игра окончена', f'Победил {playerName[nowPlayerMove]}')


def EndGameDraw():
    messagebox.showinfo(
        'Игра окончена', 'Ничья')


def handle_click(event):
    row = event.widget.location[0]
    column = event.widget.location[1]
    globalData = list(
        filter(lambda x: x['row'] == row and x['column'] == column, listFilledFilds))
    data = globalData[0]

    Move(data)

    iiMove()


def Move(data):
    if endGame != True:
        if data['type'] != None:
            return

        data['btn']['text'] = figures[globals()['nowFigure']]
        data['type'] = globals()['nowFigure']

        if CheckEndGame(globals()['nowFigure']):
            globals()['endGame'] = True
            return

        globals()['nowPlayerMove'] = 1 if globals()[
            'nowPlayerMove'] == 2 else 2
        globals()['nowFigure'] = 1 if globals()['nowFigure'] == 2 else 2


def CheckEndGame(nowFigure) -> bool:
    emptyFields = len(
        list(filter(lambda x: x['type'] == None, listFilledFilds)))
    if emptyFields == 0:
        EndGameDraw()
        return True

    for i in range(0, 3):
        # горизонт
        countGor = len(
            list(filter(lambda x: x['row'] == i and x['type'] == nowFigure, listFilledFilds)))
        # вертикаль
        countVert = len(
            list(filter(lambda x: x['column'] == i and x['type'] == nowFigure, listFilledFilds)))
        if countGor == 3 or countVert == 3:
            EndGame()
            return True
    # диагональ
    countDiag = len(list(filter(
        lambda x: x['column'] == x['row'] and x['type'] == nowFigure, listFilledFilds)))
    countDiag2 = len(list(filter(
        lambda x: x['column'] == 2 - x['row'] and x['type'] == nowFigure, listFilledFilds)))

    if countDiag == 3 or countDiag2 == 3:
        EndGame()
        return True
    return False


def firstMove() -> int:
    return rn.randint(1, 2)


def lastFieldFigure(array):
    empty = list(filter(lambda x: x['type'] == None, array))
    if len(empty) == 1 and len(array) == 3:
        return empty[0]
    else:
        return False


def iiMove():
    if endGame != True:
        myList = list(filter(lambda x: x['type'] == None, listFilledFilds))
        data = myList[rn.randint(0, len(myList)-1)]

        for i in range(0, 3):
            # горизонт
            listFields = list(filter(lambda x: x['row'] == i and (
                x['type'] == globals()['nowFigure'] or x['type'] == None), listFilledFilds))
        Move(data)


def createWindow(window):
    for i in range(0, 3):
        for j in range(0, 3):
            frame = tk.Frame(master=window)
            frame.grid(column=j, row=i)
            btn = tk.Button(master=frame, width=10, height=5,
                            text="", bg="RoyalBlue")
            btn.location = (i, j)
            btn.bind("<Button-1>", handle_click)
            btn.pack()
            globals()['listFilledFilds'].append({
                'row': i,
                'column': j,
                'location': (i, j),
                'type': None,
                'btn': btn
            })


# 1 - пользователь
# 2 - компьютер
playerName = {
    1: 'пользователь',
    2: 'компьютер'
}

# 1 - +
# 2 - 0
figures = {1: '+', 2: '0'}
nowFigure = 1

endGame = False

nowPlayerMove = firstMove()

window = tk.Tk()
createWindow(window)

if nowPlayerMove == 2:
    iiMove()

window.mainloop()
