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
        return data[key][0]
    except KeyError:
        print('word not found')
        print('Do you want to add it?')
        add = input('[y]/n: ')
        if add == 'y' or add == '':
            try:
                temp = ['word', 0]
                temp[0] = input('Enter the word: ')
                data[key].append(temp[0]) 
            except KeyboardInterrupt:
                print('Cancelled')
                return
            return data[key]
        else:
            print('Cancelled')
            return

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
                print('Bye')
                break
            print(search(word))
        except KeyboardInterrupt:
            print('\nBye')
            break
    atexit.register(save_data)
