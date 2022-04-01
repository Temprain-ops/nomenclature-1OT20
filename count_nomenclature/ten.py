from count_nomenclature import quarter, regexp_config


def get_ten_list(nomenclature):
    row = nomenclature[regexp_config.row_letter]
    column = nomenclature[regexp_config.column_number]
    letter = nomenclature[regexp_config.half_hundred_letter]
    letter_quarter = nomenclature[regexp_config.quarter_letter]
    number = nomenclature[regexp_config.hundred_number]
    ten_number = nomenclature[regexp_config.ten_number]
    nomenclature_list = []
    neighbours = quarter.get_quarter_list([row, column, number, letter, letter_quarter])
    if ten_number == '1':
        nomenclature_list.append(neighbours[0] + '-' + '4')
        nomenclature_list.append(neighbours[1] + '-' + '3')
        nomenclature_list.append(neighbours[1] + '-' + '4')
        nomenclature_list.append(neighbours[3] + '-' + '2')
        nomenclature_list.append(
            row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + ten_number)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '2')
        nomenclature_list.append(neighbours[3] + '-' + '4')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '3')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '4')
    elif ten_number == '2':
        nomenclature_list.append(neighbours[1] + '-' + '3')
        nomenclature_list.append(neighbours[1] + '-' + '4')
        nomenclature_list.append(neighbours[2] + '-' + '3')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '1')
        nomenclature_list.append(
            row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + ten_number)
        nomenclature_list.append(neighbours[5] + '-' + '1')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '3')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '4')
        nomenclature_list.append(neighbours[5] + '-' + '3')

    elif ten_number == '3':
        nomenclature_list.append(neighbours[3] + '-' + '2')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '1')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '2')
        nomenclature_list.append(neighbours[3] + '-' + '4')
        nomenclature_list.append(
            row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + ten_number)
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '4')
        nomenclature_list.append(neighbours[6] + '-' + '2')
        nomenclature_list.append(neighbours[7] + '-' + '1')
        nomenclature_list.append(neighbours[7] + '-' + '2')
    else:
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '1')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '2')
        nomenclature_list.append(neighbours[5] + '-' + '1')
        nomenclature_list.append(row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + '3')
        nomenclature_list.append(
            row + '-' + column + '-' + number + '-' + letter + '-' + letter_quarter + '-' + ten_number)
        nomenclature_list.append(neighbours[5] + '-' + '3')
        nomenclature_list.append(neighbours[7] + '-' + '1')
        nomenclature_list.append(neighbours[7] + '-' + '2')
        nomenclature_list.append(neighbours[8] + '-' + '1')
    return nomenclature_list
