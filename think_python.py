import string
import random
import os

def right_justify(s):
    print(' '*(70-len(s)) + s)


def do_twice(function):
    function()
    function()


def print_twice(function, s):
    function(s)
    function(s)


def print_grid():
    print(('+ - - - - ')*2 + '+')
    print(('|         ')*2 + '|')


def make_word_list():
    word_list = []
    book = open('book.txt')
    for line in book:
        line = line.split()
        for word in line:
            word = word.lower()
            for char in string.punctuation:
                word = word.replace(char, "")
            word_list.append(word)
    return word_list


def make_histogram(word_list):
    hist = {}
    for word in word_list:
        if word not in hist:
            counter = 0
            for word2 in word_list:
                if word == word2:
                    counter += 1
            hist.update({word: counter})
    return hist


def make_weights(hist):
    start = 0
    stop = 0
    weights = {}
    for word in hist:
        stop += hist.get(word)
        weights.update({word: str(start)+" "+str(stop)})
        start = stop
    return weights


def random_word():
    word_list = make_word_list()
    histogram = make_histogram(word_list)
    weights = make_weights(histogram)
    value = random.randint(1, len(word_list))
    for word in weights:
        interval = weights.get(word)
        interval = interval.split()
        if int(interval[0]) < value & value <= int(interval[1]):
            print(value, word)

    print(weights)


def walk(dirname):
    try:
        fin = open('bad_file')
        for line in fin:
            print(line)
            fin.close()
    except:
        print('Something went wrong.')

def directory():
    cwd = os.getcwd()
    path = os.path.abspath('book.txt')
    walk(cwd)
    ldir = os.listdir(cwd)
    print(ldir)


if __name__ == "__main__":
    directory()

