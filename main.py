from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime

def obter_atributos_imagem(caminho_imagem):
    try:
        # Abrir a imagem
        imagem = Image.open(caminho_imagem)

        # Obter tamanho da imagem em MB
        tamanho_mb = os.path.getsize(caminho_imagem) / (1024 * 1024)

        # Obter altura e largura da imagem
        largura, altura = imagem.size

        # Obter data de modificação da imagem
        data_modificacao = os.path.getmtime(caminho_imagem)

        # Obter os metadados EXIF da imagem
        exif = imagem._getexif()

        # Extrair a data de criação original da imagem dos metadados EXIF
        data_criacao = exif.get(36867) if exif else None  # Tag para data de criação original

        # Imprimir os atributos
        print(f"Tamanho da imagem: {tamanho_mb:.2f} MB")
        print(f"Largura: {largura} pixels")
        print(f"Altura: {altura} pixels")
        print(f"Data de criação original: {data_criacao}")
        print(f"Data de modificação: {datetime.fromtimestamp(data_modificacao)}")

        # Mostrar outros atributos da imagem
        # outros_atributos = imagem.info
        # print("Outros atributos da imagem:")
        # for chave, valor in outros_atributos.items():
        #     print(f"{chave}: {valor}")

    except Exception as e:
        print(f"Erro ao obter os atributos da imagem: {e}")

if __name__ == "__main__":
    caminho_imagem = input("Digite o caminho da imagem: ").strip()
    # caminho_imagem = '/home/jean/Pictures/IMG_20141121_223739.jpg'.strip()
    obter_atributos_imagem(caminho_imagem)
