def Coding(cleanString: str) -> str:
    amountLetter = 0
    lastLetter = ''
    resultString = ''
    for i, nowLetter in enumerate(cleanString):
        if nowLetter != lastLetter and lastLetter != '':
            resultString += f'{amountLetter}{lastLetter}'
            amountLetter = 1
        else:
            amountLetter += 1

        lastLetter = nowLetter

        if i == len(cleanString) - 1:
            resultString += f'{amountLetter}{lastLetter}'
    return resultString


def Decoding(encodedString: str) -> str:
    amountString = ''
    resultString = ''
    for nowLetter in encodedString:
        if nowLetter.isnumeric():
            amountString += nowLetter
        else:
            resultString += nowLetter * int(amountString)
            amountString = ''
    return resultString


file = open('./text.txt', 'r')
listLine = list(Coding(line.strip()) for line in file)
file.close()

file = open('./encodedText.txt', 'w')
finishedList = list(map(Decoding,listLine))
file.write('\n'.join(finishedList))
file.close()