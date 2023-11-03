# while_over100.py

def main():
    i = 1
    sum = 0    
    while sum <= 100:
        sum = sum + i        
        i = i + 1
    print(i, "더했을 때의 합", sum, end = ' ')

main()
