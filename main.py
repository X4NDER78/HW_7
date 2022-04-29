# HW7

def digits(age):
    """
    FUNCTION FIND NUMBERS WITH THE SAME NUMERIC
    Args:
        age (int):

    Returns: LIST WITH THE SAME NUM
    """

    return [int(c) for c in str(age)][::-1]

except_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def compair_except_with_list(x):        #Все работало у меня,но не получается после того,что я решил не вручную писать исключения,а написать функцию,которая сравнивает age и лист?
    """
    FUNCTION COMPAIR ARG(AGE) WITH EXCEPTION LIST
    Args:
         x: int

    Returns:GIVES BACK AGE , IF IT COINCIDED WITH NUM AT LIST
    """
    x = age
    while (x not in y): print("X = ", x)
    x = random.randrange(0, 1999)

    return x

exc = compair_except_with_list(x)

def form_of_age(age):
    """
    FUNCTION COMPAIR ARG(AGE) WITH RULES OF CINEMA
    Args:
        age: int

    Returns:GIVES BACK CORRECT FORM OF YEAR
    """

    if age % 10 == 1 and age != 11:
        res = 'рік'
    elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        res = 'роки'
    elif age % 10 == 5 or age % 10 == 6 or age % 10 == 7 or age % 10 == 8 or age % 10 == 9 or age == exc:
        res = 'років'

    return res

age = int(input('Введіть свій рік ->'))
repdigit = digits(age)
year = form_of_age(age)

if len(set(repdigit)) != len(repdigit):
    print(f'О вам {age}{year}! Який цікавий вік')
else:
    print(f'Незважаючи на те, що вам {age}{year}, білетів всеодно нема!')



