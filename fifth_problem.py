while(True):
    check = False
       for j in range(11, 21):
          if n % j == 0:
             check = True
          else:
             check = False
             break
    if check == True:
       print(n)
       break
    else:
       n += 1
