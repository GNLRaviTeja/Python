# TASK1:
def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

for i in range(1,10):
    print(mult3(i))

#TASK2:
def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)

#TASK3:
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))	
