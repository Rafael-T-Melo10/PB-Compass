import hashlib

while True:
    input_texto = input('Digite a palavra: ')
    texto_hash = hashlib.sha1(input_texto.encode()).hexdigest()
    print(texto_hash)