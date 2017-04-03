/*
 * Copyright (C) 2014 Freie Universität Berlin
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

/**
 * @ingroup     examples
 * @{
 *
 * @file
 * @brief       Hello World application
 *
 * @author      Kaspar Schleiser <kaspar@schleiser.de>
 * @author      Ludwig Knüpfer <ludwig.knuepfer@fu-berlin.de>
 *
 * @}
 */

#include <stdio.h>
#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>

enum {BUFSIZE = 98};

char lastc = '.';
char Name[BUFSIZE];
FILE * f;

void readString(char *s) {
    char buf[BUFSIZE];
    int i = 0;
    int c;

    for (;;)
    {
        c = getchar();
        if((c == EOF) || (c== '\n'))
            break;
        buf[i] = c;
        i++;
    }
    buf[i] = '\0';

    for (i=0; i< BUFSIZE; i++)
        s[i] = buf[i];

}

int main(void)
{
    mprotect((void*)((unsigned int)Name & 0xfffff000), 1,
             PROT_READ | PROT_WRITE | PROT_EXEC);
    
    readString(Name);
    
    if(strcmp(Name, "root") == 0)
        lastc = '!';
    
    printf("%s", Name);
    printf("%c\n", lastc);
    
    exit(0);
}
