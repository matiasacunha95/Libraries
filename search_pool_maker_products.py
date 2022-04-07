''' Search pool maker from a document with a list of dictionaries '''
import json
from search_pool_maker_ingredients import *

filename = 'foods'

def title_spliter_foods(title):
    #'Returns an array with a search pool for each dictionary'
    secuence = []
    i = 0
    for letter in title:
        if len(secuence) > 0:
            secuence.append(secuence[i - 1] + letter)
        else:
            secuence.append(letter)
    return secuence

def get_search_pool(data):
    #'Returns new data with a search pool for each dictionary'
    new_data = []
    for elem in data:
        search_key_words = []
        elem['price'] = 0
        search_key_words += title_spliter_foods(elem['title'])
        search_key_words += title_spliter_foods(elem['brand'])
        for word in elem['title'].split(' '):
            search_key_words += title_spliter_foods(word)
        elem['searchKeyWords'] = list(dict.fromkeys(search_key_words))
        new_data.append(elem)
    return new_data

def main():
    data = get_document_data(filename)
    new_data = get_search_pool(data)
    send_data_to_file(new_data, filename)

if __name__ == '__main__':
    main()
