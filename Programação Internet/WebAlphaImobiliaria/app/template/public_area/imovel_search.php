<?php
session_start();
require_once("./../../../src/utils/dir_functions.php");
require_once("./../../../src/bd/connection.php");

require_once("./../../../src/bd/bd_querys.php");

try {
    $msgErro = "";
    $connection = connectMySQL();
    $arrayBairros = list_bairro($connection);  
} catch (Exception $e) {
	$msgErro = $e->getMessage();
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Alpha Imobiliaria</title>

    <script src="../../lib/jquery-3.4.1.min.js"></script>
    <script src="../../lib/popper.min.js"></script>
    <script src="../../lib/bootstrap-4.1.3-dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="../../lib/bootstrap-4.1.3-dist/css/bootstrap.min.css">
    <link rel="icon" href="./../../img/logo-icon.ico">
    <link rel="stylesheet" href="./../../css/style.css">
    <script src="./../../js/search_neighborhood.js"></script>

</head>

<body>

  <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./../static/public_header.php"; ?>
    <?php include "./../static/public_navbar.php"; ?>
  </div>

    <!-- main -->
    <div class="container img-background">

        <form class="form" method="GET" action="./imovel_list.php">

            <div class="row">
                <div class="form-group col-sm-2">
                    <label for="objetivo">Objetivo </label>
                    <select id="objetivo" name="objetivo" class="form-control">
                        <option value="comprar" selected>Comprar</option>
                        <option value="alugar">Alugar</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="bairro">Bairro </label>
                    <select id="bairro" name="bairro" class="form-control">
                        <?php
                        if ($arrayBairros != null) {
                            foreach ($arrayBairros as $bar) { 
                            echo " <option value=\"$bar->bairro\">$bar->bairro</option> ";
                            }
                        }
                        ?>  
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="valorMin"> Minimo </label>
                    <div class="input-group-prepend col">
                        <span class="input-group-text">$</span>
                        <input type="text" class="form-control" id="valorMin" 
                            name= "valorMin" placeholder="Minimo" aria-label="Amount">
                    </div>
                </div>
                <div class="form-group col-sm-2">
                    <label for="valorMax"> Maximo</label>
                    <div class="input-group-prepend col">
                        <span class="input-group-text">$</span>
                        <input type="currency" class="form-control" id="valorMax" name="valorMax" placeholder="Maximo">
                    </div>
                </div>
                <div class="form-group col-sm-4">
                    <label for="informacoes">Informações adicionais</label>
                    <input type="text" class="form-control" id="informacoes" name="informacoes" placeholder="Observações">
                </div>
            </div>

            <button type="submit" class="btn btn-success">
              Buscar
            </button>
        </div>

    </form>

    <!-- Footer and LoginModal -->
  <?php include "./../static/footer.php"; ?>
  <?php include "./../static/login_modal.php"; ?>
  
</body>

</html>