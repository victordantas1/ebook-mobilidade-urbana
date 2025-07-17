import pywhatkit
import pyautogui
import time

mensagem = ''

for i in range (100):
    mensagem += (f'FEIA, VELHA CHATA \n')

numero = '+5592993327528'

pywhatkit.sendwhatmsg_instantly(numero,mensagem)

# Esperar tempo para você abrir a conversa no WhatsApp Web/Desktop
print("Você tem 10 segundos para abrir a conversa no WhatsApp...")
time.sleep(10)

for i in range(1, 10):

    pyautogui.typewrite(mensagem)  # Digita a mensagem
    pyautogui.press("enter")  # Pressiona Enter para enviar

    time.sleep(1.2)  # Espera 1.2 segundos entre cada mensagem
