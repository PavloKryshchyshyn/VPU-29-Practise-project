# from uuid import uuid4
# class Music():
#     def __init__(self, id, name, author, album, lenght):
#         self.id = int(id) #identification number
#         self.name = str(name)
#         self.author = str(author)
#         self.album = str(album)
#         self.lenght = float(lenght) #minutes

# base_id = int(0)
# random_id = int(uuid4())

# music = [
#     Music(random_id, "Romantic Devil", "Coldin", "Romantic Devil(From Sematic Error)", 3.07),
#     Music(random_id, "Gravity", "EXO", "LOVE SHOT", 3.54),
#     Music(random_id, "Rush Hour", "Monsta X", "NO LIMIT", 3.22),
#     Music(random_id, "Wish You Were Here", "SuperM","Super One", 3.12),
#     Music(random_id, "You Calling My Name", "GOT7", "Call My Name", 3.14),
#     Music(random_id, "You Problem", "Monsta X", "The Dreaming", 3.19),
#     Music(random_id, "One (Monster & Infinity)", "SuperM", "Super One",3.41),
#     Music(random_id, "Hair Cut - inst.", "Xdinary Heroes", "Overload",3.25),
#     Music(random_id, "Teenager", "Got7", "7 for 7", 3.09)
# ]

# print(music[0:9])


import glob
value1 = glob.glob("./FCKINGMUSIC/*.mp3")
value2 = glob.glob("./FCKINGMUSIC/*.m4a")
# for everyValueIn in value2:
#     value1.append(everyValueIn)
value = []
i = 0
def appen():
    if i < len(value2):
        value.append(value2[i])
        i+=1
        appen()
    return value

print(value)