import fitz
import os, sys
from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_path
from typing import Tuple
from PIL import Image
import config


def extract_img(filename):
    img =Image.open(filename)
    text = pytesseract.image_to_string(img, lang='rus')
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    print(text)
    os.remove(filename)

def convert_pdf(filename):
    reader = PdfReader(f'inputs/{filename}.pdf')
    count_page = reader.pages

    pdffile = f"inputs/{filename}.pdf"
    doc = fitz.open(pdffile)
    for i in range(len(count_page)):
        page = doc.load_page(i)  # number of page
        pix = page.get_pixmap()
        output = f"outfile{i}.png"
        pix.save(output)
        extract_img(output)

    doc.close()

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = config.pytesseract_path
    file = input()
    convert_pdf(file)
