from rembg import remove
from PIL import Image
import os

from pyautogui import alert, prompt

while True:
    ## Receber do usuário o caminho para a imagem que deseja retirar o fundo
    input_path = prompt(title='Instruções de uso',
                        text='Vá até o arquivo que deseja remover o fundo, clique com o botão direito do mouse e clique em "Copiar como caminho", ou "Ctrl+Shift+C"\n\n ***são suportados arquivos tipo [jpg,jpeg,png,gif]')
    
    input_path = input_path.replace("\\", "/").replace('"', "")
    formato_entrada = input_path[-4:]
    
    nome_saida = input_path.split('/')[-1].split(f'{formato_entrada}')[0]
    output_path = f"{nome_saida}_fundoRemov.png"
    
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    
    # Salvar arquivo
    alert(text=f"O arquivo será salvo como: {output_path}", title='Aviso', button='Salvar')
    output_image.save(output_path)
    

# Abrir o arquivo automaticamente usando o sistema operacional
    try:
        os.startfile(output_path)  # Funciona no Windows
    except AttributeError:
        os.system(f"open {output_path}")  # Alternativa para sistemas baseados em Unix
    
  