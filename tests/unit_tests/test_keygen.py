import pytest

from crackme_simple_keygen.main import generate_serial


@pytest.mark.parametrize("serial", [generate_serial() for _ in range(1000)])
def test_keygen(serial: str) -> None:
    serial_length = len(serial)
    if serial_length != 16:
        raise AssertionError()
    for index in range(0, serial_length - 1, 2):
        current = ord(serial[index])
        neighbour = ord(serial[index + 1])
        if current - neighbour != -1:
            raise AssertionError()
