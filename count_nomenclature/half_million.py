from count_nomenclature import million, regexp_config


def get_half_million_list(nomenclature):
    row = nomenclature[regexp_config.row_letter]
    column = nomenclature[regexp_config.column_number]
    letter = nomenclature[regexp_config.half_million_letter]
    nomenclature_list = []
    neighbours = million.get_million_list([row, column])
    if letter == 'А':
        nomenclature_list.append(neighbours[0] + '-' + 'Г')
        nomenclature_list.append(neighbours[1] + '-' + 'В')
        nomenclature_list.append(neighbours[1] + '-' + 'Г')
        nomenclature_list.append(neighbours[3] + '-' + 'Б')
        nomenclature_list.append(row + '-' + column + '-' + letter)
        nomenclature_list.append(row + '-' + column + '-' + 'Б')
        nomenclature_list.append(neighbours[3] + '-' + 'Г')
        nomenclature_list.append(row + '-' + column + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + 'Г')
    elif letter == 'Б':
        nomenclature_list.append(neighbours[1] + '-' + 'В')
        nomenclature_list.append(neighbours[1] + '-' + 'Г')
        nomenclature_list.append(neighbours[2] + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + letter)
        nomenclature_list.append(neighbours[5] + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + 'Г')
        nomenclature_list.append(neighbours[5] + '-' + 'В')

    elif letter == 'В':
        nomenclature_list.append(neighbours[3] + '-' + 'Б')
        nomenclature_list.append(row + '-' + column + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + 'Б')
        nomenclature_list.append(neighbours[3] + '-' + 'Г')
        nomenclature_list.append(row + '-' + column + '-' + letter)
        nomenclature_list.append(row + '-' + column + '-' + 'Г')
        nomenclature_list.append(neighbours[6] + '-' + 'Б')
        nomenclature_list.append(neighbours[7] + '-' + 'А')
        nomenclature_list.append(neighbours[7] + '-' + 'Б')
    else:
        nomenclature_list.append(row + '-' + column + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + 'Б')
        nomenclature_list.append(neighbours[5] + '-' + 'А')
        nomenclature_list.append(row + '-' + column + '-' + 'В')
        nomenclature_list.append(row + '-' + column + '-' + letter)
        nomenclature_list.append(neighbours[5] + '-' + 'В')
        nomenclature_list.append(neighbours[7] + '-' + 'А')
        nomenclature_list.append(neighbours[7] + '-' + 'Б')
        nomenclature_list.append(neighbours[8] + '-' + 'А')
    return nomenclature_list
