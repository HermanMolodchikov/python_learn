guess = 0
number = 2
cnt = 0


while True:
    guess = int(input("Input number from 1 to 100: "))
    cnt += 1
    if guess == number:
        print(f'congratulations you guessed it {cnt} approaches . this {number}')
        break
    elif guess < number:
        print(f'sorry. My number more your')
    else:
        print(f'sorry. My number less your')
