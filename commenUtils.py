import logging

logger = logging.getLogger(__name__)


def get_input_data(input_file_name: str) -> list[int]:
    f = open(input_file_name, "r")
    numbers: list[int] = []
    for line in f:
        numbers.append(int(line.strip()))
    f.close()
    return numbers
