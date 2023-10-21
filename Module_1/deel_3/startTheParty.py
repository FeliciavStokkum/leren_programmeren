gastheer = True
gasten = True
drank = False
chips = True

if chips and drank or gasten and chips and drank or gastheer and drank or gastheer and gasten and chips and drank:
    print('Start the Party')
else:
    print('No Party')