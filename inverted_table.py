# inverted table to store word_name

from inverted_index import *

class table():

    #__init__ method
    def __init__(self):
        self.inverted_table = []
    #end __init__()

    #parse_data(): return dictionary-type word_list
    def parse_data(self, data):
        #split space
        list = data.split()
        #split other non-alpha and non-digit characters
        for words in range(len(list)):
            word = list[words]
            start = -1
            end = index = 0
            #string has only one character must have if-condition to check if isalpha()
            if len(word) > 1:
                while index < len(word):
                    #word either alpha or digit
                    if word[index].isalpha() or word[index].isdigit():
                        if start == -1: #start must index first character in the string
                            start = index   #end must increment when alpha character appears
                        end += 1
                    else:
                        if word[index - 1].isalpha() or word[index - 1].isdigit():   #end may index the non-alpha character at the tail of substring
                            end = index
                            break
                    index += 1
                #add substring to list
                list[words] = word[start:end ]
            elif not word[0].isalpha(): #all string length must be breater than 0
                list.remove(list[word]) #if not alpha, the string comp is delete
        #need more advance parsing
        return list
    #end parser_data()

    #categorize word
    def categorize_word(self, text_name, data):
        '''
        :param text_name: name of text
        :param parse_data: list of split words
        :return:
        '''
        list = parser_data(data)
        for index1 in range(len(self.inverted_table)):
            for index2 in list:
                if self.inverted_table[index1] is not list[index2]:
                    self.inverted_table.append(word_index(list[index2]))
                else:
                    word = self.inverted_table[index1]
                    word.add_word_index(text_name, index2)
    #end categorize_word()

    #create inverted_table
    def create_inverted_table(self, file_name):
        file = open(str(file_name), 'r')    #open file
        data = file.read()

        #add data to inverted_table
        list = self.parse_data(data)
        if not self.inverted_table:
            for index in range(len(list)):
                word = word_index(list[index], file_name, index)
                self.inverted_table.append(word)
        else:
            word_list = []
            for index in range(len(self.inverted_table)):
                word_list.append(self.inverted_table[index].get_word())
            for index in range(len(list)):
                if not list[index] in word_list:
                    word = word_index(list[index], str(file_name), index)
                    self.inverted_table.append(word)
                else:
                    ind = word_list.index(list[index])
                    self.inverted_table[ind].add_word_text(str(file_name), index)
        file.close()    #close file
    #end create_inverted_table

    #find(): search method for word
    def find(self, word):
        word_index = []
        for index in range(len(self.inverted_table)):
            w = self.inverted_table[index]
            if word == self.inverted_table[index]:
                word_index.append(index)
        print("The word " + word + " is in the text")
        print(word_index)
        return 1
    #end find()

    #print_table(): print inverted table
    def print_table(self):
        for element in self.inverted_table:
            print(element.get_word())
        print("done")
    #end print_table()

#end inverted_table class