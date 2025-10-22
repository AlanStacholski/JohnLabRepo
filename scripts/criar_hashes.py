import bcrypt
import hashlib
import os

# Definindo senhas simples
senhas_simples = [
    "senha123",
    "john123",
    "admin",
    "teste",
    "password"
]

# Configuração dos nomes de arquivos
NOME_WORDLIST = "wordlist.txt"
NOME_BCRYPT_LOW = "hashes_bcrypt_low.txt"  # Cost = 4 (Rápido, para demonstração)
NOME_BCRYPT_HIGH = "hashes_bcrypt_high.txt" # Cost = 10 (Lento, para comparação)
NOME_MD5 = "hashes_md5.txt" # MD5 (Inseguro, para comparação de velocidade)

def gerar_hashes_e_wordlist():
    """Gera wordlist e múltiplos arquivos de hash para diferentes cenários."""
    try:
        with open(NOME_WORDLIST, 'w') as f_wordlist, \
             open(NOME_BCRYPT_LOW, 'w') as f_bcrypt_low, \
             open(NOME_BCRYPT_HIGH, 'w') as f_bcrypt_high, \
             open(NOME_MD5, 'w') as f_md5:
            
            print("Iniciando a criação de hashes e wordlist...")

            for i, senha in enumerate(senhas_simples):
                senha_bytes = senha.encode('utf-8')
                usuario = f"usuario{i + 1}"

                # 1. BCrypt - Custo Baixo (rounds=4)
                salt_low = bcrypt.gensalt(rounds=4) 
                hash_bcrypt_low = bcrypt.hashpw(senha_bytes, salt_low).decode('utf-8')
                f_bcrypt_low.write(f"{usuario}:{hash_bcrypt_low}\n")
                
                # 2. BCrypt - Custo Alto (rounds=10)
                salt_high = bcrypt.gensalt(rounds=10)
                hash_bcrypt_high = bcrypt.hashpw(senha_bytes, salt_high).decode('utf-8')
                f_bcrypt_high.write(f"{usuario}:{hash_bcrypt_high}\n")

                # 3. MD5 Puro (Inseguro)
                hash_md5 = hashlib.md5(senha_bytes).hexdigest()
                # O John the Ripper (JTR) pode identificar o hash MD5 puro sem prefixo
                f_md5.write(f"{usuario}:{hash_md5}\n") 

                # 4. Wordlist
                f_wordlist.write(f"{senha}\n")
                
                print(f"Gerado {usuario}: BCrypt(4)={hash_bcrypt_low[:10]}... | BCrypt(10)={hash_bcrypt_high[:10]}... | MD5={hash_md5}")

        print(f"\n[SUCESSO] Wordlist criada: {NOME_WORDLIST}")
        print(f"[SUCESSO] Hashes BCrypt (Custo Baixo) criados: {NOME_BCRYPT_LOW}")
        print(f"[SUCESSO] Hashes BCrypt (Custo Alto) criados: {NOME_BCRYPT_HIGH}")
        print(f"[SUCESSO] Hashes MD5 criados: {NOME_MD5}")

    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro: {e}")

if __name__ == "__main__":
    gerar_hashes_e_wordlist()