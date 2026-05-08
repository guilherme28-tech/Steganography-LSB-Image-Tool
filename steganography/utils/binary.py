def text_to_binary(text):
    """Converte texto para string binaria."""
    binary_final = ""
    for char in text:
        valor_ascii = ord(char)
        binary = bin(valor_ascii)[2:].zfill(8)
        binary_final += binary
    return binary_final

def binary_to_text(binary):
    """Converte binario pra string."""
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        valor_ascii = int(byte, 2)
        char = chr(valor_ascii)
        text += char
    return text
