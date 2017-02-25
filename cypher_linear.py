from string import ascii_lowercase


def encode(message, shift=4):
    """
    Caesars cypher encoder with linear implementation
    Arguments:
        message: string to encode
        shift: encrypting key
    Returns:
        encoded string
    """
    alpha = ascii_lowercase  # abcd...
    shifted = alpha[shift:] + alpha[:shift]  # efghi...
    encoded_message = []
    for letter in message:
        if letter in alpha:
            index = alpha.index(letter)  # get letter position in alphabet
            encoded_letter = shifted[index]  # get encoded letter by same index
            encoded_message.append(encoded_letter)  # add encoded letter to message
        else:
            # if we can't encode letter, save the original one
            # this ensures that we will not lose any data
            encoded_message.append(letter)  # add encoded letter to message
    return ''.join(encoded_message)  # compress encoded letters to string


def decode(message, shift=4):
    """
    Caesars cypher decoder
    Decoding message is basically encoding with negative shift
    Arguments:
        message: string to decode
        shift: encrypting key
    Returns:
        decoded string
    """
    return encode(message, -shift)


# tests
print(encode('Hello'))
print(encode('how are you?'))
print(encode('Ten-letter shift', 10))

msg = 'Secret love message'
print(decode(encode(msg)) == msg)
