#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define BUFFER_SIZE 64


typedef struct __cli {{{arguments}}
} CLI;


void parse(int argc, char *argv[], CLI *cli) {
    char usage[] = ("{{usage}}");
    char lut[] = ("{{lut}}");
    char *ptr = lut;
    char buf0[BUFFER_SIZE], buf1[BUFFER_SIZE];
    int j, i;
    while (*ptr != '\0') {
        for (j=0; *ptr != ',' && *ptr != '\0'; j++)
            buf0[j] = *ptr++;
        buf0[j] = '\0';
        if (*ptr == ',')
            ptr++;
        j = atoi(buf0);
        if ((argc - 1) < j)
            break;
        if ((argc - 1) > j) {
            while (*ptr != '|' && *ptr != '\0')
                ptr++;
            if (*ptr == '|')
                ptr++;
            continue;
        }
        buf1[0] = '\0';
        while (*ptr != ',' && *ptr != '\0') {
            for (j=0; (*ptr != ';' && *ptr != ',')  && *ptr != '\0'; j++)
                buf0[j] = *ptr++;
            buf0[j] = '\0';
            if (*ptr == ';')
                ptr++;
            j = atoi(buf0);
            strcat(buf1, argv[j + 1]);
        }
        if (*ptr == ',')
            ptr++;
        for (j=0; *ptr != ',' && *ptr != '\0'; j++)
            buf0[j] = *ptr++;
        buf0[j] = '\0';
        if (*ptr == ',')
            ptr++;
        if (strcmp(buf0, buf1)){
            while (*ptr != '|' && *ptr != '\0')
                ptr++;
            if (*ptr == '|')
                ptr++;
            continue;
        }
        for (i=1; i < argc; i++) {
            for (j=0; (*ptr != ';' && *ptr != '|')  && *ptr != '\0'; j++)
                buf0[j] = *ptr++;
            buf0[j] = '\0';
            if (*ptr == ';')
                ptr++;
            if (buf0[0] != '-' && argv[i][0] == '-') {
                fprintf(stderr, "%s\n", usage);
                exit(EXIT_FAILURE);
            }{{comparers}}
        }
        return;
    }
    fprintf(stderr, "%s\n", usage);
    exit(EXIT_FAILURE);
}


int main(int argc, char *argv[]){
    CLI cli = {0};
    parse(argc, argv, &cli);{{dumpers}}
    return 0;
}
