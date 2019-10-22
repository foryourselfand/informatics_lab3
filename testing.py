from datetime import datetime
from typing import List, Union
from sys import argv


def get_variant() -> int:
    base_variant = 6

    args = argv[1:]
    if len(args) == 1:
        try:
            variant = int(args[0])
        except ValueError:
            variant = base_variant

        if 5 <= variant <= 8:
            return variant

    return base_variant


def get_text(input_file_name: str = 'input.txt') -> List[str]:
    text: List[str] = list()
    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        text += [line.replace('\n', '') for line in input_file.readlines()]
    return text


def get_arr_split(text: List[str]) -> List[list]:
    arr_split: List[List[Union[str, int, datetime]]] = list()
    for line_raw in text:
        line_split = line_raw.split(' ')

        full_name = ' '.join(line_split[:2])

        dates = [datetime.strptime(date_str, '%d.%m.%Y') for date_str in line_split[2: 4]]

        points = line_split[4:]

        points_str = ' '.join(points)

        average_point = (sum(map(int, points))) / len(points)

        line_split = [full_name, *dates, average_point, points_str]
        arr_split.append(line_split)

    return arr_split


def print_arr(arr: List[list]):
    for line in arr:
        full_name = line[0]

        dates = [date.strftime('%d.%m.%Y') for date in line[1: 3]]

        average_point_raw = line[3]

        if float(average_point_raw) == int(average_point_raw):
            average_point_str = str(int(average_point_raw))
        else:
            average_point_str = '{:.6f}'.format(average_point_raw).replace('.', ',')

        points = f'{line[-1]} -> {average_point_str}'

        line_temp = [full_name, *dates, points]

        line_str = ' | '.join(line_temp)
        print(line_str)


def main():
    variant = get_variant()
    text = get_text()

    arr_split = get_arr_split(text)
    arr_sorted = sorted(arr_split, reverse=True, key=lambda x: x[variant - 5])

    print_arr(arr_sorted)


if __name__ == '__main__':
    main()
