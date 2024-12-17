# write your solution here
def matrix_sum():

    total = 0

    with open("matrix.txt") as new_file:
        for line in new_file:
            numbers = line.strip().split(',')
            total += sum(int(num) for num in numbers)

    return total
    

def matrix_max():
    
    max_val = 0

    with open('matrix.txt') as new_file:
        for line in new_file:
            numbers = line.strip().split(',')
            for i in numbers:
                if int(i) > max_val:
                    max_val = int(i)
    
    return max_val


def row_sums():

    row_sum = []

    with open ('matrix.txt') as new_file:
        for line in new_file:
            numbers = line.strip().split(',')
            sum_row = sum(int(num) for num in numbers)
            row_sum.append(sum_row)
    return row_sum

if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()
    