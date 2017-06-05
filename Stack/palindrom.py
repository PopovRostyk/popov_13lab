from arraystack import ArrayStack
class Palindrom():
    def __init__(self):
        self.lst = []
        self.uk_lst, self.en_lst = [], []

    def palindrom(self, word):
        if len(word) >= 2:
            word = str(word)
            stack = ArrayStack()
            for i in range(len(word) // 2):
                stack.push(word[i])
            if len(word) % 2:  # odd
                for i in range(len(word) // 2):
                    if word[len(word) // 2 + 1 + i] != stack.pop():
                        return False
                return True
            else:
                for i in range(len(word) // 2):
                    if word[len(word) // 2 + i] != stack.pop():
                        return False
                return True

    def read(self, en=0, uk=0):
        if en == 1:
            file = open("words.txt",'r', encoding='utf-8')
            for items in file.readlines():
                self.lst.append(items.strip().lower())
            file.close()
        if uk == 1:
            file = open('base.lst','r', encoding='utf-8')
            for items in file.readlines():
                self.lst.append(items.strip().lower())
            file.close()

    def uk_words(self):
        self.read(uk=1)
        for items in self.lst:
            if self.palindrom(items):
                self.uk_lst.append(items)
        self.lst = []

    def en_words(self):
        self.read(en=1)
        for items in self.lst:
            if self.palindrom(items) and items not in self.en_lst:
                self.en_lst.append(items)
        self.lst = []

    def write_in_files(self):
        file_uk = open("palindrome_uk.txt", 'w', encoding='utf-8')
        file_en = open("palindrome_en.txt", 'w', encoding='utf-8')
        for items in self.uk_lst:
            file_uk.write(items + '\n')
        for items in self.en_lst:
            file_en.write(items + '\n')

a = Palindrom()
a.uk_words()
a.en_words()
a.write_in_files()