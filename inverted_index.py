
#word_index:
'''
    word_name: name of word
    word_pos: a dictionary containing key - text_name word in and value - pos of each word frequency in
'''
class word_index():

    #__inint__()
    def __init__(self, w_name, file_name, index):
        self.word_name = w_name
        self.list_file = {file_name:[index]}  #word_pos is a list: key is name of text and value is pos of word in that text
    #end __init__()

    #add_word_text(): add elements of dictionary key - text and value - a list containing positions of the word in text
    def add_word_text(self, file_name, pos):
        '''
        :param file_name: name of text
        :param pos: position of word in text
        :return:
        '''
        #text_name not exist then make dicitonary
        if not file_name in self.list_file:
            temp_dict = {file_name: [pos]}  #create temporary dict to update
            self.list_file.update(temp_dict)
        else:
            #text_name exists then only append pos
            self.list_file[file_name].append(pos)
    #end add_word_text()

    #create_list_pos(): create a list containing position of word in each text
    def create_list_pos(self, pos):
        '''
        :param pos: a list of positions of word in a text
        :return: a list of positions of words
        '''
        #need more work to take parsing_data of word in a text
        #return a list of position of word in a text
        list_pos.append(pos)
        return list_pos
    #end create_list_pos()

    #get_word: to return dictionary containing position of the word in different texts
    def get_word(self):
        return self.word_name
    #end get_word()

#end inverted_index class