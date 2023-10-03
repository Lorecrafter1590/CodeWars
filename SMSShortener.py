def shortener(message):
    while len(message) > 160 and ' ' in message:
        last_space_position = message.rfind(' ')
        message = message[:last_space_position] + message[last_space_position+1].upper() + message[last_space_position + 2:]
    return message
