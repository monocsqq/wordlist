import atexit
import pandas as pd
import pickle

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
            add_word(key)
            return data[key][0]
        else:
            return 'Cancelled'

# Add a word
def add_word(key):
    try:
        temp = ['word', 0]
        temp[0] = input('Enter the word: ')
        data[key] = temp 
    except KeyboardInterrupt:
        return 'Cancelled'
    return data[key][0]

# Main
if __name__ == '__main__':
    print('Loading data')
    load_data()
    print('Data loaded')
    print('Enter a word to search')
    print('If you want to quit, enter Q or press ctrl+C')
    while True:
        try:
            word = input('Enter word: ')
            if word == 'Q':
                break
            print(search(word))
        except KeyboardInterrupt:
            print('')
            break
    print('Bye')
    atexit.register(save_data)
