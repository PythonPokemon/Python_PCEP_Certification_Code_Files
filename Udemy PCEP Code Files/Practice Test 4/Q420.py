"""
entweder eine typumwandlung oder eine ganzzahl erforderlich, es sei den es ist mit 'not' so gewohlt!
"""


# room = input('Enter the room number: ')
room = '101'  
rooms = {101: 'Gathering Place', 102: 'Meeting Room'}
if not room in rooms:
    # if room not in rooms:
    print('The room does not exist.')
else:
    print('The room name is: ' + rooms[room])

d = {'101': "String", 101: "Integer"}
