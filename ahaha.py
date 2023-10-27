import fitz, easyocr
from PyPDF2 import PdfReader

def extract_img(img):
    reader = easyocr.Reader(['ru'], gpu=True)
    results = reader.readtext(img, detail=0)
    print(results)

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
    print('Ввод имени файла:')
    convert_pdf(input())