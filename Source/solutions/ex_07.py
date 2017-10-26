def print_reverse(text):
    counter = len(text)-1
    word = []
    while counter >= 0:
        # print(text[counter])
        word.append(text[counter])
        counter -= 1
    sign = ''
    print sign.join(word)
string = input('String: ')
print_reverse(string)
