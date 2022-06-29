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
    start_index = _random()
    serial = [chr(i) for i in range(start_index, start_index + PASSWORD_LEN)]
    return "".join(serial)


def _random() -> int:
    return randint(ASCII_MIN, ASCII_MAX - PASSWORD_LEN)


if __name__ == "__main__":
    app()  # pragma: no cover
