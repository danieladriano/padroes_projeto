public abstract class DataMiner{
    public void mine(String path){
        String file = openFile(path);
        String rawData = extractData(file);
        String data = parseData(rawData);
        String analysis = analyzeData(data);
        sendReport(analysis);
        closeFile(file);
    }

    public abstract String openFile(String path);
    public abstract String extractData(String file);
    public abstract String parseData(String rawData);
    public abstract void closeFile(String file);

    public String analyzeData(String data){
        return data + " | Dados analisados";
    }

    public void sendReport(String analysis){
        System.out.println("Relatorio enviado -> " + analysis);
    }
}