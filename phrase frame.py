# frame phrase
# JC Matteson






phrase = (  )

def frame(phrase):
     x = 0
     y = 0
     frame_a = list(phrase.split())

     for i in frame_a:
          x = len(i)
          if x>y:
               y=x
          
     top = y
     
     for i in range(1,top+3):
          print('*', end='')
          
     print('')

     for i in frame_a:
          print('*', end='')
          line = i.center(top)
          print (line, end='')
          print('*')

     for i in range(1,top+3):
          print('*', end='')
     

     
                    

frame('Longer is beter than short')
