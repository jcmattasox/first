# test list outputs
# JC Matteson



names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():  #define function

    x=0 #declair variable
    for i in names: #set loop condition

        print ('{}. {:11}    {}'.format( x+1 , names[x], countries[x])) # test format
    
        x=x+1 # change variable

enumerate_names_countries()   # call function
