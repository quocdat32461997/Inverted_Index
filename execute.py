from inverted_index import word_index
from inverted_table import table

tab = table()

tab.create_inverted_table("text.txt")
tab.create_inverted_table("text11.txt")
tab.find('Hello')

tab.print_table()