from collections import defaultdict


def part_1(groups):
    total = 0
    for group in groups:
        seen_answer = defaultdict(bool)
        for answer_set in group:
            for char in answer_set:
                seen_answer[char] = True

        total += len(seen_answer.keys())

    return total


def part_2(groups):
    total = 0

    for group in groups:
        answers = defaultdict(int)
        for answer_set in group:
            for char in answer_set:
                answers[char] += 1

        for times_seen in answers.values():
            if times_seen == len(group):
                total += 1

    return total


def main():
    with open('day6.txt') as f:
        groups = []
        inner = []
        lines = [x.replace('\n', '') for x in f.readlines()]
        lines.append("")
        for line in lines:
            if line == "":
                groups.append(inner)
                inner = []
            else:
                inner.append(line)

    print(part_1(groups))
    print(part_2(groups))


if __name__ == "__main__":
    main()
