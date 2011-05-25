/**
 * Classe Tad
 *
 * @author  Guilherme Mangabeira Gregio
 * @version 1.0
 */
public class Tad
{
	private long id;
	private String nome;
	private int idade;
	private String cpf;
	private String telefone;
	private String email;
	
	/**
	 * Seta id
     * @param	id			long
     */
	 public void setId(long id){ this.id = id; }
	 
	 /**
	 * Seta nome
     * @param	nome		String
     */
	 public void setNome(String nome){ this.nome = nome; }
	 
	 /**
	 * Seta idade
     * @param	idade		String
     */
	 public void setIdade(int idade){ this.idade = idade; }
	 
	 /**
	 * Seta cpf
     * @param	cpf			String
     */
	 public void setCpf(String cpf){ this.cpf = cpf; }
	 
	 /**
	 * Seta telefone
     * @param	telefone	String
     */
	 public void setTelefone(String telefone){ this.telefone = telefone; }
	 
	 /**
	 * Seta email
     * @param	email		String
     */
	 public void setEmail(String email){ this.email = email; }
	 
	 /**
	 * Retorna id
     * @return	valor long id
     */
	 public long getId(){ return this.id; }
	 
	 /**
	 * Retorna nome
     * @return	valor String nome
     */
	 public String getNome(){ return this.nome; }
	 
	 /**
	 * Retorna idade
     * @return	valor int idade
     */
	 public int getIdade(){ return this.idade; }
	 
	 /**
	 * Retorna cpf
     * @return	valor String cpf
     */
	 public String getCpf(){ return this.cpf; }
	 
	 /**
	 * Retorna telefone
     * @return	valor String telefone
     */
	 public String getTelefone(){ return this.telefone; }
	 
	 /**
	 * Retorna email
     * @return	valor String email
     */
	 public String getEmail(){ return this.email; }
	 
}