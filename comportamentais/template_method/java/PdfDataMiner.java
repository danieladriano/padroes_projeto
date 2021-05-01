public class PdfDataMiner extends DataMiner{
    @Override
    public String openFile(String path){
        System.out.println("Arquivo PDF aberto");
        return "Arquivo PDF";
    }

    @Override
    public String extractData(String file){
        return "Dados do arquivo PDF";
    }

    @Override
    public String parseData(String rawData){
        return rawData + " | Dados PDF tratados";
    }

    @Override
    public void closeFile(String file){
        System.out.println("Arquivo PDF fechado");
    }

}