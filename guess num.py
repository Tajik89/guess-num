import random as random

rand_num = random.randint(1, 100)
count = 0

print('\n<#-- Welcome to guess num _Game --#>\n')
print('\n----------')
user = int(input(f'Enter num from Try {count} : '))
count += 1
if user < rand_num :
    print('\nYour num is less')
elif user > rand_num :
    print('\nYour num is more')
else :
    print('\n<# ---End--- #>')
    print('<-- You are Win :~) -->')
    print(f'You are try {count} to found {rand_num} :)\n')
    exit(0)

while True :
    if user < rand_num :
        tring = 0
        for i in range(5) :
            print('\n----------')
            user = int(input(f'Enter num from Try {count} : '))
            count += 1

            if user == rand_num :
                print('\n<# ---End--- #>')
                print('<-- You are Win :~) -->')
                print(f'You are try {count} to found {rand_num} :)\n')
                exit(0)
            elif user < rand_num :
                tring += 1
                if tring == 5 :
                    print(f'\nYou are send {tring} <--successive--> less num :~(')
                    print(f'Please Send more num :)\n')
                else :
                    print('\nYour num is less')
                    continue
            else :
                print('\nYour num is more')
                break
    elif user > rand_num :
        tring = 0
        for j in range(5) :
            print('\n----------')
            user = int(input(f'Enter num from Try {count} : '))
            count += 1

            if user == rand_num :
                print('\n<# ---End--- #>')
                print('<-- You are Win :~) -->')
                print(f'You are try {count} to found {rand_num} :)\n')
                exit(0)
            elif user > rand_num :
                tring += 1
                if tring == 5 :
                    print(f'\nYou are send {tring} <--successive--> more num :~(')
                    print(f'Please Send less num :)\n')
                else :
                    print('\nYour num is more')
                    continue
            else :
                print('\nYour num is less')
                break
    else :
        print('\n<# ---End--- #>')
        print('<-- You are Win :~) -->')
        print(f'You are try {count} to found {rand_num} :)\n')
        exit(0)