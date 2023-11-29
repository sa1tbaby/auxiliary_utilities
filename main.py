
with open('file.txt', 'w+') as file:
    file.read()

try:
    sasd = open('file.txt', 'w+')
    sasd.read()
finally:
    sasd.close()


