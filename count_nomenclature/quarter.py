from count_nomenclature import half_hundred, regexp_config


def get_quarter_list(nomenclature):
    row = nomenclature[regexp_config.row_letter]
    column = nomenclature[regexp_config.column_number]
    letter = nomenclature[regexp_config.half_hundred_letter]
    letter_quarter = nomenclature[regexp_config.quarter_letter]
    number = nomenclature[regexp_config.hundred_number]
    nomenclature_list = []
    neighbours = half_hundred.get_half_hundred_list([row, column, number, letter])
    if letter_quarter == 'а':
        nomenclature_list.append(neighbours[0] + '-' + 'г')
        nomenclature_list.append(neighbours[1] + '-' + 'в')
        nomenclature_list.append(neighbours[1] + '-' + 'г')
        nomenclature_list.append(neighbours[3] + '-' + 'б')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'б')
        nomenclature_list.append(neighbours[3] + '-' + 'г')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'в')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'г')
    elif letter_quarter == 'б':
        nomenclature_list.append(neighbours[1] + '-' + 'в')
        nomenclature_list.append(neighbours[1] + '-' + 'г')
        nomenclature_list.append(neighbours[2] + '-' + 'в')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'а')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter)
        nomenclature_list.append(neighbours[5] + '-' + 'а')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'в')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'г')
        nomenclature_list.append(neighbours[5] + '-' + 'в')

    elif letter_quarter == 'в':
        nomenclature_list.append(neighbours[3] + '-' + 'б')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'а')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'б')
        nomenclature_list.append(neighbours[3] + '-' + 'г')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'г')
        nomenclature_list.append(neighbours[6] + '-' + 'б')
        nomenclature_list.append(neighbours[7] + '-' + 'а')
        nomenclature_list.append(neighbours[7] + '-' + 'б')
    else:
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'а')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'б')
        nomenclature_list.append(neighbours[5] + '-' + 'а')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + 'в')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter)
        nomenclature_list.append(neighbours[5] + '-' + 'в')
        nomenclature_list.append(neighbours[7] + '-' + 'а')
        nomenclature_list.append(neighbours[7] + '-' + 'б')
        nomenclature_list.append(neighbours[8] + '-' + 'а')
    return nomenclature_list
