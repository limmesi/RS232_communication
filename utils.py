def txt2frame(text):
    ded_text = list(text.encode('ascii'))
    framed_text = []
    for dec_char in ded_text:
        # dec to bin
        bin_char = bin(dec_char)[2:]
        # padding to 8 bits
        while len(bin_char) < 8:
            bin_char = '0' + bin_char
        # reversing MSB:LSB to LSB:MSB
        r_bin_char = bin_char[::-1]
        # append start and stop bits
        frame = '1' + r_bin_char + '00'
        framed_text.append(frame)

    return framed_text


def frames2txt(frames):
    text = ''
    for frame in frames:
        # delete start and stop bits
        r_bin_char = frame[1:-2]
        # reversing LSB:MSB to MSB:LSB
        bin_char = r_bin_char[::-1]
        # bin to dec
        dec_char = int(bin_char, 2)
        # dec to ascii character
        ascii_char = chr(dec_char)
        text += ascii_char

    return text


def swearword_check(text):
    swearword_dict = ['kwiatki', 'ziemniaki']
    lower_text = text.lower()
    splited_text = None

    for swearword in swearword_dict:
        splited_text = list(text)
        idx = start_idx = lower_text.find(swearword)

        if idx != -1:
            while idx < len(swearword) + start_idx:
                splited_text[idx] = '*'
                idx += 1

            text = ''.join(splited_text)

    checked_txt = ''.join(splited_text)
    return checked_txt
