class Main {
  
  private static void dataminer(DataMiner dataminer, String path){
      dataminer.mine(path);
  }

  public static void main(String[] args) {

      CsvDataMiner csv = new CsvDataMiner();
      dataminer(csv, "./arquivo.csv");

      PdfDataMiner pdf = new PdfDataMiner();
      dataminer(pdf, "./arquivo.pdf");
  }
}