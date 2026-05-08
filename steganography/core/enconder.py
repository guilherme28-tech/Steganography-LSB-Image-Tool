"""codificador LSD para imagem esteganográfica."""

from __future__ import annotations
from pathlib import Path
from PIL import Image
from utils.binary import text_to_binary


def _set_bit(value: int, bit: str):
    return (value & ~1) | int(bit)


def _build_payload(message: str):
    payload = text_to_binary(message)
    header = format(len(payload), "032b")
    return header + payload


def _validate_capacity(image: Image.Image, payload_length: int):
    width, height = image.size
    capacity = width * height * 3
    if payload_length > capacity:
        raise ValueError(
            f"Mensagem muito longa para a imagem. "
            f"Capacidade: {capacity} bits, mensagem: {payload_length} bits."
        )


def embed_message_in_image(input_path: str | Path, output_path: str | Path, message: str):
    """adicione uma mensagem de texto em uma imagem usando codificação LSB."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    image = Image.open(input_path)
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")

    payload = _build_payload(message)
    _validate_capacity(image, len(payload))

    pixels = list(image.getdata())
    encoded_pixels = []
    payload_index = 0

    for pixel in pixels:
        channels = list(pixel[:3])
        new_channels = []

        for channel in channels:
            if payload_index < len(payload):
                new_channels.append(_set_bit(channel, payload[payload_index]))
                payload_index += 1
            else:
                new_channels.append(channel)

        if image.mode == "RGBA":
            new_channels.append(pixel[3])

        encoded_pixels.append(tuple(new_channels))

    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(encoded_pixels)
    encoded_image.save(output_path)


def get_image_capacity(input_path: str | Path):
    """Retorna o número de bits de mensagem que podem ser escondidos na imagem."""
    image = Image.open(input_path)
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")

    width, height = image.size
    return width * height * 3 - 32