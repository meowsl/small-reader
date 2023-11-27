import os, sys, fitz, pytesseract, io
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from typing import Tuple
from PIL import Image
import config

def extract_img(bytelist):
    '''
    ОБРАБОТКА ТЕКСТА С PNG
    '''
    img =Image.open(io.BytesIO(bytelist)) # Открытие файла png в переменной
    text = pytesseract.image_to_string(img, lang='rus') # Конвертация в строку
    text = text.replace("\r", ' ')
    text = text.replace("\n", ' ')
    print(text)


def convert_pdf(filename):
    '''
    КОНВЕРТАЦИЯ ФАЙЛА В ПНГ ФОРМАТ
    И СОХРАНЕНИЕ В ДИРЕКТОРИИ
    '''
    reader = PdfReader(f'inputs/{filename}.pdf') # Открытие файла pdf в переменной
    count_page = reader.pages # Подсчет страниц файла
    pdffile = f"inputs/{filename}.pdf" # Путь до файла
    doc = fitz.open(pdffile)
    for i in range(len(count_page)): # Цикл для обработки всех страниц
        page = doc.load_page(i)  # number of page
        pix = page.get_pixmap() # Конвертация pdf страницы в png
        byt = pix.tobytes(output='png')
        extract_img(byt) # Вызов функции

    doc.close()

if __name__ == "__main__":
    '''
    Запуск программы
    '''
    pytesseract.pytesseract.tesseract_cmd = config.pytesseract_path
    file = input() # указание имени файла
    convert_pdf(file)