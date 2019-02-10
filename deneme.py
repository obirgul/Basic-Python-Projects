def split_and_join(x):
    print('-'.join(input().split()))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)