# python3

import sys
import threading


def compute_height(n, parents, augstums):
    # Write this function
    # Your code here
    path_lengths = [0] * n
    visited = [False] * n

    for node in range(n):
        if not visited[node]:
            visited[node] = True
            path_lengths[node] += 1
            previous = [node]
            current = parents[node]
            while current != -1:
                parent = parents[current]
                if not visited[current]:
                    previous.append(current)
                    for n in previous:
                        path_lengths[n] += 1
                    visited[current] = True
                    current = parent
                else:
                    for n in previous:
                        path_lengths[n] += path_lengths[current]
                    break

    max_lenght = 0
    for l in path_lengths:
        if l > max_lenght:
            max = l 

    return max


def main():
    inp = input().strip()
    if inp.lower() == "I":
        n = int(input().strip())
        input_parents = input().strip().split()
        parents = [int(x) for x in input_parents]
        result = compute_height(n, parents)
        print(result)
    elif inp.lower() == "F":
        file = input().strip()
        if not "a" in file.lower():
            with open(file, "r") as f:
                n = int(f.readline().strip())
                input_parents = f.readline().strip().split()
                parents = [int(x) for x in input_parents]
                result = compute_height(n, parents)
                print(result)
    else:
        print("nepareizi")


if __name__ == '_main_':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
main()
