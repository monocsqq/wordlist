import atexit
import pandas as pd
import pickle
import re

data = {}

# Load the data
def load_data():
    global data
    try:
        with open('data.pkl', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print('File not found, creating new data')
        data = {"sample" : ["サンプル", 0]}

# Save the data
def save_data():
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)

# check word
def is_word(word):
    return re.match(r'^[a-zA-Z]+$', word)

# Search for a key
def search(key):
    try:
        data[key][1] += 1
        return f"意味: {data[key][0]}\n検索回数: {data[key][1]}"
    except KeyError:
        print('word not found')
        print('Do you want to add it?')
        add = input('[y]/n: ')
        if add == 'y' or add == '':
            return add_word(key)
        else:
            return 'Cancelled'

# Add a word
def add_word(key):
    try:
        temp = ['word', 0]
        temp[0] = input('Enter the word: ')
        data[key] = temp 
        return data[key][0]
    except KeyboardInterrupt:
        return '\nCancelled'
    # return data[key][0]

# Edit a word
def edit(key):
    try:
        temp = ['word', data[key][1]]
        temp[0] = input('Enter the word: ')
        data[key] = temp 
    except KeyError:
        print('word not found')
        print('Do you want to add it?')
        add = input('[y]/n: ')
        if add == 'y' or add == '':
            return add_word(key)
        else:
            return 'Cancelled'
    except KeyboardInterrupt:
        return '\nCancelled'
    return data[key][0]

# Main
if __name__ == '__main__':
    print('Loading data')
    load_data()
    print('Data loaded')
    print('Enter a word to search')
    print('If you want to quit, press ctrl+C')
    # Mode: S = Search, E = Edit 
    mode = 'Search' # Search mode
    while True:
        try:
            word = input(f'({mode})Enter word: ')
            elif word == 'S':
                mode = 'Search'
                continue
            elif word == 'E':
                mode = 'Edit'
                continue
            elif not is_word(word):
                print('Invalid word')
                continue
            if mode == 'Search':
                print(search(word))
            elif mode == 'Edit':
                print(edit(word))
        except KeyboardInterrupt:
            print('')
            break
    print('Bye')
    atexit.register(save_data)
