# ocr-binary-to-text

```bash
pipenv --python 3.9
# add pytesseract = "0.3.8" and Pillow = "8.3.1" to Pipfile
pipenv lock
brew install tesseract
# ocr sucks
python bin2txt.py
```

output:

```
P r o u d 
o r k   a 
t   S h o 
p i f y ! 

  P r o 
u d   t o 
  w o r k 
  a t   S 
h o p i f 
y ! 
```