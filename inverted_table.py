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
                        if start == -1:
                            start = index
                        end += 1
                    else:
                        # end may index the non-alpha character at the tail of substring
                        if word[index - 1].isalpha() or word[index - 1].isdigit():
                            end = index
                            break
                    index += 1
                #add substring to list
                list[words] = word[start:end]
            # all string length must be breater than 0
            elif not word[0].isalpha():
                list.remove(list[word]) #the string comp is delete

        return list
    #end parser_data()


    #create inverted table
    def create_inverted_table(self, file_name):
        '''
        :param file_name: name of file that contains a specific word
        :return: void
        '''
        #open file
        file = open(str(file_name), 'r')
        data = file.read()

        #add data to inverted_table
        data_list = self.parse_data(data)
        if not self.inverted_table:
            for index in range(len(data_list)):
                word = word_index(data_list[index], file_name, index)
                self.inverted_table.append(word)
        else:
            word_list = []

            for index in range(len(self.inverted_table)):
                word_list.append(self.inverted_table[index].get_word())
            #add word
            for index in range(len(data_list)):
                if not data_list[index] in word_list:
                    #initiate word_index variables
                    word = word_index(data_list[index], str(file_name), index)
                    self.inverted_table.append(word)
                else:
                    #add duplicates to word_index variables
                    ind = word_list.index(data_list[index])
                    self.inverted_table[ind].add_word_text(str(file_name), index)

        #close file
        file.close()
    #end create_inverted_table


    #find(): search method for word
    def find(self, word):
        '''
        :param word: word need finding
        :return: find index of word in different files and print out inverted_tabl
        '''
        for index in range(len(self.inverted_table)):
            if word == self.inverted_table[index].get_word():
                return index
    #end find()


    #print_table(): print inverted table
    def print_table(self, word):
        '''
        :param word: inverted_table variable that represent a word
        :return: return search results in form of string variables
        '''
        if not self.find(word):
            print("Word not found\n")
            exit(1)

        w = self.inverted_table[self.find(word)]
        word_table = w.list_file
        strng = "Table of " + w.get_word() + " :" + '\n'

        for element in word_table.keys():
            strng += str(element) + "   " + str(word_table[element]) + '\n'

        return strng
    #end print_table()

#end inverted_table class