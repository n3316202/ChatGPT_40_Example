# while_over100_break.py

def main():
    i = 1
    sum = 0    
    while True:
        sum = sum + i
        if sum > 100:
            print(i, "더했을 때의 합", sum, end = ' ')
            break
        i = i + 1

main()
