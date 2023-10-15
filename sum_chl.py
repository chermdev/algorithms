import time


def find_solutions_recursive(numbers: list[int], target: int):
    """
    Finds all unique combinations of numbers in the input list that
    add up to the target value using a recursive approach.

    Args:
        numbers (list[int]): A list of integers to find combinations from.
        target (int): The target value to find combinations that add up to.

    Returns:
        list[list[int]]: A list of lists containing all unique
        combinations of numbers that add up to the target value.
    """
    def find_sum(start: int,
                 target: int,
                 combination: list[int]):

        if target == 0:
            result.append(combination[:])
            return

        if not numbers or target < 0:
            return

        for index in range(start, len(numbers)):

            if index > start and numbers[index] == numbers[index - 1]:
                continue

            combination.append(numbers[index])
            find_sum(index + 1, target - numbers[index], combination)
            combination.pop()

    numbers.sort()
    result = []
    find_sum(0, target, [])
    return result


def find_combinations_stack_1(numbers: list[int], target: int):
    result = []
    numbers.sort()
    stack = [(0, target, [])]
    while stack:
        start, target, combination = stack.pop()
        if target == 0:
            result.append(combination)
            continue
        for index in range(start, len(numbers)):
            if index > start and numbers[index] == numbers[index - 1]:
                continue
            if numbers[index] > target:
                break
            stack.append((index + 1, target - numbers[index],
                          combination + [numbers[index]]))
    return result


def find_combinations_stack_2(numbers: list[int],
                              target: int) -> list[list[int]]:
    result = []
    numbers.sort()
    stack = [(0, target, [])]
    while stack:
        start, target, combination = stack.pop()
        if target == 0:
            result.append(combination)
            continue
        for index in range(start, len(numbers)):
            if index > start and numbers[index] == numbers[index - 1]:
                continue
            if numbers[index] > target:
                break
            if combination and numbers[index] < combination[-1]:
                continue
            stack.append((index+1, target-numbers[index],
                          combination + [numbers[index]]))
    return result


def find_combinations_dynamic_programming(numbers: list[int],
                                          target: int) -> list[list[int]]:
    dp = [[] for _ in range(target+1)]
    dp[0] = [[]]
    for num in numbers:
        for i in range(target, num-1, -1):
            for combo in dp[i-num]:
                new_combo = combo + [num]
                new_combo.sort()  # sort the combination to avoid duplicates
                if new_combo not in dp[i]:
                    dp[i].append(new_combo)
                # dp[i].append(combo + [num])
    return dp[target]


# numbers=[1, 2, 4, 5, 6, 8]
# target=9
numbers = [2, 3, 1, 2, 1, 5, 4]
target = 6
expected_output = [[1, 5], [1, 4, 1], [1, 3, 2], [1, 2, 2, 1], [2, 4]]

start = time.time()
print(find_solutions_recursive(numbers, target))
print(time.time()-start)
start = time.time()
print(find_combinations_stack_1(numbers, target))
print(time.time()-start)
start = time.time()
print(find_combinations_stack_2(numbers, target))
print(time.time()-start)
start = time.time()
print(find_combinations_dynamic_programming(numbers, target))
print(time.time()-start)
