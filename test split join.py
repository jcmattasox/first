# learning split / join
#  JC Matteson



message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):   # Define function
           
    lines = message.split('\n')   #Split the message by newline (\n) 
    print ('|'.join(lines))       #join it together on '|' print output
    
split_in_columns(message) # call function

