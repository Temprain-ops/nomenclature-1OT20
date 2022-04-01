from count_nomenclature import hundred, regexp_config


def get_half_hundred_list(nomenclature):
    row = nomenclature[regexp_config.row_letter]
    column = nomenclature[regexp_config.column_number]
    letter = nomenclature[regexp_config.half_hundred_letter]
    number = nomenclature[regexp_config.hundred_number]
    nomenclature_list = []
    neighbours = hundred.get_hundred_list([row, column, number])
    if letter == 'А':
        nomenclature_list.append(neighbours[0] + '-' + 'Г')
        nomenclature_list.append(neighbours[1] + '-' + 'В')
        nomenclature_list.append(neighbours[1] + '-' + 'Г')
        nomenclature_list.append(neighbours[3] + '-' + 'Б')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Б')
        nomenclature_list.append(neighbours[3] + '-' + 'Г')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Г')
    elif letter == 'Б':
        nomenclature_list.append(neighbours[1] + '-' + 'В')
        nomenclature_list.append(neighbours[1] + '-' + 'Г')
        nomenclature_list.append(neighbours[2] + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter)
        nomenclature_list.append(neighbours[5] + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Г')
        nomenclature_list.append(neighbours[5] + '-' + 'В')

    elif letter == 'В':
        nomenclature_list.append(neighbours[3] + '-' + 'Б')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Б')
        nomenclature_list.append(neighbours[3] + '-' + 'Г')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Г')
        nomenclature_list.append(neighbours[6] + '-' + 'Б')
        nomenclature_list.append(neighbours[7] + '-' + 'А')
        nomenclature_list.append(neighbours[7] + '-' + 'Б')
    else:
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'Б')
        nomenclature_list.append(neighbours[5] + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter)
        nomenclature_list.append(neighbours[5] + '-' + 'В')
        nomenclature_list.append(neighbours[7] + '-' + 'А')
        nomenclature_list.append(neighbours[7] + '-' + 'Б')
        nomenclature_list.append(neighbours[8] + '-' + 'А')
    return nomenclature_list
