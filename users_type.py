''' Script that split nutritionists from other users'''

from search_pool_maker_ingredients import get_document_data, \
					  send_data_to_file

def nutri_users(users):
    ''' returns a list of nutritionists users '''
    nutris = []
    for user in users:
        if user.get('isNutritionist'):
            nutris.append(user)
    return nutris

def main():
    data = get_document_data('accounts')
    nutris = nutri_users(data)
    send_data_to_file(nutris, 'nutris')

if __name__ == '__main__':
    main()

