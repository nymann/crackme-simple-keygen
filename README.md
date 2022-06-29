# Crackme Simple Keygen

## Reversed C code

```c
int checkSerial(char *serial)

{
  int return_code;
  size_t serial_length;
  int i;

  serial_length = strlen(serial);
  if (serial_length == 16) {
    for (i = 0; serial_length = strlen(serial), (ulong)(long)i < serial_length; i = i + 2) {
      if ((int)serial[i] - (int)serial[(long)i + 1] != -1) {
        return -1;
      }
    }
    return_code = 0;
  }
  else {
    return_code = -1;
  }
  return return_code;
}

int main(int argc,char **argv)

{
  int exit_code;

  if (argc != 2) {
    usage(*argv);
  }
  exit_code = checkSerial(argv[1]);
  if (exit_code == 0) {
    puts("Good Serial");
    exit_code = 0;
  }
  else {
    puts("Bad Serial");
    exit_code = -1;
  }
  return exit_code;
}
```

Check `tests/unit_tests/test_keygen.py` for a reversed python implementation.

## Test that it's working against the actual program

```bash
./crackme_bin/SimpleKeyGen $(crackme_simple_keygen)
```

Or via docker:

```bash
docker build -f docker/Dockerfile -t crackme_simple_keygen .
docker run -t crackme_simple_keygen SimpleKeyGen $(crackme_simple_keygen)
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
