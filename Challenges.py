# def total_goals(laLiga, copaDelRey, championsLeague):
#     return laLiga + copaDelRey + championsLeague
#
# goals_in_la_liga = 5
# goals_in_copa_del_rey = 10
# goals_in_champions_league = 15
#
# total_goals_scored = total_goals(goals_in_la_liga, goals_in_copa_del_rey, goals_in_champions_league)
#
# print(total_goals_scored)



# def str_count(strng, letter):
#     return strng.count(letter)
#
# print(str_count("Hello", 'o'))
# print(str_count("Hello", 'l'))
# print(str_count("", 'z'))


# def digitize(n):
#     return [int(digit) for digit in str(n)][::-1]
#
# print(digitize(35231))
# print(digitize(0))


# Is the string uppercase
def is_uppercase(inp):
    return inp.isupper() or not any(c.islower() for c in inp)

print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))

def is_uppercase(inp):
    return inp.isupper() or not any(c.islower() for c in inp)

print(is_uppercase("OlaKI edwIN"))
print(is_uppercase("OLAKI EDWIN"))
print(is_uppercase("olakiedwin"))
print(is_uppercase("EDWINolaki"))
print(is_uppercase("edwinOLAKI"))