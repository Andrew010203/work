from b_m.pdf_to_dict import ReadPdf


class TestReadPdf:

    def test_pdf_to_dict(self, pdf_to_dict):
        self.pdf_reader = ReadPdf(pdf_to_dict)
        result = self.pdf_reader.pdf_to_dict(pdf_to_dict)
        assert isinstance(result, dict)  # Проверяем, что результат — это словарь