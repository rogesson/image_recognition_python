import cv2
import sys
import pytesseract

img = cv2.imread('img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
custom_config = r'--oem 3 --psm 6'

threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
details = pytesseract.image_to_data(threshold_img, output_type='dict', config=custom_config, lang='por')
text = details['text']

filter('', text)
print(text)

cv2.waitKey(0)

cv2.destroyAllWindows()

#cv2.imshow('threshold image', threshold_img)
#cv2.imshow("test", img)
#image_text = pytesseract.image_to_string(thresholding, lang='por', config=custom_config)
#print(image_text)
