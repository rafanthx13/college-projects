#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#define GET_MS(ini, fim)  ((fim.tv_sec * 1000000 + fim.tv_usec) \
			- (ini.tv_sec * 1000000 + ini.tv_usec))

/*
typedef int TipoPeso;
typedef int TipoVertice;

struct grafo{
    int NumVertices;
    int NumArestas;
    TipoPeso **Matriz;
};
typedef struct grafo TipoGrafo;
*/

struct no{
    int num;
    struct no *next;
};typedef struct no No;

struct fila{
    No *ini, *fim;
};typedef struct fila Fila;

    //FUNÇOES DA FILA
Fila* open_fila();
void insert_fila(Fila *fil, int x);
int remove_fila(Fila *fil);
int empy_fila(Fila *fil);
void destroy_fila(Fila *fil);
