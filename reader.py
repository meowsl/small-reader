from PyPDF2 import PdfReader
import re

# Переменные для обработки текста
reader = PdfReader('inputs/Pravila_vnutrennego_trudovogo_rasporyadka.pdf')
text_l = []
dirty_symbolds = "<>/.,}{[])()*&-_^%$#№!"

# Функция для очистки строки
def clear_str(text):

    result = re.sub("[^А-Яа-я0-9.,]", " ", text)
    s = re.sub(r"\s(\s)?", " ", result)
    text_l.append(s)


for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    clear_str(text)



print("\n".join(text_l) )