# 🔐 Steganography LSB Image Tool

Ferramenta de esteganografia desenvolvida em Python utilizando a técnica de LSB (Least Significant Bit) para ocultar e extrair mensagens de texto em imagens através da modificação dos bits menos significativos dos canais de cores.

O projeto foi desenvolvido com foco em estudos de manipulação de imagens, lógica de programação, operações bitwise e conceitos introdutórios de segurança da informação.

---

# Recursos

- 🔒 Codificação de mensagens em imagens
- 🔓 Decodificação de mensagens ocultas
- 🖼️ Suporte para imagens RGB e RGBA
- ✅ Validação da capacidade da imagem antes da codificação
- 🖥️ Interface gráfica para facilitar a utilização
- ⚙️ Execução via linha de comando

---

# 📂 Estrutura do Projeto

```bash
steganography/
│
├── main.py
├── gui.py
│
├── core/
│   ├── encoder.py
│   └── decoder.py
│
├── utils/
│   └── binary.py
│
└── assets/
```

### Arquivos principais

- `main.py` → Interface de linha de comando com os subcomandos `encode` e `decode`
- `core/encoder.py` → Responsável pela inserção da mensagem na imagem
- `core/decoder.py` → Responsável pela extração da mensagem
- `utils/binary.py` → Conversão entre texto e binário
- `gui.py` → Interface gráfica desenvolvida para facilitar o uso da aplicação

---

# Como Funciona

O projeto utiliza a técnica de LSB (Least Significant Bit), que consiste em alterar o último bit dos canais RGB dos pixels da imagem para armazenar informações sem mudanças perceptíveis visualmente.

## Processo de codificação

1. A mensagem é convertida para binário
2. Um cabeçalho de 32 bits armazena o tamanho da mensagem
3. Os bits da mensagem são inseridos nos canais RGB da imagem
4. A nova imagem é salva contendo os dados ocultos

## Processo de decodificação

1. O programa lê os primeiros 32 bits da imagem
2. O tamanho da mensagem é recuperado
3. Os bits seguintes são extraídos
4. O binário é convertido novamente para texto

---

# 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Pillow
- Tkinter

---

# ⚙️ Instalação

## 1️⃣ Clone o repositório

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd steganography
```

---

## 3️⃣ Crie e ative o ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4️⃣ Instale as dependências

```bash
pip install pillow
```

---

# ⚠️ Uso Recomendado

A forma recomendada de utilizar o projeto é através da interface gráfica:

```bash
python gui.py
```

A interface permite:
- selecionar imagens facilmente
- inserir mensagens
- codificar e decodificar dados sem utilizar o terminal

---

# Uso via Linha de Comando

## Comando `encode`

Oculta uma mensagem em uma imagem:

```bash
python main.py encode <imagem_entrada> <imagem_saida> "Sua mensagem secreta"
```

### Exemplo

```bash
python main.py encode input.png output.png "Mensagem oculta"
```

---

## Comando `decode`

Extrai uma mensagem de uma imagem:

```bash
python main.py decode <imagem_entrada>
```

### Exemplo

```bash
python main.py decode output.png
```

---

# Exemplo Completo

```bash
python main.py encode foto.png foto_com_mensagem.png "Olá, isso é um teste!"
python main.py decode foto_com_mensagem.png
```

---

# ⚠️ Limitações

- A capacidade máxima depende do tamanho da imagem
- Mensagens muito grandes excedem a capacidade disponível
- O projeto funciona melhor com imagens PNG
- Compressão excessiva pode comprometer os dados ocultos

---

# Objetivos do Projeto

Este projeto foi desenvolvido para praticar:

- manipulação de imagens
- operações bitwise
- lógica de programação
- arquitetura de projetos Python
- conceitos básicos de segurança da informação

