<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/bd/bd_querys.php");

try {
  $msgErro = "";
	$connection = connectMySQL();
	$arrayFuncionarios = list_employes($connection);  
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
  <title>Listagem de Funcionários</title>

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

  <!-- main -->

  <div class="container">

    <h2>Listagem de Funcionários</h2>

    <table class="table table-hover table-sm">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Nome</th>
          <th scope="col">CPF</th>

          <th scope="col">E-Mail</th>
          <th scope="col">Telefone</th>
          <th scope="col">Endereço</th>

          <th scope="col">CEP</th>
          <th scope="col">Ingresso</th>
          <th scope="col">Cargo</th>

          <th scope="col">Salário</th>
          <th scope="col">Usuário</th>
        </tr>
      </thead>
      <tbody>
        
        <?php
          if ($arrayFuncionarios != null) {
            foreach ($arrayFuncionarios as $fun) { 
              $formated_date = date_format(date_create($fun->ingresso), "d/m/Y");
              echo "
              <tr>
                <th scope=\"row\">$fun->cod_funcionario</th>
                <td>$fun->nome</td>
                <td>$fun->cpf</td>

                <td>$fun->email</td>
                <td>$fun->telefone</td>
                <td>$fun->endereco</td>

                <td>$fun->cep</td>
                <td>$formated_date</td>
                <td>$fun->cargo</td>

                <td>$fun->salario</td>
                <td>$fun->login</td>
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