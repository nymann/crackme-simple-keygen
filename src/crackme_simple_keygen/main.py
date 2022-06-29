from random import randint

import typer

app = typer.Typer()

ASCII_MIN = 32  # ' '
ASCII_MAX = 127  # ~
PASSWORD_LEN = 16


@app.command()
def keygen():
    typer.echo(generate_serial())  # pragma: no cover


def generate_serial() -> str:
    serial = []
    for _ in range(0, PASSWORD_LEN - 1, 2):
        a: int = _random_ascii()
        serial.append(chr(a))
        serial.append(chr(a + 1))

    return "".join(serial)


def _random_ascii() -> int:
    return randint(ASCII_MIN, ASCII_MAX - 1)


if __name__ == "__main__":
    app()  # pragma: no cover
