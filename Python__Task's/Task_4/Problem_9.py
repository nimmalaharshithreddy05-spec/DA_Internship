def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]




if __name__ == '_main_':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
#https://www.hackerrank.com/challenges/python-mutations/problem