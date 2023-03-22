from pytube import YouTube

url = input("Insira a URL do vídeo do YouTube: ")

# Cria uma instância da classe YouTube para a URL especificada
yt = YouTube(url)

# Seleciona a melhor resolução possível para o download
resolucao = yt.streams.get_highest_resolution()

# Realiza o download do vídeo na pasta atual
resolucao.download()
print("Download completo!")
