# task_skrapy

Парсер товаров с https://krasn.russcvet.ru/

Стек: ````Python3.10```` ````Scrapy```` ````openpyxl````

## Установка и запуск

Клонировать репозиторий с Github.com, перейти в директорию проекта  
````
git clone https://github.com/Povarenskiy/task_skrapy.git
cd task_skrapy
````

Настроить виртульаное окружение
````
python -m venv venv

venv\Scripts\activate           # on windows
source venv/bin/activate        # on linux

pip install -r requirements.txt  
````

Запустить
````
scrapy crawl category 

# По умолчанию выгружаются данные с категории эмалей "https://krasn.russcvet.ru/catalog/enamels/", однако нужную категорию можно указать # через start_url при запуске через запятую

scrapy crawl category -a start_url="https://krasn.russcvet.ru/catalog/shpatlevki/,https://krasn.russcvet.ru/catalog/laki/"
````
