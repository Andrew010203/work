import os
import pypdf

base_path = os.path.dirname(__file__)
pdf_path = os.path.join(base_path, 'test_task.pdf')


class ReadPdf:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def pdf_to_dict(self, pdf_path):
        """Метод, считывающий данные из pdf
        файла и возвращающий данные в виде словаря"""
        pdf_dict = {}

        with open(pdf_path, 'rb') as data_pdf:  # Открываем файл в бинарном режиме
            reader = pypdf.PdfReader(data_pdf)  # Создаем объект PdfReader для чтения содержимого pdf файла
            for page_num in range(len(reader.pages)):  # Итерируемся по всем страницам в pdf файле
                page = reader.pages[page_num]  # Получаем текущую страницу по номеру (page_num)
                pdf_dict[page_num + 1] = page.extract_text()  # Извлекаем текст и сохраняем в словаре
        print(pdf_dict)
        print(type(pdf_dict))  # Убеждаемся, что тип данных это словарь
        return pdf_dict