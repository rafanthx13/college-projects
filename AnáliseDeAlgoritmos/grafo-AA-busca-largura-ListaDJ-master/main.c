#include "grafos.h"

/*	@autor:	Rafael Morais de Assis - 01 de Agosto de 2017

	Objetivo: Analise de Algoritmos com Grafos (AA)
	Descriçao do Programa:
		Cria N Grafos de Nvert com Narestas e calcula seu tempo colocando-os em um arquivoTempoTXT
	Intruçoes:
		1. começa de begin = 5 ==> 2^5 = 32 Vertices, para muda-lo 			//modifique begin
		2. vai ate max_potencia. max_potencia = 14 ==> 2^14 = 16k vertices	//modifique max_potencia
		3. fator_aresta eh a proporçao de arestas. Ex: se fator_aresta = 4 ==> que a quantidade
			de aresta eh a quantidade de vertices dividio por 2^4 = 16,
				--> Quanto menor fator_aresta ==> Mais Arestas ==> Mais Denso
				--> Obs: tente nao arpoximar muito arestas ===== vertice, pois ele verifica se uma
						 aresta pode ou nao ser colocada(Somente em busca em Profundidade)
*/

/*
	CHANGE: O num maximo de Arestas eh Aresta = n(n-1)/2, onde n eh o numero de vertices
		==>	Entao, da pra colocar mais aresta do que se pensa, e, nos estamos colocando poucas.
*/

enum cores {WRITE = 0, GRAY = 1, BLACK = 2, NILL = 3};

/**< para testar com aresta diferentes: modifique fator_aresta nos parametros  */

void arquivoTempoTXT(char *nome, double *tempo, int begin, int end_n){
    FILE *p;
    p = fopen(nome, "w");
    if(p == NULL){
        printf("ERRO no file\n");
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
    srand(time(NULL));

    /**< Variaveis */
    int Nvert, i, j, v, Naresta, iteracao;
    int vert_inicial = 0, r1, r2;
    Fila *Q;
    clock_t t;
    char buffer[50];
    double tempo;
    double vetor_tempo[17];
    int *cor, *pai, *d;

    /**< Parametros Coonfiguraveis - */
    int begin = 5;          /**< Begin: o 2^n que começa, ou seja, begin = 5 ==> começa de 32 Vertices */
    int max_potencia = 15; /**< max_potencia: ate que potencia vai, max_potenia = '5 ==> vai ate 2^15 vertices */

    for(iteracao = begin; iteracao < max_potencia; iteracao++){
        Nvert = (int) pow(2,iteracao);
        Naresta = (int) Nvert*(Nvert-1)/32;
        //1) Cria Grafo de Matriz
        int **Grafo;
        Grafo = (int**)malloc(Nvert*sizeof(int*));
        if(Grafo == NULL){
            printf("ERRO ao Alocar_1");
            system("pause");
            return 0;
        }
        //2) Verifica Erros na alocaçao
        for(i = 0; i < Nvert; i++){
            Grafo[i] = (int*)calloc(Nvert,sizeof(int));
            if(Grafo[i] == NULL){

                for(j = 0; j < Nvert; j++){
                    free(Grafo[j]);
                }
                free(Grafo);
                printf("ERRO ao Alocar_2");
                system("pause");
                exit(1);
            }
        }
        //3) Zera o Grafo
        for(i = 0; i < Nvert; i++){
            for(j = 0; j < Nvert; j++){
                Grafo[i][j] = 0;
            }
        }
        //4) Povoa Grafo =  Arestas Aleartorias
        for(i = 0; i < Naresta; i++){
            r1 = rand() % Nvert;
            r2 = rand() % Nvert;
            Grafo[r1][r2] = 1;
            Grafo[r2][r1] = 1;
        }
        //5) Escolher vertice inicial e definindo ED auxiliares
        vert_inicial = rand() % Nvert;

        cor = (int*) malloc(sizeof(int)*Nvert);
        d   = (int*) malloc(sizeof(int)*Nvert);
        pai = (int*) malloc(sizeof(int)*Nvert);

        /**< INICIO DO ALGORIMO DE BUSCA EM LARGURA */
        t = clock();
        //6) Inicializaçao
        for(i = 0; i < Nvert; i++){
            if(i == vert_inicial){
                cor[i] = GRAY;
                d[i] = 0;
                pai[i] = NILL;
                i++;
            }
            cor[i] = WRITE;
            d[i] = -2;
            pai[i] = NILL;
        }
        //7) Inicializa Fila e trabalha sobre ela
        Q = open_fila();
        insert_fila(Q, vert_inicial);
        //8) A busca em Largura
        while( empy_fila(Q) == 0){ // Enquanto tiver elementos
            v = remove_fila(Q);
            for(i = 0; i < Nvert; i++){ //varia a linha
                if(Grafo[v][i] == 1){ //existe vertice
                    if(cor[i] == WRITE){
                        cor[i] = GRAY;
                        d[i] = d[v] + 1;
                        pai[i] = v;
                        insert_fila(Q, i);
                    }
                }
            }
            cor[v] = BLACK;
        }
        //9) Terminou o alg: calucala e salva tempo
        t = clock() - t;
        tempo = ((double)t)/((CLOCKS_PER_SEC/1000));

        vetor_tempo[iteracao] = tempo;

        //10) Terminou - Imprimi algo
        printf("Terminou! Busca em Largura\n");
        printf("\tGrafo com %d vertices e %d arestas\n", Nvert, Naresta*2);
        /*
            Imprimi pra conferir se deu certo
        */

        //11) Desaloca para nova interaçao
        for(i = 0; i <Nvert; i++){
            free(Grafo[i]);
        }
        free(Grafo);
        destroy_fila(Q);
        free(d);
        free(cor);
        free(pai);
    }
    /**< FIM    */
        strcpy(buffer, "grafoLargura++");
        arquivoTempoTXT(buffer, vetor_tempo, begin, max_potencia);
    printf("END\n");
    system("pause");
    return 0;
}
