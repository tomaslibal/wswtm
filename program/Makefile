CC=gcc
IFLAG=/usr/local/include
LFLAG=/usr/local/lib


all: src/wswtm.c
	-mkdir bin
	$(CC) -I$(IFLAG) -L$(LFLAG) src/wswtm.c -o bin/wswtm

clean:
	rm -f wswtm
