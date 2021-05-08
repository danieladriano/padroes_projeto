from dataminer import DataMiner


class PdfDataMiner(DataMiner):
    def open_file(self, path):
        print("Arquivo PDF aberto")
        return "Arquivo PDF"

    def extract_data(self, file):
        return "Dados do arquivo PDF"

    def parse_data(self, raw_data):
        return raw_data + " | Dados PDF tratados"

    def close_file(self, file):
        print("Arquivo PDF fechado")
