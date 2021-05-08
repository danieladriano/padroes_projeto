public class CsvDataMiner extends DataMiner{
    @Override
    public String openFile(String path){
        System.out.println("Arquivo CSV aberto");
        return "Arquivo CSV";
    }

    @Override
    public String extractData(String file){
        return "Dados do arquivo CSV";
    }

    @Override
    public String parseData(String rawData){
        return rawData + " | Dados CSV tratados";
    }

    @Override
    public void closeFile(String file){
        System.out.println("Arquivo CSV fechado");
    }

}