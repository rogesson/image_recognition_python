import cv2
import pytesseract

img = cv2.imread('img.png')

custom_config = r'--oem 3 --psm 6'
image_text = pytesseract.image_to_string(img, config=custom_config)

print(image_text)

# Código para deixar background cinza
#src = cv.imread("img.JPG") img = cv.cvtColor(src, cv.COLOR_BGR2GRAY) cv.imwrite("img2.JPG", img)
