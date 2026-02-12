def conversion(value)
    return value * 9 / 5 + 32


def is_strong(values):
    return sum(values) / len(values) > 50


def average(values):
    return sum(values) / len(values)
