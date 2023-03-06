# python3

import sys
import threading

def compute_height(n, parents):
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

    max = 0
    for l in path_lengths:
        if l > max:
            max = l 

    return max


def main():
    ievade = input("").strip()
    if "i" == ievade.lower() :
        n = int(input("").strip())
        vecaki = input("").strip().split()
        parents = [int(x) for x in vecaki]
        try:
            result = compute_height(n, parents)
            print(result)
        except IndexError:
            print("incorrect input")
    elif "f" == ievade.lower() :
        file = input("").strip()
        if "a" in file.lower():
            print("Nepareiza faila nosaukums. Faila nosaukumā nedrīkst būt burts 'a'.")
            return
        try:
            file = open("./test/" + file, mode="r")
            lines = file.readlines()
            n = int(lines[0])
            parents = lines[1].split()
            parents = [int(x) for x in parents]
            result = compute_height(n, parents)
            print(result)
        except FileNotFoundError as e:
            print(e)
    else:
        print("nepareizi")

if __name__ == '_main_':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
main()
