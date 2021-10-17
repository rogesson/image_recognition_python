# Reconhecimento de Imagem
Trabalho de reconhecimento de imagem para o curso de Engenharia de Software - FIAP

# Linguagem de programação
Python 3.7

# Instalação no Linux

# Python 3.7
$ sudo apt-get update
$ sudo apt-get install python3.7

# Instalação Tesseract OCR
$ sudo apt-get install tesseract-ocr
$ sudo apt-get install tesseract-ocr-por

# Instalação plugin OpenCV e Pytesseract
$ pip install cv2
$ pip install --no-binary :all: opencv-python
$ pip install pytesseract

# Execução do script
$ python script.py img.png
$ python script.py img2.jpg
$ python script.py img3.jpg


# Detalhamento
Esse trabalho tem o intúito de ler um comprovante fiscal a marca DEALERNET.

O script criado na Linguagem de programação Python faz a leitura do comprovante
fiscal e lista informações como: estabelecimento, endereço, CNPJ, dados do
consumidor, produtos e valor total.

O script além de exibir na tela os dados, também captura em variáveis para que
sejam trabalhados, como o valor total ou a forma de pagamento utilizada.

# Descrição
1. Leitura da imagem com CV2
2. Alteração da cor de fundo para cinza
3. Redimencionamento da imagem no eixo vertical e horizontal em 2x
4. Opcional (exibição da imagem)
5. Configurações:
  oem 3 = (OCR Engine modes) valor 3 para utilizar o padrão
  psm 6 = (Page segmentation modes) valor 7 para assumir um único bloco de texto uniforme
  output_type = dict: Leitura da imagem e transformação em uma lista (array)
  lang = por: Dicionário em Português para palavras com acento
6. A função 'find_text': procura uma palavra na lista de palavras e retorna a posição correspondente

