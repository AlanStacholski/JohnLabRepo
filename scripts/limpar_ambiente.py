import os
import glob

def limpar():
    arquivos_para_remover = [
        "wordlist.txt",
        "hashes_bcrypt_low.txt",
        "hashes_bcrypt_high.txt",
        "hashes_md5.txt",
        "~/.john/john.pot" 
    ]
    
    print("[LIMPEZA] Iniciando a limpeza do ambiente...")
    
    for arquivo in arquivos_para_remover:
        caminho_completo = os.path.expanduser(arquivo) # Trata o caminho do .pot
        
        if os.path.exists(caminho_completo):
            try:
                os.remove(caminho_completo)
                print(f"  [OK] Removido: {arquivo}")
            except Exception as e:
                print(f"  [ERRO] Falha ao remover {arquivo}: {e}")
        else:
            print(f"  [PULADO] Arquivo não encontrado: {arquivo}")

    # John também cria um arquivo de sessão, se quiser remover:
    for sessao in glob.glob("*.rec"):
        try:
            os.remove(sessao)
            print(f"  [OK] Removida sessão: {sessao}")
        except:
            pass

    print("\n[FIM] O ambiente está limpo e pronto para uma nova execução.")

if __name__ == "__main__":
    limpar()