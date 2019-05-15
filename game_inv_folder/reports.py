import csv
import re

def read_file(file_name):
    try:
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                data.append(row)
        return data
    except Exception as ex:
        print(ex)


TITLE = 0
COPIES = 1
RELEASE = 2
GENRE = 3
PUBLISHER = 4


# Tasks
def count_games(file_name):                     #1
    data = read_file(file_name)
    if (data == None): return
    return len(data)


def decide(file_name, year):                    #2
    data = read_file(file_name)
    for row in data:
        if (row[RELEASE] == year):
            return True
    return False


def get_latest(file_name):                      #3
    data = read_file(file_name)
    id = 0
    for i in range(len(data)):
        if(data[i][RELEASE] > data[id][RELEASE]):
            id = i
    return data[id][TITLE]


def count_by_genre(file_name, genre):           #4
    data = read_file(file_name)

    counter = 0
    for row in data:
        if(row[GENRE] == genre):
            counter += 1
    return counter

    
def get_line_number_by_title(file_name, title): #5
    data = read_file(file_name)
    line_count = 0
    for line in data:
        line_count += 1
        if (title == line[TITLE]):
            return line_count


# Extras
def sort_abc(file_name):                        #6
    data = read_file(file_name)

    for i in range(len(data) - 1):
        left = data[i][TITLE]
        right_pos = 0
        for j in range(i + 1, len(data)):
            right = data[j][TITLE]
            if(right < left):
                left = right
                right_pos = j
        if(right_pos > 0):
            new = data[right_pos]
            data[right_pos] = data[i]
            data[i] = new
    return data


def get_genres(file_name):                       #7
    data = read_file(file_name)
    if(data == None): return
    
    genres_set = set()
    for row in data:
        genres_set.add(row[GENRE])
    return genres_set


def when_was_top_sold_fps(file_name):            #8
    data = read_file(file_name)
    if(data == None): return
    
    top_sold = 0
    top_year = None
    for row in data:
        if(row[3] == "First-person shooter"):
            if(float(row[COPIES]) > float(top_sold)):
                top_sold = row[COPIES]
                top_year = str(row[RELEASE])
    return top_year
