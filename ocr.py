import pytesseract
from PIL import Image

if __name__ == '__main__':
    bin_text = Image.open('input_image_thru_g_translate.jpg')
    print(pytesseract.image_to_string(bin_text, lang='eng', config='-c tessedit_char_whitelist=01'))
