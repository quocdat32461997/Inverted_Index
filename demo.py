# inverted table to store word_name

from inverted_index import *

class table():

    #__init__ method
    def __init__(self):
        self.inverted_table = []

    #parse_data method return dictionary-type word_list
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
                    #need funciton to add frequency
        return 1
    #create inverted_table
    def create_inverted_table(self, file_name):
        file = open(str(file_name), 'r')    #open file
        data = file.read()

        #add data to inverted_table
        list = self.parse_data(data)
        for index1 in range(len(self.inverted_table)):
            if self.inverted_table[index1].get_word() in list:
                word = word_index(list[index2], file_name, index2)
                self.inverted_table.append(word)
                print("ahh")
            else:
                print("haa")
                word = self.inverted_table[index1]
                word.add_word_text(file_name, index2)


        file.close()    #close file

    #search method for word
    def find(self, word):
        word_index = []
        for index in range(len(self.inverted_table)):
            w = self.inverted_table[index]
            if word == self.inverted_table[index]:
                word_index.append(index)
        print("The word " + word + " is in the text")
        print(word_index)
        return word_index

    #print inverted table
    def print_table(self):
        print(self.inverted_table)