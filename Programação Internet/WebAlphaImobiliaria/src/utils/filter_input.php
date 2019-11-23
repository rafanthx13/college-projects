<?php

// Filtra campo do form para evitar SQL INjection
function filter_form($data){
  $data = trim($data);               // remove espaços no inicio e no final da string
  $data = stripslashes($data);       // remove contra barras: "cobra d\'agua" vira "cobra d'agua"
  $data = htmlspecialchars($data);   // caracteres especiais do HTML (como < e >) são codificados
  return $data;
}

?>