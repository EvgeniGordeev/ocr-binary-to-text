if __name__ == '__main__':
    with open('voice_to_text_sanitized.txt', 'r') as file:
        data = file.read()
        for line in data.split('\n'):
            for ch in line.split(' '):
                ascii_code = int(ch, 2)
                print(chr(ascii_code), end=' ')
            print()
