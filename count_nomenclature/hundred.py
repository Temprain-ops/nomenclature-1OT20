from count_nomenclature import million, regexp_config


def get_hundred_list(hundred):
    row = hundred[regexp_config.row_letter]
    million_number = int(hundred[regexp_config.column_number])
    hundred_number = int(hundred[regexp_config.hundred_number])
    nomenclatures_list = []
    if 1 < hundred_number < 12:
        million_neighbour = million.get_million_list([row, million_number])[1]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(132 + hundred_number - 1))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(132 + hundred_number))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(132 + hundred_number + 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 13))

    elif hundred_number % 12 == 1 and 1 < hundred_number < 133:
        million_neighbour = million.get_million_list([row, million_number])[3]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 11))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number + 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 1))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number + 11 + 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 13))

    elif hundred_number % 12 == 0 and 12 < hundred_number < 144:
        million_neighbour = million.get_million_list([row, million_number])[5]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 13))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 11 - 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 12))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 11 + 12))

    elif 133 < hundred_number < 144:
        million_neighbour = million.get_million_list([row, million_number])[7]
        million_neighbour_split = million_neighbour.split(regexp_config.split_symbol)
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 13))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 1))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 132 - 1))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 132))
        nomenclatures_list.append(million_neighbour_split[regexp_config.row_letter] + '-' + million_neighbour_split[
            regexp_config.column_number] + '-' + str(hundred_number - 132 + 1))

    elif hundred_number == 1:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[0] + '-' + str(144))
        nomenclatures_list.append(million_neighbours[1] + '-' + str(133))
        nomenclatures_list.append(million_neighbours[1] + '-' + str(134))
        nomenclatures_list.append(million_neighbours[3] + '-' + str(12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(2))
        nomenclatures_list.append(million_neighbours[3] + '-' + str(24))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(13))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(14))
    elif hundred_number == 12:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[1] + '-' + str(143))
        nomenclatures_list.append(million_neighbours[1] + '-' + str(144))
        nomenclatures_list.append(million_neighbours[2] + '-' + str(133))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(million_neighbours[5] + '-' + str(1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 12))
        nomenclatures_list.append(million_neighbours[5] + '-' + str(13))
    elif hundred_number == 133:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(million_neighbours[3] + '-' + str(132))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 11))
        nomenclatures_list.append(million_neighbours[3] + '-' + str(144))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 1))
        nomenclatures_list.append(million_neighbours[6] + '-' + str(12))
        nomenclatures_list.append(million_neighbours[7] + '-' + str(1))
        nomenclatures_list.append(million_neighbours[7] + '-' + str(12))
    elif hundred_number == 144:
        million_neighbours = million.get_million_list([row, million_number])
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 13))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(million_neighbours[5] + '-' + str(121))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(million_neighbours[6] + '-' + str(133))
        nomenclatures_list.append(million_neighbours[7] + '-' + str(11))
        nomenclatures_list.append(million_neighbours[7] + '-' + str(12))
        nomenclatures_list.append(million_neighbours[8] + '-' + str(1))
    else:
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 13))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number - 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 1))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 11))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 12))
        nomenclatures_list.append(row + '-' + str(million_number) + '-' + str(hundred_number + 13))
    return nomenclatures_list
