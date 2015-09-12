#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define BUFFER_SIZE 64


typedef struct __cli {/*{{arguments}}*/
} CLI;


void parse(int argc, char *argv[], CLI *cli) {
    char usage[] = "{{usage}}";
    char lut[] = ("{{lut}}");
    char *ptr = lut;
    char buf0[BUFFER_SIZE], buf1[BUFFER_SIZE];
    int j, i;
    while (*ptr != '\0') {
        for (j=0; *ptr != ','; j++)
            buf0[j] = *ptr++;
        buf0[j] = '\0';
        if (argc != atoi(buf0)) {
            while (*ptr != '|')
                ptr++;
            ptr++;
            continue;
        }
        while (*ptr != ',') {
            for (j=0; *ptr != ';' || *ptr != ','; j++)
                buf0[j] = *ptr++;
            buf0[j] = '\0';
            strcat(buf1, argv[atoi(buf0)]);
        }
        for (j=0; *ptr != ','; j++)
            buf0[j] = *ptr++;
        buf0[j] = '\0';
        if (strcmp(buf0, buf1))
            continue;
        for (i=0; i < argc; i++) {
            for (j=0; *ptr != ';' || *ptr != '|'; j++)
                buf0[j] = *ptr++;
            buf0[j] = '\0';
            if (buf0[0] != '-' && argv[i] == '-')
                exit(EXIT_FAILURE);
            /*
            if (!strcmp(buf0, "fin"))
                cli->fin = argv[i];
            else
            if (!strcmp(buf0, "fout"))
                cli->fout = argv[i];
            else
            if (!strcmp(buf0, "-f"))
                cli->_f = argv[i];
            */
        }
    }
    exit(EXIT_FAILURE);
}


int main(int argc, char *argv[]){
    CLI cli;
    parse(argc, argv, &cli);
    printf("{}\n");
    return 0;
}
