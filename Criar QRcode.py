import pyqrcode
from pyautogui import prompt
import re

# Solicitar entrada do usuário
string = prompt(title='Gerador de QRCode',
                text="Cole aqui o endereço da página \nExemplo: www.suapagina.com")

# Converter para letras minúsculas
string = string.lower()

# Gera QR CODE
qrcode = pyqrcode.create(string)

# Criar e salvar o QRcode
qrcode.svg(f'{string}.svg', scale=10)
