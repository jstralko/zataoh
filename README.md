# zataoh
Zen and the Art of Hacking

Build:
gcc -g -z execstack -no-pie -o vuln vuln.c

Generate the shellcode
(Need to find the EIP using gdb)
python shellcode.py > shellcode

*buffer lives in between esp and ebp
info registers
x/40x $esp

Run:
./envexec.sh vuln $(cat shellcode)
