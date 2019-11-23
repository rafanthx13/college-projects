<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/bd/bd_querys.php");

try {
  $msgErro = "";
	$connection = connectMySQL();
	$arrayClientes = list_clients($connection);  
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
  <title>Alpha Imobiliaria</title>

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

    <h2>Listagem de Clientes Proprietários</h2>

    <table class="table table-hover table-sm">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Nome</th>
          <th scope="col">CPF</th>
          <th scope="col">E-mail</th>
          <th scope="col">Telefone</th>
          <th scope="col">Sexo</th>
          <th scope="col">Profissão</th>
          <th scope="col">Estado Civil</th>
          <th scope="col">CEP</th>
          <th scope="col">Bairro</th>
          <th scope="col">Logradouro</th>
          <th scope="col">Número</th>
        </tr>
      </thead>

      <tbody>
      <?php
          if ($arrayClientes != null) {
            foreach ($arrayClientes as $cli) { 
              echo "
              <tr>
                <th scope=\"row\">$cli->cod_cliente</th>
                <td>$cli->nome</td>
                <td>$cli->cpf</td>
                <td>$cli->email</td>
                <td>$cli->telefone</td>
                <td>$cli->sexo</td>
                <td>$cli->profissao</td>
                <td>$cli->estado_civil</td>
                <td>$cli->cep</td>
                <td>$cli->bairro</td>
                <td>$cli->logradouro</td>
                <td>$cli->numero</td>
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