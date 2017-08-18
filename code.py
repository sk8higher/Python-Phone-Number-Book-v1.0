choose = int(input('What do you want? \n1 - Write data \n2 - Read data \n3 - Clear ALL data '))
if choose == 1:
    a = open('file.txt', 'at')
    a.write(input())
    a.write('\n')
    a.close()
elif choose == 2:
    a = open('file.txt', 'r')
    print(a.read())
    a.close()
elif choose == 3:
    clr = open('file.txt', 'w').close()