'''
Input: txt file
 -Each line has L/R and a # representing a rotation on a dial
    -L -> move down the dial
    -R -> move up the dial
    -# -> number, can be big

Dial Features
 - Starts from 0 and goes to 99. Loops back to 0 from 99
 - Intial value is 50

Part 1 Output: # of times dial lands on 0 after a completed rotation step

Part 2 Output: # of times dial passes 0
'''
from pathlib import Path

class DayOne:
    dir = Path(__file__).resolve().parent.parent / "tests"
    test = "day1_test.txt" 
    input = "day1_input.txt"

    def part1(filepath):
        dial_val = 50
        counter = 0

        with open(filepath, 'r') as file:
            for line in file:
                rotation = int(line.strip()[1:])
                if line[0] == 'L': rotation *= -1

                dial_val += rotation

                while dial_val > 99:
                    dial_val -= 100

                while dial_val < 0:
                    dial_val += 100
                
                if dial_val == 0:
                    counter += 1
            
            return counter
        
    def part2(filepath):
        dial_val = 50
        counter = 0

        with open(filepath, 'r') as file:
            for line in file:
                rotation = int(line.strip()[1:])
                if line[0] == 'L': rotation *= -1

                dial_val += rotation

                if dial_val % 100 == 0:
                    counter += 1

                while dial_val > 99:
                    dial_val -= 100
                    counter += 1

                while dial_val < 0:
                    dial_val += 100
                    counter += 1

            return counter

    # print(f'Part1 test: {part1(dir/test)}')
    # print(f'Part1 input: {part1(dir/input)}')
    print(f'Part2 test: {part2(dir/test)}')
    print(f'Part2 input: {part2(dir/input)}')