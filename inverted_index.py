
#word_index:
'''
    word_name: name of word
    word_pos: a dictionary containing key - text_name word in and value - pos of each word frequency in
'''
class word_index():

    #__inint__()
    def __init__(self, w_name, file_name, index):
        self.word_name = w_name
        self.list_file = {file_name:[index]}
        #list_file is a dirctoinary: key is file_name and value is index of word in that file
    #end __init__()

    #add_word_text(): add elements of dictionary key - text and value - a list containing positions of the word in text
    def add_word_text(self, file_name, index):
        '''
        :param file_name: name of text
        :param index: position of word in text
        :return:
        '''
        #text_name not exist then make dicitonary
        if not file_name in self.list_file:
            temp_dict = {file_name:[index]}  #create temporary dict to update
            self.list_file.update(temp_dict)
        else:
            #text_name exists then only append pos
            self.list_file[file_name].append(index)
    #end add_word_text()

    #get_word: to return dictionary containing position of the word in different texts
    def get_word(self):
        '''
        :return: name of word
        '''
        return self.word_name
    #end get_word()

#end inverted_index class