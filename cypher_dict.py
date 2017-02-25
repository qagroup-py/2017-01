from string import ascii_lowercase


def encode(message, shift=4):
    """
    Caesars cypher encoder with dict implementation
    Arguments:
        message: string to encode
        shift: encrypting key
    Returns:
        encoded string
    """
    alpha = ascii_lowercase  # letters that will be encoded
    shifted = alpha[shift:] + alpha[:shift]  # letter pairs
    # dictionary that handles original letter -> encoded letter relation
    encoder = dict(zip(alpha, shifted))
    encoded_message = []
    for letter in message:
        if letter in encoder:
            # if we have corresponding letters, get encoded one
            encoded_letter = encoder[letter]
        else:
            # if not, use original one to preserve all data
            encoded_letter = letter

        # All if/else clause can be changed to
        # encoded_letter = encoder.get(letter, letter)

        encoded_message.append(encoded_letter)
    return ''.join(encoded_message)  # compress letters to string


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
