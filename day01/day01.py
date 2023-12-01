# Advent of Code 2023 - Day 1 solution

import re

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
digits_spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
digit_first_letters = {d[0]: d for d in digits_spelled.keys()}


def part1():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            line_digits = [c for c in line if c in digits]
            line_total = int(line_digits[0] + line_digits[-1])
            total += line_total
    print("Part 1:", total)


def findall(string, substring):
    return [m.span()[0] for m in re.finditer(substring, string)]


def find_digits(line):
    numeral_locations = [(d, pos) for d in digits for pos in findall(line, d)]
    spelled_locations = [
        (v, pos) for k, v in digits_spelled.items() for pos in findall(line, k)
    ]
    return sorted(numeral_locations + spelled_locations, key=lambda x: x[1])


def part2():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            digit_locations = find_digits(line)
            first_digit = digit_locations[0][0]
            last_digit = digit_locations[-1][0]
            total += int(first_digit + last_digit)
    print("Part 2:", total)


if __name__ == "__main__":
    part1()
    part2()
