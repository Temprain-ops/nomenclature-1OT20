import re

from count_nomenclature import half_hundred, half_million, hundred, million, regexp_config, quarter, ten, two_hundred


def get_nomenclatures(nomenclature):
    if re.match(regexp_config.million_regexp, nomenclature):
        nomenclatures_list = million.get_million_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.half_million_regexp, nomenclature):
        nomenclatures_list = half_million.get_half_million_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.two_hundred_regexp, nomenclature):
        nomenclatures_list = two_hundred.get_two_hundred_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.hundred_regexp, nomenclature):
        nomenclatures_list = hundred.get_hundred_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.half_hundred_regexp, nomenclature):
        nomenclatures_list = half_hundred.get_half_hundred_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.quarter_regexp, nomenclature):
        nomenclatures_list = quarter.get_quarter_list(nomenclature.split(regexp_config.split_symbol))
    elif re.match(regexp_config.ten_regexp, nomenclature):
        nomenclatures_list = ten.get_ten_list(nomenclature.split(regexp_config.split_symbol))
    else:
        raise Exception('doesn\'t match regexp')
    return nomenclatures_list


if __name__ == '__main__':
    nomenclatures = get_nomenclatures('B-13-XVIII')
    for i in range(1, 10):
        print(nomenclatures[i - 1], end=' ')
        if i % 3 == 0:
            print(' ')
