from random import randint

import typer

app = typer.Typer()

ASCII_MIN = 32  # ' '
ASCII_MAX = 127  # ~
PASSWORD_LEN = 16


@app.command()
def keygen() -> None:
    typer.echo(generate_serial())  # pragma: no cover


def generate_serial() -> str:
    serial = []
    for _ in range(0, PASSWORD_LEN - 1, 2):
        index: int = _random_ascii_readable_index()
        serial.append(chr(index))
        serial.append(chr(index + 1))
    return "".join(serial)


def _random_ascii_readable_index() -> int:
    return randint(ASCII_MIN, ASCII_MAX - 1)  # noqa: S311


if __name__ == "__main__":
    app()  # pragma: no cover
