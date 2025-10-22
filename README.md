# 🔐 Projeto Hash Cracker - Laboratório Educacional

Projeto de automação em laboratório utilizando John the Ripper para demonstração de criptografia (BCrypt e MD5) e quebra de senhas simples para fins **estritamente didáticos**.

## 📋 Descrição

Este projeto automatiza o processo de:
1. **Criação de hashes** de senhas usando algoritmos BCrypt e MD5
2. **Geração de wordlist** com senhas conhecidas
3. **Quebra de hashes** utilizando John the Ripper com ataque de dicionário

> ⚠️ **AVISO IMPORTANTE**: Este projeto é destinado exclusivamente para fins educacionais em ambientes controlados de laboratório. Nunca utilize estas técnicas em sistemas sem autorização explícita.

## 🎯 Objetivos Educacionais

- Compreender como funcionam algoritmos de hash (BCrypt e MD5)
- Demonstrar a importância de senhas fortes
- Aprender sobre ferramentas de segurança ofensiva
- Praticar automação com Python

## 🖥️ Requisitos do Sistema

### Sistema Operacional
- **Linux** (Recomendado: Ubuntu 20.04 ou superior)
- Sugestão: Utilize uma **máquina virtual** para isolamento do ambiente

### Dependências Necessárias

#### 1. Python 3
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### 2. Biblioteca BCrypt
```bash
pip3 install bcrypt
```

#### 3. John the Ripper
```bash
sudo apt install john -y
```

Para verificar a instalação:
```bash
john --version
```

## 📁 Estrutura do Projeto

```
.
├── criar_hashes.py      # Script para gerar hashes e wordlist
├── quebra_hashes.py     # Script para quebrar os hashes
├── hashes.txt          # Arquivo gerado com os hashes (formato JTR)
├── wordlist.txt        # Arquivo gerado com as senhas
└── README.md           # Este arquivo
```

## 🚀 Como Utilizar

### Passo 0: Preparar o Ambiente

**IMPORTANTE**: Execute os scripts no **terminal Linux** dentro do diretório do projeto.

Navegue até o diretório onde os scripts estão localizados:
```bash
cd /caminho/para/o/projeto
```

Certifique-se de que você está no diretório correto:
```bash
pwd
ls -l
```

### Passo 1: Gerar os Hashes e Wordlist

Execute o script de criação no terminal:
```bash
python3 criar_hashes.py
```

Este script irá:
- Criar hashes BCrypt de 5 senhas simples
- Gerar hashes MD5 das mesmas senhas (para comparação)
- Salvar os hashes no formato John the Ripper em `hashes.txt`
- Criar uma wordlist em `wordlist.txt`

### Passo 2: Quebrar os Hashes

Execute o script de quebra no terminal:
```bash
python3 quebra_hashes.py
```

Este script irá:
- Utilizar o John the Ripper para atacar os hashes
- Usar a wordlist gerada como dicionário
- Exibir os resultados das senhas descobertas

## 📊 Senhas Utilizadas (Exemplo)

O projeto utiliza senhas **intencionalmente fracas** para demonstração:
- senha123
- john123
- admin
- teste
- password

## 🔍 Entendendo os Algoritmos

### BCrypt
- Algoritmo de hash **lento** e seguro
- Utiliza **salt** para proteção contra rainbow tables
- **Custo configurável** (rounds) - neste projeto usa rounds=4 para acelerar
- Recomendado para armazenamento de senhas

### MD5
- Algoritmo de hash **rápido** (considerado inseguro)
- Sem salt por padrão
- Vulnerável a ataques de força bruta
- **Não recomendado** para senhas atualmente

## 🛡️ Considerações de Segurança

### Boas Práticas Demonstradas:
✅ Uso de BCrypt com salt  
✅ Isolamento em ambiente de teste  
✅ Código educacional bem documentado  

### Lições Aprendidas:
⚠️ Senhas simples são quebradas rapidamente  
⚠️ MD5 não deve ser usado para senhas  
⚠️ A complexidade da senha é fundamental  

## 📚 Recursos Adicionais

- [Documentação BCrypt](https://pypi.org/project/bcrypt/)
- [John the Ripper Wiki](https://www.openwall.com/john/)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetsproject.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

## ⚖️ Aspectos Legais e Éticos

Este projeto deve ser utilizado apenas em:
- Ambientes de laboratório pessoal
- Sistemas que você possui ou tem autorização explícita
- Contextos educacionais supervisionados

**Uso não autorizado de ferramentas de quebra de senha é ilegal e antiético.**

## 🤝 Contribuições

Sugestões de melhorias são bem-vindas! Este é um projeto educacional em constante evolução.

## 📝 Licença

Projeto desenvolvido para fins educacionais. Use com responsabilidade.

---

**Desenvolvido para aprendizado em Segurança da Informação e Criptografia**
