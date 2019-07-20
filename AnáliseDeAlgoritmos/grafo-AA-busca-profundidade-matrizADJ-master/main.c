#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#define GET_MS(ini, fim)  ((fim.tv_sec * 1000000 + fim.tv_usec) \
			- (ini.tv_sec * 1000000 + ini.tv_usec))

/*	@autor:	Rafael Morais de Assis - 01 de Agosto de 2017

	Objetivo: Analise de Algoritmos com Grafos (AA)
	Descriçao do Programa:
		Cria N Grafos de Nvert com Narestas e calcula seu tempo colocando-os em um arquivoTempoTXT
	Intruçoes:
		1. começa de begin = 5 ==> 2^5 = 32 Vertices, para muda-lo 			//modifique begin
		2. vai ate max_potencia. max_potencia = 14 ==> 2^14 = 16k vertices	//modifique max_potencia
		3. QTD_DE_ARESTA: Procure Naresta e muda o numero final, quanto maior, menos arestas
*/

/*
	CHANGE: O num maximo de Arestas eh Aresta = n(n-1)/2, onde n eh o numero de vertices
		==>	Entao, da pra colocar mais aresta do que se pensa, e, nos estamos colocando poucas.
*/

/**< para testar com aresta diferentes: modifique fator_aresta nos parametros  */

typedef struct listadj{
	int campo;
	struct listadj* prox;
} ListaAdj;

enum cores {WRITE = 0, GRAY = 1, BLACK = 2, NILL = 3};

int acessa_adj(ListaAdj **ladj, int count, int vertice){
    ListaAdj *pt;
    int pass = 1;
    if(ladj == NULL){
        printf("erro -1\n");
        return -1;
    }
    pt = ladj[vertice]; //ladj tem ** e, por isso, pt pode ter um dos seus * , por isos o []
    while(pt != NULL && pass < count){
        pt = pt->prox;
        pass++;
    }
    if(pt == NULL){
        //printf("nao encontrou\n");
        return -1;
    }else{
        //printf("find: %d\n", pt->campo);
        return pt->campo;
    }
}

void Visita_Profundidade(int u, int *cor, int tempo, int *d, int *pai, int *f, int Nvert, ListaAdj **ladj){
    cor[u] = GRAY;
    tempo = tempo + 1;
    d[u] = tempo;
    int count_adj = 1;
    int novo_vertice;
    while(1){
        novo_vertice = acessa_adj(ladj, count_adj, u);
        if(novo_vertice == -1){
            break; // nao tem mais vertices
        }else{
            if(cor[novo_vertice] == WRITE){
                pai[novo_vertice] = u;
                Visita_Profundidade(novo_vertice,cor,tempo,d,pai,f,Nvert,ladj); // here
            }
        }
        count_adj++;
    }
    cor[u] = BLACK;
    tempo = tempo+1;
    f[u] = tempo;
}

void inserir_aresta(ListaAdj **listADJ, int vert_atual, int vert_adj){
    ListaAdj *p, *aux;
    if(listADJ == NULL){
        printf("erro\n");
        exit(1);
    }
    aux = listADJ[vert_atual];
    while(aux != NULL && aux->campo != vert_adj){
        aux = aux->prox;
    }
    if(aux != NULL){
        //printf("Aresta (%d,%d) ja existe\n", vert_atual, vert_adj);
        return ;
    }
    p = (ListaAdj*)malloc(sizeof(ListaAdj));
    if(p == NULL) return ;
    p->campo = vert_adj;
    p->prox = listADJ[vert_atual];
    listADJ[vert_atual] = p;
}

void arquivoTempoTXT(char *nome, double *tempo, int begin, int end_n){
    FILE *p;
    p = fopen(nome, "w");
    if(p == NULL){
        printf("ERRO no file");
        exit(1);
    }
    int i;
    printf("\nImprimindo em Arquivo\n");
    fprintf(p, "tamanho tempo\n");
    for(i=begin; i<end_n; i++)
    {
        fprintf(p, "%d %lf\n", (int)pow(2,i), tempo[i]);
    }
    fclose(p);
}

int main(){

    /**< Variaveis */
    int Nvert, i, Naresta = 0;
    int iteracao, r1, r2, u, tempo;

    /**< Parametros Coonfiguraveis - */
    int begin = 5;          /**< Begin: o 2^n que começa, ou seja, begin = 5 ==> começa de 32 Vertices */
    int max_potencia = 15; /**< max_potencia: ate que potencia vai, max_potenia = '5 ==> vai ate 2^15 vertices */


    /**< Alocaçao: Grafo, cor, pai, d, Q*/
    int *cor, *d, *pai, *f;
    ListaAdj **ladj;
    ListaAdj *pt_aux, *aux_free;

    /**< Variaveis para calcular os horarios */
    clock_t t;
    char buffer[50];
    double tempo_process;
    double vetor_tempo[17];

    /**< Inicio */
    for(iteracao = begin; iteracao < max_potencia; iteracao++){
        Nvert = (int) pow(2,iteracao);
        Naresta = (int) Nvert*(Nvert)/32; // 50% de Arestas, 25% de ida e 25% de volta

        /**< 1) Cria Lista de Adjacencia */
        ladj = (ListaAdj**)malloc(sizeof(ListaAdj*)*Nvert);
        if(ladj == NULL){
            printf("ERRO");
            system("pause");
            exit(1);
        }

        /**< 2) Inicializa a Lista de Adjacencia */
        for(i=0; i<Nvert; i++){
            ladj[i] = NULL;
        }

        /**< 3) Povoar Lista de Adjacencia*/
        for(i = 0; i < Naresta; i++){
            r1 = rand() % Nvert;
            r2 = rand() % Nvert;
            inserir_aresta(ladj,r1,r2);
            inserir_aresta(ladj,r2,r1);
        }

        /**< 4) Inicializa ED auxiliares */
        cor = (int*)malloc(sizeof(int)*Nvert);
        d   = (int*)malloc(sizeof(int)*Nvert);
        pai = (int*)malloc(sizeof(int)*Nvert);
        f   = (int*)malloc(sizeof(int)*Nvert);

        /**< 5) Algoritmo: Busca em Profundidade em Lista de Adjacencia - Calcula Tempo */
        t = clock();
        for(i = 0; i < Nvert; i++){
            cor[i] = WRITE;
            pai[i] = NILL;
        }
        tempo = 0;
        for(u = 0; u < Nvert; u++){
            if(cor[u] == WRITE){
                Visita_Profundidade(u,cor,tempo,d,pai,f, Nvert, ladj);
            }
        }
        t = clock() - t;
        tempo_process = ((double)t)/((CLOCKS_PER_SEC/1000));
        vetor_tempo[iteracao] = tempo_process;

        /**< 6) Desalocar valores */
        if(ladj != NULL){
            for(i=0; i<Nvert; i++){
                pt_aux=ladj[i];
                while(pt_aux!=NULL){
                    aux_free = pt_aux;
                    pt_aux = pt_aux->prox;
                    free(aux_free);
                }
            }
        }
        free(ladj);
        free(pai);
        free(d);
        free(f);
        free(cor);

        /**< 7) Terminou */
        printf("Terminou! Busca em Largura\n");
        printf("\tGrafo com %d vertices e %d arestas\n", Nvert, Naresta); //Grafo Nao orientado
    }

    /**< 8)Imprimir */
    strcpy(buffer, "grafoProfundidade++");
    arquivoTempoTXT(buffer, vetor_tempo, begin, max_potencia);

    printf("END\n");
    system("pause");
    return 0;
}
