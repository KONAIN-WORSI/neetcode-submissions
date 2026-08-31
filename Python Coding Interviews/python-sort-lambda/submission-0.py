from typing import List


def sort_words(words: List[str]) -> List[str]:
    n = len(words)
    result = words.copy()

    compare = lambda a, b: len(a) < len(b)

    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(result[j], result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def sort_numbers(numbers: List[int]) -> List[int]:
    n = len(numbers)
    result = numbers.copy()

    compare = lambda a, b: abs(a) > abs(b)

    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(result[j], result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
