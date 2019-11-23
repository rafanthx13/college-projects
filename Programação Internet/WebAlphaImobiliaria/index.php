<?php

// session_start();

require_once("./src/utils/dir_functions.php");

?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Alpha Imobiliaria - Home</title>

  <script src="./app/lib/jquery-3.4.1.min.js"></script>
  <script src="./app/lib/popper.min.js"></script>
  <script src="./app/lib/bootstrap-4.1.3-dist/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="./app/lib/bootstrap-4.1.3-dist/css/bootstrap.min.css">

<!-- 

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

-->

  <link rel="icon" href="./app/img/logo-icon.ico">
  <link rel="stylesheet" href="./app/css/style.css">
  <script src="./app/js/login.js"></script>

</head>

<body>

  <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./app/template/static/public_header.php"; ?>
    <?php include "./app/template/static/public_navbar.php"; ?>
  </div>

  <!-- main -->
  <div class="container">

    <h1 class="center-private mt-5">Alpha Imobiliária - Home</h1>

  </div>

  <!-- Footer and LoginModal -->
  <?php include "./app/template/static/footer.php"; ?>
  <?php include "./app/template/static/login_modal.php"; ?>

  <?php 
    if(isset($_GET["page"])){
      if( strcmp($_GET["page"], "no_session") == 0){
        $modalTitle = "Error de Acesso à Área Privada";
        $modalContent = "Sessão não iniciada! Acesso Negado!";
        include "./app/template/static/modal_template.php";
      }
      if( strcmp($_GET["page"], "login_wrong") == 0){
        $modalTitle = "Login Inválido";
        $modalContent = " Usuário ou Senha Inválidos! Acesso Negado!";
        include "./app/template/static/modal_template.php";
        echo "<script>";
        echo "$('#meuModal').on('hidden.bs.modal', function (e) {";
        echo '  window.close();';
        echo '  close();';
        echo "});";
        echo "</script>";
      }
    }
  ?>

</body>

</html>
