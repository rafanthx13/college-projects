<?php

require_once("./../../../src/utils/dir_functions.php");

?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Alpha Imobiliaria</title>

  <script src="./../../lib/jquery-3.4.1.min.js"></script>
  <script src="./../../lib/popper.min.js"></script>
  <script src="./../../lib/bootstrap-4.1.3-dist/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="./../../lib/bootstrap-4.1.3-dist/css/bootstrap.min.css">
  <link rel="icon" href="./../../img/logo-icon.ico">
  <link rel="stylesheet" href="./../../css/style.css">

</head>

<body>

  <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./../static/public_header.php"; ?>
    <?php include "./../static/public_navbar.php"; ?>
  </div>

  <!-- main -->
  <div class="container">

    <img class="logoMain img-thumbnail" src="./../../img/whoWeAre.jpg" alt="">
    <br>
    <h2>Missão</h2>

    <p>
      Oferecer serviços para o mercado imobiliário com excelência, superando as expectativas e
      gerando valor e satisfação para os clientes colaboradores e sociedade.
    </p>

    <h2>Visão</h2>

    <p>Ser líder de mercado e referência em soluções e serviços imobiliários</p>


    <h2>Valores</h2>

    <ul>
      <li>Transparência</li>
      <li>Equipe</li>
      <li>Inovação</li>
      <li>Comprometimento</li>
      <li>Exelência</li>
    </ul>

  </div>

  <!-- Footer and LoginModal -->
  <?php include "./../static/footer.php"; ?>
  <?php include "./../static/login_modal.php"; ?>

</body>

</html>