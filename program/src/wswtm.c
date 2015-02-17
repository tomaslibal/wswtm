#include <stdio.h>

#include <stdlib.h>
#include <string.h>

#include "util.h"

/*
 * Make inline
 */
void mydebug(char* msg, char* filename, int line);

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
int main(int argc, char** argv)
{
    /*
     * Check that there are at least 3 arguments
     */
    if (argc < 2) {
        mydebug("Not enough parameters\n", __FILE__, __LINE__);
        printf("Usage: wswtm path/to/image.jpg\n");
        return 1;
    }

    /*
     * Read argument argv[2] which should have the path to the image that
     * is being classified.
     */
    char* img_path;
    img_path = malloc(sizeof(char) * strlen(argv[1]));
    if (img_path == NULL) {
        mydebug("Error allocating memory for img_path\n", __FILE__, __LINE__);
    }

    /*
     * Extract the pixel array from the image and compute the feature vector
     */

    /*
     * Run the feature vector through all classifiers and collect 
     * classification results
     */

    /*
     * Print out the results
     */

    return 0;
}

void mydebug(char* msg, char* filename, int line)
{
    printf("!mydebug in %s, line %d: ", filename, line);
    printf("%s", msg);
}
