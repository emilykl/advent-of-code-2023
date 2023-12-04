# Advent of Code 2023 - Day 4 solution


def part1():
    answer = 0

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            n_winners = count_winning_numbers(line)
            score = 2 ** (n_winners - 1) if n_winners > 0 else 0
            answer += score

    print("Part 1:", answer)


def part2():
    scratchcard_counts = [1] * 216

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            n_winners = count_winning_numbers(line)
            for j in range(i + 1, i + 1 + n_winners):
                scratchcard_counts[j] += scratchcard_counts[i]
    answer = sum(scratchcard_counts)

    print("Part 2:", answer)


def count_winning_numbers(line):
    numbers = line.split(": ")[1]
    winning, i_have = numbers.split(" | ")
    win_set = {n.strip() for n in winning.strip().split()}
    i_have_set = [n.strip() for n in i_have.strip().split()]
    winners = win_set.intersection(i_have_set)
    return len(winners)


if __name__ == "__main__":
    part1()
    part2()
