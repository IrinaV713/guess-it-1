import numpy as np

array = []
movaver =[]
while(1):
    try:
        inp = input()
    except EOFError:
        break

    elem = int(inp)
    if len(array) > 0:
        if abs(elem/movaver[-1]) > 1000:
            array.append(movaver[-1])
        else:
            array.append(elem)
    else:
        array.append(elem)

    if len(array) <= 5:
        movaver.append(int(np.mean(array)))
        print(str(np.mean(array)-np.std(array)) + " " + str(np.mean(array)+np.std(array)))
    else:
        myslice = array[-5:]
        av = int(np.mean(myslice))
        movaver.append(av)
        std = int(np.std(myslice))
        print(str(av-std) + " " + str(av+std))
