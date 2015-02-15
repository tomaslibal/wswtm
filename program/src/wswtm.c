#include <stdio.h>

void debug(char* msg, int code);

/*
 * Usage:
 *
 * wswtm path/to/image.jpg
 *
 * Help:
 *
 * wswtm --help: prints possible flags
 *
 * wswtm --man: prints URL of manual 
 */
int main(int argc, char* argv)
{	
    debug("Not yet implemented\n", 1);
	return 0;
}

void debug(char* msg, int code)
{
    fprintf(stdout, msg, code);
}
