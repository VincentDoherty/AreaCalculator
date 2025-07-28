import math

print('==================\nArea Calculator 📐\n==================')
shape = int(input('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n Which shape: '))
area = 0

if shape == 1:
  base = int(input('\nBase: '))
  height = int(input('Height: '))
  area = (height * base) / 2
elif shape == 2:
  lenght = int(input('\nLenght: '))
  width = int(input('Width: '))
  area = lenght * width
elif shape == 3:
  side = int(input('\nSide: '))
  area = side ** 2
elif shape == 4:
  radius = int(input('\nRadius: '))
  area = math.pi * radius ** 2
else:
 print('Bye :)')


print(f"\nThe area is {area}")

