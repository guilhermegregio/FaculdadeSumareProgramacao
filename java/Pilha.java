/**
 * Classe Pilha
 *
 * @author  Guilherme Mangabeira Gregio
 * @version 1.0
 */
public class Pilha
{
	private int topo;
	private Object [] vetor;
	
	/**
     * Contrutor padr�o
	 * Seta topo como zero 0;
	 * E vetor com tamanho 5;
     */
	public Pilha()
	{
		topo = 0;
		vetor = new Object[5];
	}
	
	/**
     * Contrutor com parametro de tamanho da pilha
     * @param     tam inteiro com o tamanho da pilha (vetor).
     */
	public Pilha(int tam)
	{
		topo = 0;
		vetor = new Object[tam];
	}
	
	/**
     * Insere um valor na pilha
	 * Retorna um valor booleano:
     * True se inserir dado na pilha com sucesso;
	 * False se pilha estiver cheia;
     * @param     dado Objeto pois pode receber qualquer coisa (Inclusive TDA).
     * @return    boolean.
     */
	public boolean push(Object dado)
	{
		if(!isFull())
		{
			vetor[topo++] = dado;
			return true;
		}
		return false;
	}
	
	/**
     * Retira o primeiro item da pilha
	 * Retorna um objeto:
     * Caso a pilha esteja vazia retorna false;
	 * Sen�o retorna um objeto
     * @return    objeto.
     */
	public Object pop()
	{
		if(!isEmpty())
			return vetor[--topo];
		return null;
	}
	
	/**
     * Verifica se a pilha esta cheia:
	 * Retorna um valor boleano:
     * True se pilha cheia;
	 * False se pilha n�o estiver cheia;
     * @return    boolean.
     */
	public boolean isFull()
	{
		return topo == vetor.length ? true : false;
	}
	
	/**
     * Verifica se a pilha esta vazia:
     * Retorna um valor boleano:
	 * True se estiver vazia;
	 * False se n�o estiver vazia;
     * @return    boolean.
     */
	public boolean isEmpty()
	{
		return topo == 0 ? true : false;
	}
}