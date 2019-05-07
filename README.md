# utf8 overlong encode #
```
usage: utf8encode.py [-h] [-b NUM] string

positional arguments:
  string      string to be encoded

optional arguments:
  -h, --help  show this help message and exit
  -b NUM      Number of bytes
```

## example ##
* `utf8encode.py -b 1 "../"`
  * `%2e%2e%2f`
* `utf8encode.py "../"`
  * `%c0%ae%c0%ae%c0%af`