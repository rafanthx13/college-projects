<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/bd/bd_querys.php");

try {
  $msgErro = "";
	$connection = connectMySQL();
	$arrayInteresses = list_interest($connection);  
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
  <title>Listagem Interesses</title>

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

    <h2>Listagem de Interesses em Imóveis</h2>

    <table class="table table-hover table-sm">
      <thead>
        <tr>
          <th scope="col">Nome Interessado</th>
          <th scope="col">Email</th>
          <th scope="col">Telefone</th>
          <th scope="col">Comentário</th>
          <th scope="col">ID Proprietario</th>
          <th scope="col">Nome Proprietario</th>
          <th scope="col">Email Proprietario</th>
          <th scope="col">Telefone Proprietario</th>
          <th scope="col">ID Imovel</th>
          <th scope="col">Descrição Imóvel</th>
          <th scope="col">Bairro Imóvel</th>
        </tr>
      </thead>

      <tbody>

        <?php
          if ($arrayInteresses != null) {
            foreach ($arrayInteresses as $inte) { 
              echo "
              <tr>
                <td scope=\"row\">$inte->nome_interressado</td>
                <td>$inte->email</td>
                <td>$inte->telefone</td>
                <td>$inte->comentario</td>
                <td>$inte->id_proprietario</td>
                <td>$inte->nome_proprietario</td>
                <td>$inte->email_proprietario</td>
                <td>$inte->telefone_proprietario</td>
                <td>$inte->id_imovel</td>
                <td>$inte->desc_imovel</td>
                <td>$inte->bairro_imovel</td>
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