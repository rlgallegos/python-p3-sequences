#!/usr/bin/env python3

def print_fibonacci(length):
    if not length:
        print([])
    elif length == 1:
        print([0])
    else:
        sequence = [0, 1]
        for i in range(length - 2):
            new_number = sequence[i] + sequence[i + 1]
            sequence.append(new_number)
        print(sequence)
