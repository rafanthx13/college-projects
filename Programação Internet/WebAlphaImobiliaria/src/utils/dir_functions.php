<?php

/*
As funções "chose_prefix" e semelhantes sâo necessárias para diferenciar
os endereços de diretorio entre o index.php , que está na raiz e as páginas
públicas que estão dentro de '/app/template/public_area'. Como ambos usam um mesmo
header que aponta para endereços difenretes, o "prefixo" deve ser diferente:
  (o index.php só entra até chega no destino, já os da area publica tem que
   sair e pegar um caminho diferente)
*/

// Retorna um das tres strings: alpha (para o index), private_area ou public_area

function actual_dir(){
  $dir = getcwd();
  $array_dir = explode("/", $dir);
  $actual_dir = end($array_dir);
  return $actual_dir;
}

// trocar por "alpha1imobiliaria99.onlinewebshop.net" "alpha"

function choose_prefix_navbar(){
  $dir = actual_dir();
  if(strcmp($dir, "alpha1imobiliaria99.onlinewebshop.net") == 0){
    $prefix = "./app/template/public_area/";
  } else {
    $prefix = "./";
  }
  return htmlspecialchars($prefix);
}

function choose_prefix_header(){
  $dir = actual_dir();
  if(strcmp($dir, "alpha1imobiliaria99.onlinewebshop.net") == 0){
    $prefix = "./app/img/";
  } else {
    $prefix = "./../../img/";
  }
  return htmlspecialchars($prefix);
}

function choose_prefix_private(){
  $dir = actual_dir();
  if(strcmp($dir, "alpha1imobiliaria99.onlinewebshop.net") == 0){
    $prefix = "./app/template/private_area/";
  } else {
    $prefix = "./../private_area/";
  }
  return htmlspecialchars($prefix);
}

function choose_prefix_home(){
  $dir = actual_dir();
  if(strcmp($dir, "alpha1imobiliaria99.onlinewebshop.net") == 0){
    $prefix = "";
  } else {
    $prefix = "./../../../index.php";
  }
  return htmlspecialchars($prefix);
}

function choose_prefix_login(){
  $dir = actual_dir();
  if(strcmp($dir, "alpha1imobiliaria99.onlinewebshop.net") == 0){
    $prefix = "./src/bd/";
  } else {
    $prefix = "./../../../src/bd/";
  }
  return htmlspecialchars($prefix);
}

?>