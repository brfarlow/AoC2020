def valid_year(minimum, maximum, value):
    return minimum <= int(value) <= maximum


def valid_height(value):
    if value.endswith('in'):
        hgt = int(value.split('in')[0])
        return 59 <= hgt <= 76
    elif value.endswith('cm'):
        hgt = int(value.split('cm')[0])
        return 150 <= hgt <= 193

    return False


def valid_hair_color(value):
    chars = ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if not value.startswith('#') or len(value) != 7:
        return False

    for char in value:
        if char not in chars:
            return False

    return True


def valid_eye_color(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_passport_id(value):
    if len(value) == 9:
        try:
            int(value)
            return True
        except ValueError:
            pass

    return False


with open('day4.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]
    # append empty line at end for cleaner passport parsing
    lines.append("")
    passports = []
    passport = ""
    for line in lines:
        if line == "":
            passport = passport.strip()
            passports.append(dict(x.split(':') for x in passport.split(' ')))
            passport = ""
        else:
            passport += line + " "

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = []

for passport in passports:
    is_valid = True
    for key in required_keys:
        if key not in passport.keys():
            is_valid = False
            break

    if is_valid:
        valid_passports.append(passport)

print(len(valid_passports))

part_2_valid_passports = []
for passport in valid_passports:
    if valid_year(1920, 2002, passport.get('byr')) and \
            valid_year(2010, 2020, passport.get('iyr')) and \
            valid_year(2020, 2030, passport.get('eyr')) and \
            valid_height(passport.get('hgt')) and \
            valid_hair_color(passport.get('hcl')) and \
            valid_eye_color(passport.get('ecl')) and \
            valid_passport_id(passport.get('pid')):
        part_2_valid_passports.append(passport)

print(len(part_2_valid_passports))
