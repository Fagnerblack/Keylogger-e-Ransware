🛡️ Desafio Final: Simulação e Análise de Malwares (Ransomware & Keylogger)

Este repositório contém os projetos práticos desenvolvidos como parte do Desafio Final de Simulação de Malwares, com foco na compreensão, detecção e defesa contra ameaças cibernéticas. Todos os scripts são criados exclusivamente para fins educacionais e devem ser executados apenas em ambientes controlados (sandboxing).

🎯 Objetivos do Projeto

Compreender o funcionamento prático de mecanismos de ataque (criptografia maliciosa, captura de dados).

Demonstrar a implementação de um Ransomware (ataque/recuperação) e um Keylogger (captura/exfiltração).

Analisar e Documentar estratégias eficazes de prevenção e defesa digital.

💻 1. Ransomware Simulado (ransomware_simulado.py)

O script simula o sequestro de dados criptografando e, posteriormente, descriptografando arquivos em um diretório de teste.

⚙️ Como Usar

Instalação:

pip install cryptography


Preparação: Crie uma pasta chamada test_files no mesmo diretório do script e adicione arquivos de texto (.txt, .doc, etc.) para serem criptografados.

Modo de Operação: Altere a variável MODO_DESCRIPTOGRAFIA dentro do script para definir o comportamento.

Variável

Ação

Resultado

MODO_DESCRIPTOGRAFIA = False

ATAQUE (Criptografia)

Gera chave.key, cria a nota LEIA ISSO.txt e criptografa os arquivos em test_files.

MODO_DESCRIPTOGRAFIA = True

DEFESA (Descriptografia)

Usa a chave.key gerada no ataque e restaura os arquivos em test_files.

🧠 Entendimento da Ameaça

O Ransomware explora a confiança do usuário (clicar em anexos ou links maliciosos) e a urgência (necessidade de acesso imediato aos dados) para forçar o pagamento. A chave de defesa reside na separação de privilégios e no backup.

⌨️ 2. Keylogger com Exfiltração (keylogger_email.py)

Este script demonstra como um atacante pode capturar sequências de teclas (credenciais, mensagens) e enviá-las de volta para o atacante via e-mail (exfiltração de dados).

⚙️ Como Usar

Instalação:

pip install pynput


Configuração de E-mail (CRÍTICO): O script usa o Gmail. Para que smtplib funcione, você DEVE gerar e usar uma Senha de Aplicativo (App Password) nas configurações de segurança do Google, em vez de sua senha de login normal. Preencha as variáveis EMAIL_ORIGEM, EMAIL_DESTINO e SENHA_EMAIL no script.

Execução Furtiva: Para executar o script sem que a janela do terminal apareça (modo furtivo), renomeie o arquivo para .pyw e execute-o.

# Exemplo de execução furtiva no Windows (após renomear para .pyw)
# pythonw keylogger_email.pyw


🧠 Entendimento da Ameaça

O Keylogger depende da furtividade e da persistência (rodar no background). A exfiltração via e-mail é um método comum para transferir dados roubados em pequenos lotes (a cada 60 segundos), dificultando a detecção por firewalls simples.

🛑 3. Reflexão sobre Defesa e Prevenção

A melhor forma de combater esses malwares é através de uma defesa em camadas: tecnológica, processual e humana.

A. Defesa Tecnológica (Hardening)

Ameaça

Medida de Prevenção

Detalhes

Ransomware

Backup 3-2-1

Manter 3 cópias de dados, em 2 mídias diferentes, com 1 cópia fora do local (off-site ou na nuvem).

Ransomware

Antivírus (EDR)

Utilizar soluções de EDR (Endpoint Detection and Response) que monitoram o comportamento do sistema (ex: muitos arquivos sendo criptografados rapidamente).

Keylogger

Firewall de Host

Bloquear tentativas de conexão SMTP (porta 587) de programas não autorizados em background.

Geral

Sandboxing e VM

Executar programas de origem desconhecida em ambientes isolados (Máquinas Virtuais) que não têm acesso aos dados reais do usuário.

B. Conscientização do Usuário (O Fator Humano)

A maioria dos malwares depende da engenharia social para infectar.

Ameaça

Medida de Prevenção

Detalhes

Ransomware (Phishing)

Verificação de E-mail

Desconfiar de anexos de remetentes desconhecidos ou e-mails com tom de urgência extrema.

Keylogger

Gerenciadores de Senha

Usar gerenciadores de senha que preenchem as credenciais automaticamente. Em muitos casos, isso impede o keylogger de capturar as credenciais digitadas.

Geral

Princípio do Menor Privilégio

Utilizar contas de usuário padrão (sem privilégios de administrador) para o uso diário, impedindo que um malware se instale profundamente no sistema.

🔗 Entrega do Desafio

Crie um repositório público no GitHub.

Adicione os arquivos ransomware_simulado.py e keylogger_email.py ao repositório.

Use este conteúdo como o arquivo README.md principal.

Submeta o link do repositório para a conclusão do desafio!

Bons estudos e sucesso na sua apresentação!
