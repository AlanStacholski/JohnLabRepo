import subprocess
import os
import time

# Configuração dos Arquivos
NOME_WORDLIST = "wordlist.txt"
ARQUIVOS_HASHES = [
    "hashes_bcrypt_low.txt",
    "hashes_bcrypt_high.txt",
    "hashes_md5.txt"
]
ARQUIVO_POT = "~/.john/john.pot" # Local padrão do JTR no Linux

def executar_john(modo, arquivo_hashes, wordlist=None, regras=None):
    """Executa o John the Ripper com argumentos, mede o tempo e trata a saída."""
    
    comando = ["john", arquivo_hashes]
    
    if modo == "crack":
        print(f"\n{'='*50}\n[INFO] Iniciando ataque contra {arquivo_hashes}...")
        
        if regras:
            print(f"[INFO] Usando Modo Híbrido: Wordlist + Regras '{regras}'...")
            comando.extend(["--wordlist=" + wordlist, f"--rules={regras}"])
        else:
            print(f"[INFO] Usando Modo Dicionário (Wordlist simples) com {wordlist}...")
            comando.extend(["--wordlist=" + wordlist])
        
    elif modo == "show":
        print(f"\n[INFO] Mostrando resultados quebrados para {arquivo_hashes}...")
        comando.extend(["--show"])

    # Medição de Tempo
    inicio = time.time()
    
    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            check=False 
        )
        
        fim = time.time()
        tempo_execucao = fim - inicio
        
        # Impressão de Resultados
        if modo == "crack":
            print(f"\n[TEMPO] Quebra de {arquivo_hashes} levou {tempo_execucao:.2f} segundos.")
            # O JTR costuma imprimir o resultado final aqui, então imprimimos a saída padrão
            print(resultado.stdout) 
        elif modo == "show":
            print("\n--- SENHAS DESCOBERTAS ---")
            # Filtra a saída para mostrar apenas o que foi quebrado e não a parte do 'session ended'
            linhas_uteis = [line for line in resultado.stdout.splitlines() if not line.startswith("0 password hashes") and not line.startswith("Use the 'show'") and line.strip()]
            print('\n'.join(linhas_uteis))

        if resultado.stderr and "No password hashes cracked" not in resultado.stderr:
            print("\n--- ERROS OU AVISOS DO JOHN THE RIPPER (Stderr) ---")
            print(resultado.stderr)
            
    except FileNotFoundError:
        print("\n[ERRO] O John the Ripper ('john') não foi encontrado. Instale-o com 'sudo apt install john -y'.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao executar o John the Ripper: {e}")

def limpar_john_pot():
    """Remove o arquivo john.pot para resetar a sessão do John."""
    caminho_pot = os.path.expanduser(ARQUIVO_POT)
    try:
        if os.path.exists(caminho_pot):
            print(f"\n[LIMPEZA] Removendo arquivo de pot ({caminho_pot}) para resetar...")
            os.remove(caminho_pot)
        else:
            print(f"\n[LIMPEZA] Arquivo de pot não encontrado em {caminho_pot}. Continuando...")
    except Exception as e:
        print(f"\n[ERRO] Falha ao limpar o arquivo de pot: {e}")

# Execução principal
if __name__ == "__main__":
    if not all(os.path.exists(f) for f in ARQUIVOS_HASHES) or not os.path.exists(NOME_WORDLIST):
        print(f"[ERRO] Arquivos de hashes/wordlist necessários não encontrados.")
        print("Execute primeiro o script 'criar_hashes.py' para gerar todos os arquivos.")
    else:
        # Garante que o John comece com a memória limpa de senhas quebradas
        limpar_john_pot()

        # 1. Quebra de MD5 (Para demonstrar a velocidade)
        executar_john("crack", "hashes_md5.txt", NOME_WORDLIST)
        
        # 2. Quebra de BCrypt (Custo Baixo) - Dicionário Simples
        executar_john("crack", "hashes_bcrypt_low.txt", NOME_WORDLIST)
        
        # 3. Quebra de BCrypt (Custo Alto) - Ataque Híbrido com Regras
        # (O ataque com 'all' ou 'KoreLogic' tenta variações da wordlist - e.g., 'admin' -> 'Admin1')
        print("### ATENÇÃO: Executando ataque com regras (mais lento, mais completo)")

        # Usamos o arquivo de custo alto, para simular uma quebra mais demorada e real
        executar_john("crack", "hashes_bcrypt_high.txt", NOME_WORDLIST, regras="all")
        
        # 4. Mostrar os resultados consolidados
        # John the Ripper armazena todos os resultados no mesmo arquivo .pot
        executar_john("show", "hashes_bcrypt_low.txt")
        
        print("\n[FIM] Execução concluída. Limpe o diretório e o arquivo .pot para começar de novo.")