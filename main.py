import sys
import random
import itertools

zeitweise=[]
ausgabe=[]

for h in range(len(sys.argv)):

    if h > 0:
        wort = list(sys.argv[h])

        for i in range(len(wort)):
            tmp = random.random()
            if tmp >= 0.5: 
                wort[i]=wort[i].lower()
            else:
                wort[i]=wort[i].upper()
        zeitweise.append(wort)
        zeitweise.append(" ")

ausgabe=list(itertools.chain.from_iterable(zeitweise))
print(''.join(ausgabe))
