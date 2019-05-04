# divisible numbers / prime numbers
# JC Matteson



def get_input(): # by using function this input can be called more then once
    return int(input('Please input a number\n'))


def divisables(): # body of the program can be run many times
    div_list = []
    num = get_input()
    number_range = list(range(1,num))

    for i in number_range:
        
        if num % i ==0:
             div_list.append(i)


    if len(div_list) <2:
        print(num,'is prime')
        start()

    else:
        print(div_list)
        start()

def start(): # main control for the program 
    
    ask =input ('would you like to test a number?')
    
    if ask =='y':    
        divisables()
        

    else:
        print('goodbye')



start()
                
