from counter import*

answerAdd = ' '
answerReduce = ' '

cont.seeCont()

while True:
    answerAdd = str(input("Do you want to add? [Y/N] "))
    if answerAdd in 'Yy':
        cont.add()
        cont.seeCont()
    else:
        break

cont.seeCont()

while True:
    answerReduce = str(input("Do you want to reduce? [Y/N] "))
    if answerReduce in 'Yy':
        cont.reduce()
        cont.seeCont()
    else:
        break

cont.seeCont()



