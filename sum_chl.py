numbers = [2, 3, 1, 2, 1, 5, 4]
# numbers = [1, 1, 1, 1, 1, 1]
target = 6
expected_output = [[1, 5], [1, 4, 1], [1, 3, 2], [1, 2, 2, 1], [2, 4]]


# def find_solutions_recursive(numbers: list[int], target: int):
#     """
#     Finds all unique combinations of numbers in the input list that
#     add up to the target value using a recursive approach.

#     Args:
#         numbers (list[int]): A list of integers to find combinations from.
#         target (int): The target value to find combinations that add up to.

#     Returns:
#         list[list[int]]: A list of lists containing all unique
#         combinations of numbers that add up to the target value.
#     """
#     def find_sum(start: int,
#                  target: int,
#                  combination: list[int]):

#         if target == 0:
#             result.append(combination[:])
#             return

#         if len(numbers) == 0 or target < 0:
#             return

#         for index in range(start, len(numbers)):

#             if index > start and numbers[index] == numbers[index - 1]:
#                 continue

#             combination.append(numbers[index])
#             find_sum(index + 1, target - numbers[index], combination)
#             combination.pop()

#     numbers.sort()
#     result = []
#     find_sum(0, target, [])
#     return result


# print(find_solutions_recursive(numbers, target))


def find_solutions(numbers: list[int], target: int):
    numbers.sort()
    stack = [(0, target, [])]
    result = []

    while stack:
        print('Stack:', stack)
        start, target, combination = stack.pop()
        print('Popped:', (start, target, combination))

        if target == 0:
            print('Adding:', combination)
            result.append(combination)
            continue

        for index in range(start, len(numbers)):
            if index > start and numbers[index] == numbers[index - 1]:
                print('Skipping:', numbers[index])
                continue

            if numbers[index] > target:
                print('Breaking:', numbers[index])
                break

            print('Appending:', numbers[index])
            stack.append((index + 1, target - numbers[index],
                          combination + [numbers[index]]))

    return result


print(find_solutions(numbers, target))
