# small-reader

<h4>Реализовано: </h4>
<ul>
  <li>reader.py - быстрая конвертация из печатного текста (не работает с изображениями/сканами)</li>
  <li>ahaha.py - приемлемо обрабатывает любой пдф файл и корректно выводит текст. </li>
</ul>

### Установка
~~~
https://github.com/UB-Mannheim/tesseract/wiki
~~~
~~~
git clone https://github.com/meowsl/hack-django

python -m venv .venv
pip install -r requirements.txt
~~~

<h5> Далее необходимо создать config.py и присвоить в нем переменной pytesseract_path путь до tesseract. </h5>
