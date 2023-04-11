import openpyxl
from itemadapter import ItemAdapter


class ScraperPipeline:

    def open_spider(self, spider):
        # подготовка файла xls для записи
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['Name', 'Price'])

        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.ws.append([adapter.get('Name'), adapter.get('Price')])
        return item
    
    def close_spider(self, spider):
        self.wb.save('data.xls')
