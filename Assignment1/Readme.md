#Simple Translator which converts 32 bit arm code to 64 bit code

###############################################################

##commands:

###executing 32_bit.asm:

nasm -f elf32 32_bit.asm

gcc -m32 32_bit.o -o 32_bit_run

./32_bit_run


###executing 64_bit.asm:

nasm -f elf64 64_bit.asm

ld 64_bit.o -o 64_bit_run

./64_bit_run


###executing 64_bit_conv.asm:

nasm -f elf64 64_bit_conv.asm

ld 64_bit_conv.o -o 64_bit_conv_run

./64_bit_conv_run


###executing transaltor.cpp

g++ translator.cpp

./a.out

