# Projeto de Programação para Internet

**Onde Acessar**: http://alphaimobiliaria.info ou http://alpha1imobiliaria99.onlinewebshop.net/

Trabalho de PI - Rafael Assis e Miguel Henrique **Está incompleto**.

Projeto Web HTML/CSS/JS usando BootStrap e PHP no backEnd

## Incompleto

+ Falta corrigir `login` para as páginas diferentes de  `index.php`
+ Corrigri responsividade (colocar várias classe s para cada tipo)
+ Fazer filtragem de PHP para todas as entradas, para tudo que vem de GET/POST
+ Usar prepared Stametement nas coisas que requerem mais segurança
+ Corrigir login para celular (nâo abrir em nova aba)
+ Usar transaçâo para salavar imagens
+ Separar banco de dados: Casa de Apartamento
+ Terminal cadastro de imovel (imagens) e listagem
+ Corrigir listagem de dados, colocar todos os dados

## Navegação do Site

**Área Pública**

+ `index.php` : index/home da área pública. 

+ `who_we_are.php` : Quem somos

+ `imovel_search.php`: Busca de imóvel 
  + `imovel_list.php`: Listagem de Imóveis escolhidos no imovel_search
+ `navbar`
  + Acesso a `busca de imóveis` e `quem somos`
  + `login`

**Área Privada**

+ `private_index.php`: principal
+ Listagem de Dados
+ Cadastro de Dados

````
.
├── app
│   ├── css
│   │   └── style.css
│   ├── fonts
│   │   ├── FONTES
│   ├── img
│   │   ├── IMAGENS
│   ├── js
│   │   ├── app.js
│   │   ├── login.js
│   │   └── search_address.js
│   ├── lib
│   │   ├── LIBS
│   └── template
│       ├── private_area
│       │   ├── list_clients.php
│       │   ├── list_employes.php
│       │   ├── list_imovel.php
│       │   ├── list_interest.php
│       │   ├── private_index.php
│       │   ├── register_clients.php
│       │   ├── register_employes.php
│       │   └── register_imovel.php
│       ├── public_area
│       │   ├── imovel_list.php
│       │   ├── imovel_search.php
│       │   └── who_we_are.php
│       └── static
│           ├── footer.php
│           ├── login_modal.php
│           ├── logout.php
│           ├── modal_template.php
│           ├── private_header.php
│           ├── private_navbar.php
│           ├── public_header.php
│           └── public_navbar.php
├── desc
│   ├── COISAS ADICIONAIS
├── index.php
├── LICENSE
├── README.md
└── src
    ├── bd
    │   ├── authenticate.php
    │   ├── bd_querys.php
    │   ├── connection.php
    │   ├── login.php
    │   └── search_address.php
    └── utils
        ├── dir_functions.php
        └── filter_input.php

19 directories, 93 files
````
