from csv_dataminer import CsvDataMiner
from pdf_dataminer import PdfDataMiner


def main(dataminer, path):
    dataminer.mine(path)

if __name__ == "__main__":
    csv = CsvDataMiner()
    main(csv, "./arquivo.csv")

    pdf = PdfDataMiner()
    main(pdf, "./arquivo.pdf")
