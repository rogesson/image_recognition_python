import cv2
import sys
import pytesseract
import re

def read_image(img_name):
    img_name = sys.argv[1]

    img = cv2.imread(img_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'

    threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    details = pytesseract.image_to_data(threshold_img, output_type='dict', config=custom_config, lang='por')
    text = details['text']

    text = list(map(str.upper, text))

    text = list(filter(None, text))
    clean_text = []
    dup_text = text.copy()
    for t in dup_text:
        splited = t.split(sep=':')
        if len(splited) > 1:
            for w in splited:
                text.append(w)

    #QTD
    #r = re.compile("*.UN")
    #xx = list(filter(r.match, text))
    #print(xx)

    return text

def payment(text):
    if 'DINHEIRO' in text:
        return 'DINHEIRO'

def find_text(word):
    try:
        word = word.upper()
        return text.index(word)
    except ValueError:
        None

def item(text):
    index = find_text('001')
    if index:
        return text[index:index+3]

def item_detail(item):
    if item:
        print('items:')
        print('item: %s - código: %s - descrição: %s' % (item[0], item[1], item[2]))

def establishment(text):
    index = find_text('DEALERNET')
    if index:
        return ' '.join(text[:index])

def location(text):
    index = find_text('DEALERNET')
    if index:
        index_end = text.index('-')
        number = text[index_end:index_end + 3]
        return ' '.join(text[index +1:index_end]) + ' ' + ' '.join(number)

def cnpj(text):
    index = find_text('CNPJ')
    if index:
        index_end = text.index('UR:SA')
        return ''.join(text[index +1:index_end -1])

if __name__ == "__main__":
    img_name = sys.argv[1]

    text = read_image(img_name)

    print(text)
    print('---------------')
    total = find_text('total')
    customer = find_text('consumidor')
    payment = payment(text)
    item = item(text)
    #qtd = find_text('un')
    print('Estabelecimento: %s' % establishment(text))
    print('Endereço: %s' % location(text))
    print('CNPJ: %s' % cnpj(text))
    print('Consumidor %s' % customer)
    print('Valor total: %s' % total)
    print('Forma de pagamento: %s' % payment)
    item_detail(item)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

#cv2.imshow('threshold image', threshold_img)
#cv2.imshow("test", img)
#image_text = pytesseract.image_to_string(thresholding, lang='por', config=custom_config)
#print(image_text)
