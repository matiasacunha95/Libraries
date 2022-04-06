''' Script that add utf-8 to a json file '''
import json

filename = 'shoppings'

def get_document_data():
    #'Get json file data'
    with open(f'{filename}.json') as f:
        document = json.load(f)
    return document

def send_data_to_file(data):
    #'Write given data to json file with 4 spaces indentation and utf-8 codification'
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False) 

def main():
    #'Main function'
    data = get_document_data()
    send_data_to_file(data)

if __name__ == '__main__':
    main()
