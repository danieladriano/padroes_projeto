import abc

class DataMiner():
    def mine(self, path):
        file = self.open_file(path)
        raw_data = self.extract_data(file)
        data = self.parse_data(raw_data)
        analysis = self.analyse_data(data)
        self.send_report(analysis)
        self.close_file(file)

    @abc.abstractmethod
    def open_file(self, path):
        pass

    @abc.abstractmethod
    def extract_data(self, file):
        pass

    @abc.abstractmethod
    def parse_data(self, raw_data):
        pass

    @abc.abstractmethod
    def close_file(self, file):
        pass

    def analyse_data(self, data):
        return data + "| Dados analisados"

    def send_report(self, analysis):
        print(f"Relatorio enviado -> {analysis}")
