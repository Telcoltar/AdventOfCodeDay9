from commenUtils import get_input_data
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()
levels = {'info': logging.INFO, 'debug': logging.DEBUG}

level = levels.get(options.log.lower())

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def find_sum_in_window(window: set[int], goal):
    for num in window:
        if goal - num == num:
            continue
        if goal - num in window:
            return True
    return False


def solution_part_1(file_name: str, window_size: int) -> int:
    numbers: list[int] = get_input_data(file_name)
    logger.debug(numbers)
    window: set[int]
    for i in range(0, len(numbers)-window_size):
        window = set(numbers[i:i+window_size])
        goal = numbers[i+window_size]
        logger.debug(f"Window: {window}, Goal: {goal}")
        if find_sum_in_window(window, goal):
            continue
        return goal
    return 0


def solution_part_2(file_name: str, window_size: int) -> int:
    goal: int = solution_part_1(file_name, window_size)
    numbers: list[int] = get_input_data(file_name)
    for i in range(2, len(numbers)+1):
        for j in range(0, len(numbers)-i+1):
            if sum(numbers[j:j+i]) == goal:
                return max(numbers[j:j+i]) + min(numbers[j:j+i])
    return 0


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt", 25))
    logger.info(solution_part_2("inputData.txt", 25))
