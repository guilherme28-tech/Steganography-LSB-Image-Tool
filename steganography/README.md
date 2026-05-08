# Steganography LSB Image Tool

Este projeto implementa uma ferramenta simples de esteganografia LSB (Least Significant Bit) para imagens em Python. O objetivo é ocultar e extrair mensagens de texto em imagens através da modificação dos bits menos significativos dos canais de cores.

## Recursos

- Codificar uma mensagem de texto em uma imagem existente
- Decodificar uma mensagem oculta de uma imagem
- Suporte a imagens RGB e RGBA
- Validação da capacidade da imagem antes de codificar

## Estrutura do projeto

- `main.py` - Script principal que expõe a interface de linha de comando com os subcomandos `encode` e `decode`
- `core/enconder.py` - Lógica de inserção da mensagem no canal LSB da imagem
- `core/decoder.py` - Lógica de extração da mensagem da imagem
- `utils/binary.py` - Funções auxiliares para conversão entre texto e binário
- `gui.py` - Interface gráfica recomendada para executar o projeto de forma mais amigável

## Uso recomendado

A forma recomendada de executar o projeto é usando a interface gráfica em `gui.py`, pois ela facilita a seleção de imagens e a inserção/extração de mensagens sem precisar usar a linha de comando.

## Requisitos

- Python 3.10 ou superior
- `Pillow`

## Instalação

1. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale a dependência:

```bash
pip install pillow
```

## Uso via linha de comando

Navegue até o diretório do projeto:

```bash
cd c:\Users\gui\Desktop\workspace\steganography
```

### Comando `encode`

Oculta uma mensagem em uma imagem.

```bash
python main.py encode <imagem_entrada> <imagem_saida> "Sua mensagem secreta"
```

Exemplo:

```bash
python main.py encode input.png output.png "Mensagem oculta"
```

### Comando `decode`

Extrai uma mensagem oculta de uma imagem.

```bash
python main.py decode <imagem_entrada>
```

Exemplo:

```bash
python main.py decode output.png
```

## Como funciona

A mensagem é convertida em uma sequência binária, e um cabeçalho de 32 bits é usado para armazenar o comprimento da mensagem em bits. Em seguida, cada bit da mensagem é inserido no bit menos significativo de cada canal de cor RGB da imagem.

Durante a decodificação, o programa lê os primeiros 32 bits para obter o tamanho da mensagem e reconstrói o texto a partir dos bits seguintes.

## Limites

- A capacidade máxima de mensagem depende do tamanho da imagem e do número de canais de cor.
- A imagem deve ter pelo menos 32 bits disponíveis para armazenar o cabeçalho.
- Se a mensagem for maior que a capacidade da imagem, o processo de codificação gera uma exceção.

## Observações

- Use imagens de boa qualidade sem compressão excessiva para manter a integridade dos dados.
- O código atual funciona melhor com imagens em formatos comuns como PNG.

## Exemplo completo

```bash
python main.py encode foto.png foto_com_mensagem.png "Olá, isso é um teste!"
python main.py decode foto_com_mensagem.png
```

Se quiser, posso também adicionar instruções para rodar a interface gráfica `gui.py`. 