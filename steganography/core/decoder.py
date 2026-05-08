"""Decodeficador LSD para imagem esteganográfica."""

from __future__ import annotations
from pathlib import Path
from PIL import Image
from utils.binary import binary_to_text


def _extract_bits_from_image(image: Image.Image):
    pixels = list(image.getdata())
    bits = []

    for pixel in pixels:
        for channel in pixel[:3]:
            bits.append(str(channel & 1))

    return "".join(bits)


def extract_message_from_image(input_path: str | Path):
    """Extrai uma mensagem de texto de uma imagem esteganográfica."""
    input_path = Path(input_path)

    image = Image.open(input_path)
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")

    bits = _extract_bits_from_image(image)
    if len(bits) < 32:
        raise ValueError("A imagem não contém dados suficientes para recuperar a mensagem.")

    header = bits[:32]
    payload_length = int(header, 2)
    expected_length = 32 + payload_length

    if len(bits) < expected_length:
        raise ValueError("A imagem não contém todos os bits da mensagem esperada.")

    payload_bits = bits[32:expected_length]
    return binary_to_text(payload_bits)