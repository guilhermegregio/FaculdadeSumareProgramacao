/**
 * Classe PrincipalPilha
 *
 * @author  Guilherme Mangabeira Gregio
 * @version %I%, %G%
 */
 
import javax.swing.JOptionPane;

public class PrincipalPilha
{
	/**
     * Metodo Principal
     */
	public static void main(String [] args)
	{
		Pilha p1 = new Pilha();
		int opt;
		
		do
		{
			opt = Integer.parseInt(JOptionPane.showInputDialog(null, ""
				+ "CRESDITOS:\n\n"
				+ "Autor: Guilherme Mangabeira Gregio\n"
				+ "E-mail: guilherme@gregio.net\n"
				+ "Faculdade Sumaré\n\n"
				+ "Opções\n"
				+ "1 - Inserir\n"
				+ "2 - Remover\n"
				+ "3 - Cheia\n"
				+ "4 - Vazia\n"
				+ "5 - Topo\n"
				+ "6 - Exibir\n"
				+ "7 - Sair\n"
				+ "Digite sua Opção:\n"
			+ ""));
			
			switch(opt)
			{
				case 1: inserir(p1); break;
				case 2: remover(p1); break;
				case 3: cheia(p1); break;
				case 4: vazia(p1); break;
				case 5: topo(p1); break;
				case 6: exibir(p1); break;
				case 7: 
					JOptionPane.showMessageDialog(null, "CREDITOS"
					+ "\n"
					+ "Autor: Guilherme Mangabeira Gregio\n"
					+ "E-mail: guilherme@gregio.net\n"
					+ "Faculdade Sumaré\n"
					+ "\n"
					+ ""); 
				break;
				default: JOptionPane.showMessageDialog(null, "Opção Inválida");
			}
		}while(opt != 7);
		
		/*
		System.out.println(p1.push("Guilherme"));
		System.out.println(p1.push("Mangabeira"));
		System.out.println(p1.push("Gregio"));
		System.out.println(p1.push(25));
		System.out.println(p1.push("anos"));
		System.out.println(p1.push("anos"));
		
		System.out.println(p1.pop());
		System.out.println(p1.pop());
		System.out.println(p1.pop());
		System.out.println(p1.pop());
		System.out.println(p1.pop());
		System.out.println(p1.pop());
		*/
	}
	/**
	 * Armazena valor digitado em dado e insere na pilha
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void inserir(Pilha p)
	{
		Tad pessoa = new Tad();
		
		pessoa.setId(Long.parseLong(JOptionPane.showInputDialog("Digite o id")));
		pessoa.setNome(JOptionPane.showInputDialog("Digite o nome"));
		pessoa.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Digite a idade")));
		pessoa.setCpf(JOptionPane.showInputDialog("Digite o cpf"));
		pessoa.setTelefone(JOptionPane.showInputDialog("Digite o telefone"));
		pessoa.setEmail(JOptionPane.showInputDialog("Digite o e-mail"));
		
		if(!p.push(pessoa))
			JOptionPane.showMessageDialog(null, "Pilha Cheia");
	}
	/**
	 * Remove primeiro elemento da pilha
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void remover(Pilha p)
	{
		Object dado = p.pop();
		Tad pessoa = new Tad();
		
		
		if(dado != null)
		{
			pessoa = (Tad)dado;
			JOptionPane.showMessageDialog(null, "Valor: " + lerTad(pessoa));
		}
		else
			JOptionPane.showMessageDialog(null, "Pilha Vazia");
	}
	/**
	 * Informa se a pilha está cheia
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void cheia(Pilha p)
	{
		if(!p.isFull())
			JOptionPane.showMessageDialog(null, "Pilha não está cheia.");
		else
			JOptionPane.showMessageDialog(null, "Pilha cheia.");
	}
	/**
	 * Informa se a pilha esta vazia
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void vazia(Pilha p)
	{
		if(!p.isEmpty())
			JOptionPane.showMessageDialog(null, "Pilha não está vazia.");
		else
			JOptionPane.showMessageDialog(null, "Pilha vazia.");
	}
	/**
	 * Exibe primeiro elemento da pilha
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void topo(Pilha p)
	{
		Object dado = p.pop();
		Tad pessoa = new Tad();
		
		if(dado != null)
		{
			pessoa = (Tad)dado;
			p.push(dado);
			JOptionPane.showMessageDialog(null, "Topo:\n" 
				+ lerTad(pessoa)
			+ "");
		}
		else
			JOptionPane.showMessageDialog(null, "Pilha vazia.");
	}
	/**
	 * Exibir toda a pilha
     * @param     p aponta para a pilha
	 * @see		  javax.swing.JOptionPane
     */
	public static void exibir(Pilha p)
	{
		Object dado;
		Tad pessoa = new Tad();
		
		String pilhaStr = "";
		Pilha temp = new Pilha();
		
		while(!p.isEmpty())
		{
			dado = p.pop();
			pessoa = (Tad)dado;
			temp.push(dado);
			pilhaStr += lerTad(pessoa)+"\n";
		}
		
		while(!temp.isEmpty())
			p.push(temp.pop());
		
		if(pilhaStr != "")
			JOptionPane.showMessageDialog(null, "Pilha:\n" + pilhaStr);
		else
			JOptionPane.showMessageDialog(null, "Pilha vazia.");
	}
	
	/**
	 * Exibir dados do Tad
     * @param		dado	Tipo de dado abstrato(Tad)
	 * @return		valor String do Tad
     */
	public static String lerTad(Tad dado)
	{
		return(""
			+ "Id: " + dado.getId() + "\n"
			+ "Nome: " + dado.getNome() + "\n"
			+ "Idade: " + dado.getIdade() + "\n"
			+ "Cpf: " + dado.getCpf() + "\n"
			+ "telefone: " + dado.getTelefone() + "\n"
			+ "Email: " + dado.getEmail() + "\n"
		+ "");
	}
}