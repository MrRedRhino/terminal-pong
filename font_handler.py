import font


def get_char(chars):
    outputs = ['', '', '', '', '']
    for char in chars:
        for x in range(5):
            outputs[x] += font.characters[char][x]
    return outputs
