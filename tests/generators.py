import random


def generate_id():
    return str(random.randint(1, 100000))


def generate_document():
    """This random cnpj generator is from this link:
    https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c"""

    def calculate_special_digit(l):
        digit = 0
        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    document = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]
    for _ in range(2):
        document = [calculate_special_digit(document)] + document
    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(document[::-1])
