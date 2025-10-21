import bcrypt
import hashlib
import os

# --- 1. Lista de Senhas Simples ---
senhas_simples = [
    "senha123",
    "john123",
    "admin",
    "teste",
    "password"
]

# --- 2. Geração de Hashes e Arquivos ---
nome_arquivo_hashes = "hashes.txt"
nome_arquivo_wordlist = "wordlist.txt"

# Abrir arquivos para escrita
try:
    with open(nome_arquivo_hashes, 'w') as f_hashes, open(nome_arquivo_wordlist, 'w') as f_wordlist:
        print("Iniciando a criação de hashes e wordlist...")

        for i, senha in enumerate(senhas_simples):
            senha_bytes = senha.encode('utf-8')

            # 2.1. Hash Bcrypt (Para ser quebrado pelo JTR)
            # Fator de custo baixo (rounds=4) para acelerar a demonstração
            salt = bcrypt.gensalt(rounds=4) 
            hash_bcrypt_completo = bcrypt.hashpw(senha_bytes, salt).decode('utf-8')

            # 2.2. Hash MD5 (Apenas para demonstração e listagem)
            hash_md5 = hashlib.md5(senha_bytes).hexdigest()

            # 2.3. Gravar Hash no Formato JTR: "username:hash"
            linha_jtr = f"usuario{i + 1}:{hash_bcrypt_completo}\n"
            f_hashes.write(linha_jtr)

            # 2.4. Gravar a senha na Wordlist
            f_wordlist.write(f"{senha}\n")
            
            print(f"Gerado: usuario{i + 1} (Bcrypt: {hash_bcrypt_completo[:10]}... | MD5: {hash_md5})")


    print(f"\n[SUCESSO] Arquivo de hashes para JTR criado: {nome_arquivo_hashes}")
    print(f"[SUCESSO] Wordlist criada: {nome_arquivo_wordlist}")

except Exception as e:
    print(f"\n[ERRO] Ocorreu um erro: {e}")