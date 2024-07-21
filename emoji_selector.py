import random
import os

# class Emoji:
#     def __init__(self):
#         self.emojis = open('emoji.txt', 'r', encoding='utf8').read()

#     def get(self):
#         select_emoji = []

#         for x in range(4):
#             select_emoji.append(random.choice(self.emojis))

#         return ' '.join(select_emoji)
    

class Emoji:
    def __init__(self):
        self.emojis = os.listdir('emojis')

    def get(self):
        select_emoji = []

        for x in range(4):
            select_emoji.append('emojis/' + random.choice(self.emojis))

        return select_emoji #' '.join(select_emoji)

if __name__ == '__main__':
    em = Emoji()
    print(em.get())