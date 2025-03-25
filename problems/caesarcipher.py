alphabets = 'abcdefghijklmnopqrstuvwxyz'

def encode(message, shift):
    encoded_message = ''
    for char in message:
        if char in alphabets:
            index = alphabets.index(char)
            encoded_message += alphabets[(index - shift) % 26] # encoding with the left shift
        else:
            encoded_message += char
    return encoded_message

def decode(message, shift):
    decoded_message = ''
    for char in message:
        if char in alphabets:
            index = alphabets.index(char)
            decoded_message += alphabets[(index + shift) % 26] # decoding with the right shift 
        else:
            decoded_message += char
    return decoded_message


if __name__ == '__main__':
    message = input('Enter the message: ')
    op = int(input('Enter the operation \n1.encode\n2.decode\n>> '))
    shift = int(input('Enter the shift: '))
    match op:
        case 1:
            print(encode(message, shift))
        case 2:
            print(decode(message, shift))
        case _:
            print('Invalid operation')
