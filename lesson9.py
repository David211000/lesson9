my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
indeks=3
while indeks<len(my_list):
     number=my_list[indeks]
     indeks+=1
     if number<0:
        break
     elif indeks==0:
        continue
     print(number)
