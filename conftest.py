import pytest
import os


@pytest.fixture(scope="function")
def pdf_to_dict():
    base_path = os.path.dirname(__file__)  # Получаем директорию текущего файла
    pdf_path = os.path.join(base_path, 'test_task.pdf')  # Указываем путь к pdf файлу
    return pdf_path  # Возвращаем путь к файлу
