print('-'*30)

customer_names = ['Rohit', 'Srilatha','Rohini' ,'Ram', 'Seeta']
customer_pins = ['1234','5678','4321','8765','0123']
customer_balance = [10000,20000,30000,40000,50000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0


while True:
    print('-'*30)
    print('---Welcome to the India Bank---')
    print('*'*30)
    print('1. Open a new account')
    print('2. Withdraw money')
    print('3. Deposit money')
    print('4. Check customers & Balance')
    print('5. Exit / Quit')
    print('*'*30)
    
    choicenumber = input('Select your choice number from the above menu: ')
    if choicenumber == '1':
        print('Choice number 1 is selected by  the costumer')    
        NOC = eval(input('Number of customers: '))

        i = i+ NOC
        if i > 5:
            print('\n')
            print('Customer registration exceed reached or Customer registration too low')
            i =  i - NOC
        else:
            while counter_1 <= 1:
                name = input('Input Fullname: ')
                customer_names.append(name)
                pin = str(input('Please input a pin of ur choice: '))
                customer_pins.append(pin)
                balance = 0
                deposition = eval(input('Please input a value to deposit to start an account: '))
                balance = balance + deposition
                customer_balance.append(balance)
                print('\nName = ',end = ' ')
                print(customer_names[counter_2])
                print('Pin = ',end = ' ')
                print(customer_pins[counter_2])
                print('Balance = ', end = ' ')
                print(customer_balance[counter_2], end = ' ')
                print('-/Rs')
                counter_1 = counter_1 + 1
                counter_2 = counter_2 = 1
                print('\nYour name is added to customers system')
                print('Your pin is added to customers system')
                print('Your balance is added to customers system')
                print('\n-----New Account Created Successfully!-----')
                print("\nNote! Please remember the 'Name' and 'Pin'")
                print('*'*30)
        Main_menu = input('Please press the enter key to go back to main menu to perform another function or exit...')
    elif choicenumber == '2' :
        j = 0
        print('Choice number 2 is selected by the customer')    
        while j < 1:
            k = -1
            name = input('Please enter the name: ')
            pin = input('Please enter the pin:')
            while k < len (customer_names) -1 :
                k = k + 1
                if name == customer_names[k]:
                    if pin == customer_pins[k]:
                        j = j + 1
                        print('Your Current Balance : ', end = ' ')
                        print(customer_balance[k], end = ' ')
                        print('-/Rs\n')
                        balance = (customer_balance[k])
                        withdrawal = eval(input('Input value to withdraw: '))
                        if withdrawal > balance:
                            deposition = eval (input('Please deposit a higher value because your balance mentioned above is not enough: '))
                            balance = balance + deposition
                            print('Your current balance: ', end = ' ')
                            print(balance, end =' ')
                            print('-/Rs\n')
                            balance = balance - withdrawal
                            print('-\n')
                            print('----Withdraw Successfull!----')     
                            customer_balance[k] = balance
                            print('Your New Balance: ', balance, end = ' ')
                            print('-/Rs\n\n')
                        else:
                            balance = balance - withdrawal
                            print('\n')
                            print('----Withdraw Successfull!----')
                            customer_balance[k] = balance
                            print('Your New Balance: ', balance, end = ' ')
                            print('-/Rs\n\n')
            if j < 1:
                print('Your name and pin does not match1\n')
                break
        Main_menu = input('Please press enter key to go back to main menu to perform another function or exit ...')
    elif choicenumber == '3':
        print('Choice number 3 is selected by the customer')
        n = 0
        while n < 1:
            k = -1
            name = input('Please enter the name: ')    
            pin = input('Please enter the pin: ')                  
            while k < len(customer_names) -1:
                k = k+1
                if name == customer_names[k]:                  
                    if pin == customer_pins[k]:
                        n = n+1
                        print('Your Current Balance: ', end = ' ')
                        print(customer_balance[k], end = ' ')
                        print('-/Rs')
                        balance = customer_balance[k]
                        deposition = eval(input('Enter the value you want to deposit: '))
                        balance = balance + deposition
                        customer_balance[k] = balance
                        print('\n')
                        print('----Deposited successfully!----')
                        print('Your New Balance: ', balance, end = ' ')
                        print('-/Rs\n\n')
            if n < 1 :
                print('Your name and pin does not match!\n')
                break
    elif choicenumber== '4':
        print('Choice number 4 is selected by the customer')
        k = 0
        print('Customers name list and balances mentioned below: ')
        print('\n')
        while k <= len(customer_names)-1:
            print('Customer = ', customer_names[k])
            print('Balance= ', customer_balance[k], end = ' ')
            print('-/Rs')
            print('\n')
            k = k + 1
        Main_menu = input('Please press enter key to go back to main menu to perform another function or exit ...')
    elif choicenumber == '5':
        print('Choice number 5 is selected by the customer')
        print('Thank you for using our banking system!')
        print('\n')
        print('*'*30)
        print('Visit Again')
        print('Namaskar')
        print('*'*30)
        break
    else:
        print('Invalid option is selected by the customer')
        print('PLease Try Again!')
        Main_menu = input('Please press enter key to go back to main menu to perform another function or exit ...')
        
                
        