print('welcome to Central Bank of Kenya')
restart = 'p'
chances = 3
while chances >= 0:
    pin = int(input('please enter your correct digit pin'))
    if pin == 1258:
        print('you have entered your pin correctly, please continue.')
        while restart not in ('n', 'NO', 'N', 'no'):
            print('please press 1 to check your balance')
            print('please press 2 to make a withdrawal')
            print('please press 3 to pay in ')
            print('please press 4 to return your card ')
            option = int(input('what would you like to choose '))
            if option == 1:
                print('your balance is Ksh ,45000')
            elif option == 2:
                withdrawal = int(input('how much do you want to withdraw'))
            elif option == 3:
                payment = int(input('how much do you want to pay in '))
            elif option == 5:
                print('you have entered an invalid option, please try again')
            else:
                print('Thank you for being honest')




