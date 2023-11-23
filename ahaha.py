import fitz
import os, sys
from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_path
from typing import Tuple
from PIL import Image
import config


def extract_img(filename):
    '''
    ОБРАБОТКА ТЕКСТА С PNG
    '''
    img =Image.open(filename) # Открытие файла png в переменной
    text = pytesseract.image_to_string(img, lang='rus') # Конвертация в строку
    # Удаление лишних символов
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")

    # Тут вместо вывода текста нужно будет сделать, чтобы текст передавался в модель джанги этим я сам займусь
    print(text)
    os.remove(filename)

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
        output = f"outfile{i}.png" # Имя файла на выходе
        pix.save(output) # Сохранения png в директории
        extract_img(output) # Вызов функции

    doc.close()

if __name__ == "__main__":
    '''
    Запуск программы
    '''
    pytesseract.pytesseract.tesseract_cmd = config.pytesseract_path
    file = input() # указание имени файла
    convert_pdf(file)
