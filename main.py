import atexit
import os
import pickle
import re
import sys

install_dir = os.path.dirname(sys.executable)
data = {}

# Load the data
def load_data():
    global data
    try:
        with open(os.path.join(install_dir, 'wordlist_data.pkl'), 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print('File not found, creating new data')
        #print('path:', os.path.join(install_dir, 'wordlist_data.pkl'))
        data = {"sample" : ["サンプル", 0]}

# Save the data
def save_data():
    with open(os.path.join(install_dir, 'wordlist_data.pkl'), 'wb') as f:
        pickle.dump(data, f)
    print('Data saved to:', os.path.join(install_dir, 'wordlist_data.pkl'))

# check word
def is_word(word):
    return re.match(r'^[a-zA-Z]+$', word)

# Search for a key
def search(key):
    try:
        data[key][1] += 1
        return f"意味: {data[key][0]}\n検索回数: {data[key][1]}"
    except KeyError:
        print(f'word not found: {key}')
        print('Do you want to add it?')
        try:
            add = input('[y]/n: ')
            if add == 'y' or add == '':
                return add_word(key)
            else:
                return 'Cancelled'
        except KeyboardInterrupt:
            return '\nCancelled'
        except EOFError:
            return '\nCancelled'

# Add a word
def add_word(key):
    if key in data:
        print('the word already exists')
        return 'Cancelled'
    try:
        temp = ['word', 0]
        temp[0] = input('Enter the meaning: ')
        data[key] = temp 
        return data[key][0]
    except KeyboardInterrupt:
        return '\nCancelled'
    except EOFError:
        return '\nCancelled'

# Edit a word
def edit(key):
    try:
        temp = ['word', data[key][1]]
        temp[0] = input('Enter the word: ')
        data[key] = temp 
    except KeyError:
        print('word not found')
        print('Do you want to add it?')
        try:
            add = input('[y]/n: ')
            if add == 'y' or add == '':
                return add_word(key)
            else:
                return 'Cancelled'
        except KeyboardInterrupt:
            return '\nCancelled'
        except EOFError:
            return '\nCancelled'
    except KeyboardInterrupt:
        return '\nCancelled'
    except EOFError:
        return '\nCancelled'
    return data[key][0]

def del_word(key):
    try:
        print(f'Are you sure you want to delete this word?: {key}')
        if input(f'y/n: ') == 'y':
            try:
                del data[key]
                return 'Deleted: {key}'
            except KeyError:
                return 'word not found: {key}'
        else:
            return 'Cancelled'
    except KeyboardInterrupt:
        return '\nCancelled'
    except EOFError:
        return '\nCancelled'

def list_words():
    for key in sorted(data.keys()):
        print(f'{key}: {data[key][0]}')

# Main
def main():
    print('Loading data')
    load_data()
    print('Data loaded')
    print('Enter a word to search')
    # Mode: S = Search, E = Edit, R = Remove
    mode = 'Search' # Search mode
    while True:
        try:
            word = input(f'({mode})Enter word: ')
            if word == 'S':
                mode = 'Search'
                continue
            elif word == 'A':
                mode = 'Add'
                continue
            elif word == 'E':
                mode = 'Edit'
                continue
            elif word == 'R':
                mode = 'Remove'
                continue
            elif word == 'L':
                list_words()
                continue
            elif word == 'Q':
                break
            elif not is_word(word):
                print('Invalid word')
                continue
            if mode == 'Search':
                print(search(word))
            elif mode == 'Add':
                print(add_word(word))
            elif mode == 'Edit':
                print(edit(word))
            elif mode == 'Remove':
                print(del_word(word))
        except KeyboardInterrupt:
            print('')
            break
        except EOFError:
            print('')
            break
    print('Bye')
    atexit.register(save_data)

if __name__ == '__main__':
    main()
