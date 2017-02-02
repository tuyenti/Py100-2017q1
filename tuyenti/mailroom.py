def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def mailroom():
    dornor = []
    while True:
        print('*' * 30)
        print('*Type 1 to Send a Thank you')
        print('*Type 2 to Create a Report')
        selection = raw_input()
        if(selection == 'list'):
            for i in range(len(dornor)):
                print(dornor[i])
        elif(selection == 'q'):
            break
        elif(selection == '1'):
            userInput = raw_input("What is your Full Name: ")
            if(userInput == 'list'):
                for i in range(len(dornor)):
                    print(dornor[i])
                break
            if(userInput == 'q'):
                break
            print('Hello', userInput)
            newCus = True
            for name in dornor:
                if name[0] == userInput:
                    newCus = False
                    amount = raw_input('Welcome back... how much would you like to donate: ')
                    while(isInteger(amount) == False):
                        amount = raw_input('Please re-enter amount in number: ')
                    name[1].append(amount) #keep track of history of donate
                    name[2] = name[2] + int(amount)
                    name[3] = name[2]/len(name[1])
                    break # break the for
            # if this is new user, add new user
            if newCus is True:
                newAmount = raw_input('Welcome, how much would you like to donate: ')
                while (isInteger(newAmount) == False):
                    newAmount = raw_input('Please re-enter amount in number: ')
                total = int(newAmount)
                average = int(newAmount)
                dornor.append([userInput, [newAmount], total, average])
        elif(selection == '2'):
            print('*' * 15 + 'REPORT' + '*' * 15)
            print('*' + 'Name***' + ' Donate Record****' + ' Total***' + ' Average')
            for j in range(len(dornor)):
                print(dornor[j])

mailroom()
