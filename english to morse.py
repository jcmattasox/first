# english to morse code translater
# JC Matteson

alpha = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..','M':'--','N':'-.', 'O':'---', 'P':'.--.', 'Q': '--.-', 'R':'.-.','S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}
phrase = input('What do you need to translate to morse code?')
phrase = phrase.upper() # convert input to uppercase 
phrase_a = list(phrase) # convert string to list
for i in phrase_a:      # loop through list
    first_a =str.strip(i) # remove white spaces
    first_a = list(first_a) # convert word to a list of letters
    for i in first_a:       # loop through list for conversion
        print(alpha[i], ' ', end='')  #replace letter with code  
    
