from collections import defaultdict


def main():
    with open('day7.txt') as f:
        lines = [x.replace('\n', '') for x in f.readlines()]

    bag_tree = defaultdict(dict)

    for line in lines:
        parent_bag = line.split('bags')[0].strip()
        child_bags = line.split('contain')[1].split(',')

        if child_bags[0].strip().startswith('no'):
            bag_tree[parent_bag] = {}
        else:
            for bag in child_bags:
                bag = bag.strip()
                parts = bag.split(' ')
                number = int(parts[0])
                bag = parts[1] + ' ' + parts[2]

                bag_tree[parent_bag][bag] = number

    can_contain_shiny_gold = set()

    for bag, children in bag_tree.items():
        can_contain_shiny_gold_bag(bag, children, bag_tree, can_contain_shiny_gold)

    print(len(can_contain_shiny_gold))

    print(number_bags_to_fit(bag_tree.get('shiny gold'), bag_tree) - 1)


def can_contain_shiny_gold_bag(bag, children, bag_tree, can_contain_shiny_gold):
    shiny_gold = 'shiny gold'
    if bag != shiny_gold:
        if bag in can_contain_shiny_gold:
            return True
        elif children:
            if shiny_gold in children:
                can_contain_shiny_gold.add(bag)
                return True
            else:
                can_i_contain = False
                for child in children:
                    if can_contain_shiny_gold_bag(child, bag_tree.get(child), bag_tree, can_contain_shiny_gold):
                        can_contain_shiny_gold.add(bag)
                        can_i_contain = True
                return can_i_contain
        else:
            return False


def number_bags_to_fit(bag, bag_tree):
    total = 1
    for child, number in bag.items():
        total += number * number_bags_to_fit(bag_tree.get(child), bag_tree)

    return total


if __name__ == '__main__':
    main()
