#include "grafos.h"

Fila* open_fila(){
    Fila *fil = (Fila*)malloc(sizeof(Fila));
    fil->fim = NULL;
    fil->ini = NULL;
    return fil;
}

No* insere_fim(No *fim, int x){
    No *p = (No*)malloc(sizeof(No));
    p->num = x;
    if(fim == NULL){
        p->next = NULL;
    }else{
        fim->next = p;
        p->next = NULL;
    }
    return p;
}

void insert_fila(Fila *fil, int x){
    fil->fim = insere_fim(fil->fim, x);
    if(fil->ini == NULL){ //So ha um elemento, enato sao os mesmos
        fil->ini = fil->fim;
    }
}

No* retira_inicio(No *ini){
    No *p = ini, *q;
    q = ini->next;
    free(p);
    return q;
}

int remove_fila(Fila *fil){
    int safe;
    if(empy_fila(fil) == 0){
        safe = fil->ini->num;
        fil->ini = retira_inicio(fil->ini);
        if(fil->ini == NULL){
            fil->fim = NULL;
        }
        return safe;
    }else{
        exit(1);
    }
}



int empy_fila(Fila *fil){
    if(fil->ini == NULL){
        return 1; //vazia mesmo
    }else{
        return 0; //tem algo dentro
    }
}

void destroy_fila(Fila *fil){
    No *p = fil->ini, *q;
    while(p != NULL){
        q = p->next;
        free(p);
        p = q;
    }
    free(fil);
}
