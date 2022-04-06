''' Search pool maker from a document with a list of dictionaries '''
import json

#filename = 'ingredients'

def get_document_data(filename):
    'Get dictionaries list from json document'
    with open(f'{filename}.json') as f:
        document = json.load(f)
    return document

def search_pool_generator(data):
    'Returns new data with a search pool for each dictionary'
    new_data = []
    for elem in data:
        search_key_words = title_spliter(elem['name'])
        elem['searchKeyWords'] = search_key_words
        new_data.append(elem)
    return new_data

def title_spliter(string):
    'Returns an array with the text secuence of a given string'
    secuence = []
    i = 0
    for letter in string:
        if len(secuence) > 0:
            secuence.append(secuence[i - 1] + letter)
        else:
            secuence.append(letter)
    return secuence

def send_data_to_file(json_data, filename):
    'Write given data to json file with 4 spaces indentation and utf-8 codification'
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)

def main():
    data = get_document_data()
    new_data = search_pool_generator(data)
    send_data_to_file(new_data)

if __name__ == '__main__':
    main()
