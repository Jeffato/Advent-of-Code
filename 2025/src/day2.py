'''

Input: Range of IDs on one line separated by commas
 - FirstID-LastID
 - Invalid IDs are sequences of digits repeated twice
    -Ex: 55, 6464, 123123 are invalid
 - No leading zeroes

Part One: Find the sum of all invalid IDs
'''

from pathlib import Path

class DayTwo:
    dir = Path(__file__).resolve().parent.parent / "tests"
    test = "day2_test.txt" 
    input = "day2_input.txt"

    def partOne(filepath):

        with open(filepath, 'r') as file:
            input = file.readline()
            id_lists = [id_range.split('-') for id_range in input.split(',')]

            for start, end in id_lists:
                for id in range(int(start), int(end) + 1):
                    pass
            
            return id_lists 

        
    partOne(dir/test) 