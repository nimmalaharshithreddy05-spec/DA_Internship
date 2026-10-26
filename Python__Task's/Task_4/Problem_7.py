def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result

if __name__ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)
    
#https://www.hackerrank.com/challenges/python-string-split-and-join/problem