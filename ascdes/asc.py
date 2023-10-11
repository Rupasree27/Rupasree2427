numbers = []
words = []

while True:
    user_input = input("Enter a number or a word (0 or END to stop): ")
    
    if user_input == '0':
        break
    elif user_input == 'END':
        break
    elif user_input.isnumeric():
        numbers.append(int(user_input))
    else:
        words.append(user_input)

if numbers:
    print("Numbers in ascending order:", sorted(numbers))
    print("Numbers in descending order:", sorted(numbers, reverse=True))

if words:
    print("Words in ascending order:", sorted(words))
    print("Words in descending order:", sorted(words, reverse=True))
