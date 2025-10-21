commit
import subprocess
import os

#Configuração dos Arquivos
nome_arquivo_hashes = "hashes.txt"
nome_arquivo_wordlist = "wordlist.txt"

# Função para Executar o John the Ripper (JTR)
def executar_john(modo, arquivo_hashes, wordlist=None):
    """Executa o John the Ripper com os argumentos fornecidos."""
    comando = ["john", arquivo_hashes]
    
    if modo == "crack":
        print(f"\n[INFO] Tentando quebrar hashes usando o modo wordlist com {nome_arquivo_wordlist}...")
        # Adicionando a wordlist ao comando
        comando.extend(["--wordlist=" + wordlist])
        
    elif modo == "show":
        print("\n[INFO] Mostrando os resultados quebrados...")
        # Adicionando --show para ver os resultados
        comando.extend(["--show"])

    try:
        # Executa o comando. 'text=True' garante que a saída seja string.
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            # Não usamos check=True, pois o JTR pode retornar um código de erro que não é falha (ex: não há mais hashes)
            check=False 
        )
        
        # A saída padrão (stdout) contendo as informações que queremos
        print("\n--- SAÍDA DO JOHN THE RIPPER ---")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n--- ERROS OU AVISOS DO JOHN THE RIPPER (Stderr) ---")
            print(resultado.stderr)
            
    except FileNotFoundError:
        print("\n[ERRO] O John the Ripper (comando 'john') não foi encontrado.")
        print("Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao executar o John the Ripper: {e}")

# -Execução principal da descriptografia
if __name__ == "__main__":
    if not os.path.exists(nome_arquivo_hashes) or not os.path.exists(nome_arquivo_wordlist):
        print(f"[ERRO] Arquivos necessários não encontrados: {nome_arquivo_hashes} e {nome_arquivo_wordlist}.")
        print("Execute primeiro o script 'cria_hashes.py'.")
    else:
        # Tentar quebrar os hashes
        executar_john("crack", nome_arquivo_hashes, nome_arquivo_wordlist)
        
        # Mostrar os hashes quebrados
        executar_john("show", nome_arquivo_hashes)
        
        print("\n[FIM] Execução concluída.")