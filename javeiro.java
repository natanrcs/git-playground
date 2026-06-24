// eu fiz uma analogia de POO com saladas e vamo meter o biruta kkkkkkkkk
public class Salada {
    //os atributos seria os ingredientes da salada kkkkkk
    // vou meter biruta encapsulando a coisa toda
    private String tipoFolha;
    private String legume;
    private String tempero;
    private String temCebola;

    public Salada (String tipoFolha,String legume,String tempero, boolean temCebola) {
    this.tipoFolha = tipoFolha
    this.legume = legume
    this.tempero = tempero
    this.temCebola = temCebola
    }
    //métodos é a açao ou comportamento 
    public void mostrarIngredientes () {
        System.out.println("mostrando os ingrediente da salada")
        System.out.println("folhas: " + this.tipoFolha)
        System.out.println("legumes: " + this.legume)
        System.out.println("temperos: " + this.tempero)
        System.out.println("tem cebola? " + this.temCebola)
    }
}

public class Main () {
    //criando o primeiro objeto que no caso é a salada com ingredientes que criam a salada 
    Salada saladaDoNatan = new Salada("rucula","tomate","azeite e sal",true);
    Salada saladaDaGabi = new Salada("alface","brocolis","vinagre e pimenta do reino",false)
    Salada saladaTradicional = new Salada("alface normal","tomate","sal",true);
    // agora  chamando a acao de mostrar a salada 
    saladaDoNatan.mostrarIngredientes()
    saladaDaGabi.mostrarIngredientes()
}