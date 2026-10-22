"""Réponses aux 20 exercices de la première série."""


def insert_item(items, index, item):  # 1
    items.insert(index, item)
    return items


def count_spaces(text):  # 2
    return text.count(" ")


def count_letters(text):  # 3
    upper = lower = 0
    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return {"upper": upper, "lower": lower}


def my_sum(numbers):  # 4 : sans sum()
    total = 0
    for number in numbers:
        total += number
    return total


def find_max(numbers):  # 5
    if not numbers:
        raise ValueError("La liste doit contenir au moins un nombre.")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def factorial(number):  # 6
    if number < 0:
        raise ValueError("La factorielle exige un entier positif ou nul.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def list_count(items, target):  # 7 : sans count()
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


def norm(numbers):  # 8
    total = 0
    for number in numbers:
        total += number ** 2
    return total ** 0.5


def is_mono(numbers):  # 9 : les égalités sont autorisées
    ascending = descending = True
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            ascending = False
        if numbers[index] > numbers[index - 1]:
            descending = False
    return ascending or descending


def print_longest(words):  # 10
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)


def separate_types(items):  # 11
    integers, strings = [], []
    for item in items:
        if type(item) is int:
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, strings


def is_palindrome(text):  # 12 : comparaison exacte
    return text == text[::-1]


def sum_over_k(sentence, k):  # 13
    count = 0
    for word in sentence.split():
        if len(word) > k:
            count += 1
    return count


def dict_avg(values):  # 14
    if not values:
        raise ValueError("Le dictionnaire ne doit pas être vide.")
    return my_sum(values.values()) / len(values)


def common_div(first, second):  # 15
    # On exclut 1 pour reproduire l'exemple de l'énoncé.
    if first == second == 0:
        raise ValueError("Deux zéros ont une infinité de diviseurs communs.")
    limit = max(abs(first), abs(second)) if 0 in (first, second) else min(abs(first), abs(second))
    return [n for n in range(2, limit + 1) if first % n == 0 and second % n == 0]


def is_prime(number):  # 16
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def weird_print(numbers):  # 17
    print([value for index, value in enumerate(numbers)
           if index % 2 == 0 and value % 2 == 0])


def type_count(**kwargs):  # 18 : bool est distinct de int
    counts = {}
    for value in kwargs.values():
        name = type(value).__name__
        counts[name] = counts.get(name, 0) + 1
    return counts


def custom_split(text, separator=None):  # 19 : sans split()
    if separator == "":
        raise ValueError("Le séparateur ne peut pas être vide.")
    parts, word = [], ""
    if separator is None:
        for character in text:
            if character.isspace():
                if word:
                    parts.append(word)
                    word = ""
            else:
                word += character
        if word:
            parts.append(word)
        return parts
    index = 0
    while index < len(text):
        if text.startswith(separator, index):
            parts.append(word)
            word = ""
            index += len(separator)
        else:
            word += text[index]
            index += 1
    parts.append(word)
    return parts


def hide_password(password):  # 20 : une étoile par caractère
    return "*" * len(password)


if __name__ == "__main__":
    print("1:", insert_item([1, 3], 1, 2))
    print("2:", count_spaces("Hello Python world"))
    print("3:", count_letters("Hello PYTHON!"))
    print("4:", my_sum([1, 5, 4, 2]))
    print("5:", find_max([0, 1, 3, 50]))
    print("6:", factorial(4))
    print("7:", list_count(['a', 'a', 't', 'o'], 'a'))
    print("8:", norm([1, 2, 2]))
    print("9:", is_mono([7, 6, 5, 5, 2, 0]))
    print("10:", end=" "); print_longest(["Python", "is", "fun"])
    print("11:", separate_types([1, "hello", 2, "Python"]))
    print("12:", is_palindrome("radar"))
    print("13:", sum_over_k("Do or do not there is no try", 2))
    print("14:", dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
    print("15:", common_div(10, 20))
    print("16:", is_prime(11))
    print("17:", end=" "); weird_print([1, 2, 2, 3, 4, 5])
    print("18:", type_count(a=1, b="string", c=1.0, d=True, e=False))
    print("19:", custom_split("hello,Python,world", ","))
    print("20:", hide_password("mypassword"))
