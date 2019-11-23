<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/bd/bd_querys.php");

try {
  $msgErro = "";
	$connection = connectMySQL();
	$arrayImoveis= list_imovel($connection);  
} catch (Exception $e) {
	$msgErro = $e->getMessage();
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Listagem Imóveis</title>

    <script src="./../../../app/lib/jquery-3.4.1.min.js"></script>
    <script src="./../../../app/lib/popper.min.js"></script>
    <script src="./../../../app/lib/bootstrap-4.1.3-dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="./../../../app/lib/bootstrap-4.1.3-dist/css/bootstrap.min.css">
    <link rel="icon" href="./../../../app/img/logo-icon.ico">
    <link rel="stylesheet" href="./../../css/style.css">

</head>

<body>

    <!-- Header and NavBar -->
    <div class="sticky-top">
      <?php include "./../static/private_header.php"; ?>
      <?php include "./../static/private_navbar.php"; ?>
    </div>

    <!-- Main -->
    <div class="container">

      <h2 class="my-1">Listagem dos Imoveis</h2>

      <table class="table table-hover table-sm">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">N° Quartos</th>
                <th scope="col">N° Banheiros</th>
                <th scope="col">N° Suites</th>
                <th scope="col">N° Garagem</th>
                <th scope="col">Área</th>
                <th scope="col">Descrição</th>
                <th scope="col">Portaria</th>
                <th scope="col">Bairro</th>
                <th scope="col">ID Prprietário</th>
                <th scope="col">Nome Proprietário</th>
            </tr>
        </thead>
        <tbody>

          <?php
            if ($arrayImoveis != null) {
              foreach ($arrayImoveis as $imovel) { 
                echo "
                <tr>
                  <td scope=\"row\">$imovel->cod_imovel</td>
                  <td>$imovel->nro_quartos</td>
                  <td>$imovel->nro_banheiros</td>
                  <td>$imovel->nro_suites</td>
                  <td>$imovel->nro_garagem</td>
                  <td>$imovel->area</td>
                  <td>$imovel->descricao</td>
                  <td>$imovel->portaria</td>
                  <td>$imovel->bairro</td>
                  <td>$imovel->cod_cliente</td>
                  <td>$imovel->nome_proprietario</td>
                </tr> 
                ";
              }
            }
          ?> 

        </tbody>
      </table>

      <?php
        if ($msgErro != "")
          echo "<p class='text-danger'>A operação não pode ser realizada: $msgErro</p>";
      ?>

    </div>

    <!-- Footer -->
    <?php include "./../static/footer.php"; ?>

</body>

</html>