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
