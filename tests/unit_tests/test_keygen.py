from devtools import debug
import pytest

from crackme_simple_keygen.main import generate_serial


@pytest.mark.parametrize("serial", [generate_serial() for _ in range(1000)])
def test_keygen(serial: str):
    serial_length = len(serial)
    if serial_length != 16:
        assert False
    for i in range(0, serial_length - 1, 2):
        a = serial[i]
        b = serial[i + 1]
        if ord(a) - ord(b) != -1:
            debug(a, b, ord(a) - ord(b))
            assert False
    assert True
