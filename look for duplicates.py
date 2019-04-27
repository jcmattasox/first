# test list and finding duplicates
# JC Matteson

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):    # define function
    new_names =[]   # start new list
    for n in NAMES:  #Set terms of loop
        if n not in new_names:  # check for duplicates
            n=n.title()         # Capitalize the names
            new_names.append(n)  # Add to new list
    #titlecase (new_names)
    print (NAMES)
    print (new_names)
dedup_and_title_case_names(NAMES)  #Call the function
