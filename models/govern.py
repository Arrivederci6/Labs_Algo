"""
Module - govern.py
This module contains a functions to make a topological sort.
"""

from collections import defaultdict, deque
import os

def topological_sort(graph):
    """
    Function for topological sorting of a graph.

    Args:
        - graph (dict): A graph represented as a dictionary of adjacency lists.

    Returns:
        - list: List of nodes in topological order.

    Exception:
        - ValueError: If the graph contains a loop or some nodes are not connected to the rest of the graph.
    """
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    result = []

    while queue:
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

        result.append(current_node)

    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle or some nodes are not connected to the rest of the graph.")
    return result[::-1]

def read_input(file_path):
    """
    Function to read input data from a file.

    Args:
        - file_path (str): The path to the input file.

    Returns:
        - dict: A graph represented as a dictionary of adjacency lists.

    Exception:
        - FileNotFoundError: If the file does not exist.
        - ValueError: If the input data format is invalid.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")

    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = defaultdict(list)

        for line in lines:
            parts = line.split()
            if len(parts) != 2:
                raise ValueError("Invalid input format.")

            dependency, node = parts[1], parts[0]
            graph[dependency].append(node)

    return graph

def write_output(file_path, order):
    """
    Function to write the output data to the file.

    Args:
        - file_path (str): The path to the source file.
        - order (list): List of nodes in topological order.
    """
    with open(file_path, 'w') as file:
        for node in order:
            file.write(node + '\n')

def main():
    """
    Main function.
    """
    input_file_path = os.path.abspath('../govern.in')
    output_file_path = os.path.abspath('../govern.out')

    try:
        graph = read_input(input_file_path)
        order = topological_sort(graph)
        write_output(output_file_path, order)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
