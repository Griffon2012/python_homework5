import random


def GetCountForDelete(maxCount: int, nowTotalAmount: int) -> int:
    result = None
    step = maxCount + 1
    if nowTotalAmount < maxCount:
        result = nowTotalAmount
    elif nowTotalAmount % step:
        result = nowTotalAmount % step
    else:
        result = random.randint(1, maxCount)

    return result


def StartGameProcess() -> None:
    MINAMOUNT = 28
    MAXAMOUNT = 300
    totalAmount = None

    enabledBot = False
    enabledBotInput = None

    while (enabledBotInput != "y" and enabledBotInput != 'n'):
        enabledBotInput = input('Игра против бота? (y/n): ')

    enabledBot = True if enabledBotInput == 'y' else False

    while (totalAmount == None or totalAmount < MINAMOUNT + 1 or totalAmount > MAXAMOUNT):
        totalAmount = int(input(
            f'Укажите общее количество конфет (от {MINAMOUNT + 1} и нее более {MAXAMOUNT}): '))
        if totalAmount < MINAMOUNT + 1 or totalAmount > MAXAMOUNT:
            print(
                f'Не подходит под диапазон (от {MINAMOUNT + 1} и нее более {MAXAMOUNT})')

    firstMove = random.randint(1, 2)

    print(f'Первым ходит игрок №{firstMove}, всего {totalAmount} конфет')

    nowTotalAmount = totalAmount
    nowPlayer = firstMove
    countForDelete = None
    playerWinner = None

    while (nowTotalAmount > 0):

        if enabledBot and nowPlayer == 2:
            countForDelete = GetCountForDelete(MINAMOUNT, nowTotalAmount)
            print(
                f'Осталось {nowTotalAmount} конфет, игрок №{nowPlayer} забирает: {countForDelete}')
        else:
            countForDelete = int(input(
                f'Осталось {nowTotalAmount} конфет, игрок №{nowPlayer} забирает (не более {MINAMOUNT}): '))

        if countForDelete > nowTotalAmount:
            print('Нет столько конфет')
            continue

        if countForDelete > MINAMOUNT:
            print(f'Не более {MINAMOUNT}')
            continue

        nowTotalAmount -= countForDelete
        if nowTotalAmount == 0:
            playerWinner = nowPlayer
            break

        nowPlayer = nowPlayer + 1 if nowPlayer == 1 else nowPlayer - 1

    print(f'Победил игрок №{playerWinner}')


StartGameProcess()
