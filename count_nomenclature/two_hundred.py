from count_nomenclature import million, regexp_config


def get_convert_dicts():
    roman_to_arabic = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X': 10,
        'XI': 11,
        'XII': 12,
        'XIII': 13,
        'XIV': 14,
        'XV': 15,
        'XVI': 16,
        'XVII': 17,
        'XVIII': 18,
        'XIX': 19,
        'XX': 20,
        'XXI': 21,
        'XXII': 22,
        'XXIII': 23,
        'XXIV': 24,
        'XXV': 25,
        'XXVI': 26,
        'XXVII': 27,
        'XXVIII': 28,
        'XXIX': 29,
        'XXX': 30,
        'XXXI': 31,
        'XXXII': 32,
        'XXXIII': 33,
        'XXXIV': 34,
        'XXXV': 35,
        'XXXVI': 36,
    }
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
    return roman_to_arabic, arabic_to_roman


def get_two_hundred_list(nomenclature):
    row = nomenclature[regexp_config.row_letter]
    million_number = int(nomenclature[regexp_config.column_number])
    roman = nomenclature[regexp_config.two_hundred_number]
    roman_to_arabic, arabic_to_roman = get_convert_dicts()
    roman_number = roman_to_arabic[roman]
    nomenclatures_list = []
    if 1 < roman_number < 6:
        million_neighbour = million.get_million_list([row, million_number])[1]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[30 + roman_number - 1])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[30 + roman_number])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[30 + roman_number + 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 7])

    elif roman_number % 6 == 1 and 1 < roman_number < 31:
        million_neighbour = million.get_million_list([row, million_number])[3]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 5])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number + 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 1])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number + 5 + 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 7])

    elif roman_number % 6 == 0 and 6 < roman_number < 36:
        million_neighbour = million.get_million_list([row, million_number])[5]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 7])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 5 - 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 6])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 5 + 6])

    elif 31 < roman_number < 36:
        million_neighbour = million.get_million_list([row, million_number])[7]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 7])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 1])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 30 - 1])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 30])
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + arabic_to_roman[roman_number - 30 + 1])

    elif roman_number == 1:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[0] + '-' + arabic_to_roman[36])
        nomenclatures_list.append(million_neighbours[1] + '-' + arabic_to_roman[31])
        nomenclatures_list.append(million_neighbours[1] + '-' + arabic_to_roman[32])
        nomenclatures_list.append(million_neighbours[3] + '-' + arabic_to_roman[6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[2])
        nomenclatures_list.append(million_neighbours[3] + '-' + arabic_to_roman[12])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[13])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[14])
    elif roman_number == 6:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[1] + '-' + arabic_to_roman[35])
        nomenclatures_list.append(million_neighbours[1] + '-' + arabic_to_roman[36])
        nomenclatures_list.append(million_neighbours[2] + '-' + arabic_to_roman[31])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(million_neighbours[5] + '-' + arabic_to_roman[1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 6])
        nomenclatures_list.append(million_neighbours[5] + '-' + arabic_to_roman[7])
    elif roman_number == 31:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[3] + '-' + arabic_to_roman[30])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 5])
        nomenclatures_list.append(million_neighbours[3] + '-' + arabic_to_roman[36])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 1])
        nomenclatures_list.append(million_neighbours[6] + '-' + arabic_to_roman[6])
        nomenclatures_list.append(million_neighbours[7] + '-' + arabic_to_roman[1])
        nomenclatures_list.append(million_neighbours[7] + '-' + arabic_to_roman[2])
    elif roman_number == 36:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 7])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(million_neighbours[5] + '-' + arabic_to_roman[25])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(million_neighbours[6] + '-' + arabic_to_roman[36])
        nomenclatures_list.append(million_neighbours[7] + '-' + arabic_to_roman[5])
        nomenclatures_list.append(million_neighbours[7] + '-' + arabic_to_roman[6])
        nomenclatures_list.append(million_neighbours[8] + '-' + arabic_to_roman[1])
    else:
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 7])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number - 4])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 1])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 5])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 6])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + arabic_to_roman[roman_number + 7])
    return nomenclatures_list
