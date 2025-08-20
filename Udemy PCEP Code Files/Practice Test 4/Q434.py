"""
setzt startpunkt Index 2
gibt 3 zeichenketten aus in Großbuchsraben
"""
def get_names():
    names = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']
    return names[2:]    # setzt startpunkt Index 2


def update_names(names):
    res = []
    for name in names:
        res.append(name[:3].upper())    # gibt 3 zeichenketten aus in Großbuchsraben
    return res


print(update_names(get_names()))  # ['MAR', 'JAN', 'STE']
