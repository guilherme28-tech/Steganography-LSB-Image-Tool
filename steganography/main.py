"""Ferramenta de esteganografia LSB para imagens."""

from __future__ import annotations
import argparse
from core.decoder import extract_message_from_image
from core.enconder import embed_message_in_image


def main():
    parser = argparse.ArgumentParser(
        description="codificador ou decodificador de mensagens em imagens."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    encode_parser = subparsers.add_parser("encode", help="Ocultar uma mensagem em uma imagem")
    encode_parser.add_argument("input_image", help="Caminho da imagem original")
    encode_parser.add_argument("output_image", help="Caminho para salvar a imagem com a mensagem oculta")
    encode_parser.add_argument("message", help="Mensagem de texto a ser escondida")

    decode_parser = subparsers.add_parser("decode", help="Extrair uma mensagem de uma imagem")
    decode_parser.add_argument("input_image", help="Caminho da imagem que contém a mensagem oculta")

    args = parser.parse_args()

    if args.command == "encode":
        embed_message_in_image(args.input_image, args.output_image, args.message)
        print(f"Mensagem codificada em {args.output_image}")
    elif args.command == "decode":
        message = extract_message_from_image(args.input_image)
        print("Mensagem extraída:")
        print(message)


if __name__ == "__main__":
    main()