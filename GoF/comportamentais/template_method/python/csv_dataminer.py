from dataminer import DataMiner


class CsvDataMiner(DataMiner):
    def open_file(self, path):
        print("Arquivo CSV aberto")
        return "Arquivo CSV"

    def extract_data(self, file):
        return "Dados do arquivo CSV"

    def parse_data(self, raw_data):
        return raw_data + " | Dados CSV tratados"

    def close_file(self, file):
        print("Arquivo CSV fechado")
