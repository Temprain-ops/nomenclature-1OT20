from random import shuffle

delimiter = '-'
row_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V']
column_list = list(range(1, 61))
half_million_list = ['А', 'Б', 'В', 'Г']
two_hundred_list = list(range(1, 37))
hundred_list = list(range(1, 145))
half_hundred_list = list(half_million_list)
quarter_list = ['а', 'б', 'в', 'г']
ten_list = [1, 2, 3, 4]

arabic_to_roman = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII',
    13: 'XIII',
    14: 'XIV',
    15: 'XV',
    16: 'XVI',
    17: 'XVII',
    18: 'XVIII',
    19: 'XIX',
    20: 'XX',
    21: 'XXI',
    22: 'XXII',
    23: 'XXIII',
    24: 'XXIV',
    25: 'XXV',
    26: 'XXVI',
    27: 'XXVII',
    28: 'XXVIII',
    29: 'XXIX',
    30: 'XXX',
    31: 'XXXI',
    32: 'XXXII',
    33: 'XXXIII',
    34: 'XXXIV',
    35: 'XXXV',
    36: 'XXXVI',

}


def get_million():
    shuffle(row_list)
    shuffle(column_list)
    return row_list[0] + delimiter + str(column_list[0])


def get_half_million():
    shuffle(half_million_list)
    return get_million() + delimiter + half_million_list[0]


def get_two_hundred():
    shuffle(two_hundred_list)
    return get_million() + delimiter + arabic_to_roman.get(two_hundred_list[0])


def get_hundred():
    shuffle(hundred_list)
    return get_million() + delimiter + str(hundred_list[0])


def get_half_hundred():
    shuffle(half_hundred_list)
    return get_hundred() + delimiter + half_hundred_list[0]


def get_quarter():
    shuffle(quarter_list)
    return get_half_hundred() + delimiter + quarter_list[0]


def get_ten():
    shuffle(ten_list)
    return get_quarter() + delimiter + str(ten_list[0])


print(get_million())
print(get_half_million())
print(get_two_hundred())
print(get_hundred())
print(get_half_hundred())
print(get_quarter())
print(get_ten())
