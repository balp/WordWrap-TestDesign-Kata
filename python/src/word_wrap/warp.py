from typing import List


def wrap_yngwie(line: str, column: int) -> str:
    def split(input: str, last_space: int, remove_space: bool):
        jump = 1 if remove_space else 0
        return input[:last_space] + '\n' + wrap_yngwie(input[last_space + jump:], column)

    if column <= 0:
        return line
    if len(line) <= column:
        return line
    last_space = line.rfind(' ', 0, column + 1)
    split_at = last_space if last_space >= 0 else column
    return split(line, split_at, last_space >= 0)


def wrap_recursive(line: str, column: int) -> str:
    if column <= 0:
        return line
    if len(line) <= column:
        return line
    index_of_blank = line.rfind(' ', 0, column + 1)
    if index_of_blank >= 0:
        split = index_of_blank
        offset = 1
    else:
        split = column
        offset = 0
    return line[:split] + '\n' + wrap_recursive(line[split + offset:], column)


def wrap_tail_recursive(line: str, column: int) -> str:
    accumulator = []
    _wrap_tail_recursive_function(line, column, accumulator)
    return ''.join(accumulator)


def _wrap_tail_recursive_function(line: str, column: int, accumulator: List[str]) -> None:
    if column <= 0:
        accumulator.append(line)
        return
    if len(line) <= column:
        accumulator.append(line)
        return
    index_of_blank = line.rfind(' ', 0, column + 1)
    if index_of_blank >= 0:
        split = index_of_blank
        offset = 1
    else:
        split = column
        offset = 0
    accumulator.append(line[:split])
    accumulator.append('\n')
    _wrap_tail_recursive_function(line[split + offset:], column, accumulator)


def wrap_loop(line: str, column: int) -> str:
    if column <= 0:
        return line
    if len(line) <= column:
        return line
    accumulator = ''
    remaining_line = line
    while len(remaining_line) > column:
        index_of_blank = remaining_line.rfind(' ', 0, column + 1)
        if index_of_blank >= 0:
            split = index_of_blank
            offset = 1
        else:
            split = column
            offset = 0
        accumulator += remaining_line[:split] + '\n'
        remaining_line = remaining_line[split + offset:]
    accumulator += remaining_line
    return accumulator
