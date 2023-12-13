from collections import deque


def is_valid_move(matrix, visited_cells, row, col):
    return (row >= 0) and (row < len(matrix)) \
        and (col >= 0) and (col < len(matrix[0])) \
        and (matrix[row][col] == 1) and not (visited_cells[row][col])


def bfs(matrix, start_row, start_col, end_row, end_col):
    visited_cells = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    queue = deque()
    queue.append((start_row, start_col, 0))

    row_directions = [-1, 0, 0, 1]
    col_directions = [0, -1, 1, 0]

    visited_cells[start_row][start_col] = True

    while queue:
        current_row, current_col, distance = queue.popleft()

        if current_row == end_row and current_col == end_col:
            return distance

        for direction in range(4):
            if is_valid_move(matrix, visited_cells, current_row + row_directions[direction],
                             current_col + col_directions[direction]):
                visited_cells[current_row + row_directions[direction]][current_col + col_directions[direction]] = True
                queue.append(
                    (current_row + row_directions[direction], current_col + col_directions[direction], distance + 1))

    return float('inf')


def read_input_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        start_point = tuple(map(int, file.readline().strip().split(', ')))
        end_point = tuple(map(int, file.readline().strip().split(', ')))
        matrix_size = tuple(map(int, file.readline().strip().split(', ')))
        matrix = [list(map(int, file.readline().strip().split())) for _ in range(matrix_size[0])]
    return start_point, end_point, matrix


def write_output_file(file_name, min_distance):
    with open(file_name, 'w', encoding='utf-8') as file:
        if min_distance != float('inf'):
            file.write(f"Найкоротший шлях має довжину {min_distance}")
        else:
            file.write("Шляху не існує")


def main():
    start_point, end_point, matrix = read_input_file('../input.txt')
    min_distance = bfs(matrix, *start_point, *end_point)
    write_output_file('../output.txt', min_distance)


if __name__ == "__main__":
    main()
