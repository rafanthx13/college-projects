<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/bd/bd_querys.php");
require_once("./../../../src/utils/filter_input.php");


$msgErro = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    print_r($_POST);

    $objetivo               = filter_form($_POST["objetivo"]);     
    $tipo                   = filter_form($_POST["tipo"]);
    $nquartos               = filter_form($_POST["nquartos"]);
    $nbanheiros             = filter_form($_POST["nbanheiros"]);
    $nsuites                = filter_form($_POST["nsuites"]);
    $ngaragem               = filter_form($_POST["ngaragem"]);
    $area                   = filter_form($_POST["area"]);
    $andar                  = filter_form($_POST["andar"]);
    $bairro                 = filter_form($_POST["bairro"]);
    $valorAluguel           = filter_form($_POST["valorAluguel"]);
    $valorCond              = filter_form($_POST["valorCond"]);
    $portaria               = filter_form($_POST["portaria"]);
    $descricao              = filter_form($_POST["descricao"]);
    $upload                 = filter_form($_POST["upload"]);  
    $cod_cliente            = filter_form($_POST["cod_cliente"]);  
  
    try {    
      $conn = connectMySQL();

      $sql = "
      INSERT INTO `Imovel` 
      (`objetivo`, `tipo`, `nro_quartos`, `nro_banheiros`, `nro_suites`, `nro_garagem`,
      `area`, `andar`, `bairro`, `valor_aluguel`, `valor_cond` , `portaria` , `descricao`, `cod_cliente`) 
      VALUES
      ( '$objetivo', '$tipo', $nquartos, $nbanheiros, $nsuites, $ngaragem,
      $area, $andar, '$bairro', $valorAluguel, $valorCond, $portaria, '$descricao', $cod_cliente)
      ;
      ";

      if (! $conn->query($sql)){
        throw new Exception($conn->error);
      }

    }	catch (Exception $e) {
      $msgErro = $e->getMessage();
    }

    // Avaliar Imagens
    if($msgErro != ""){
      // $fileName = $_FILES['myfile']['name'];
      if( isset($_FILES["img1"]) ){
        $img1 = $_FILES["img1"]["name"];
      }
      if( isset($_FILES["img2"]) ){
        $img2 = $_FILES["img2"]["name"];
      }
      if( isset($_FILES["img3"]) ){
        $img3 = $_FILES["img3"]["name"];
      }
      

    }
  
    if(isset($conection))
      $conection->close();
  }

  // AJAX
  try {
      $connection = connectMySQL();
      $arrayBairros = list_bairro($connection);  
      $arrayCli = list_cli($connection);  
  } catch (Exception $e) {
      $msgErro = $e->getMessage();
  }

  if(isset($conection))
      $conection->close();
  
  
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
    <script src="./../../js/search_neighborhood.js"></script>

    <script>
        $('#BSbtninfo').filestyle({
            buttonName: 'btn-info',
            buttonText: ' Select a File'
        });
    </script>
</head>

<body>

  <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./../static/private_header.php"; ?>
    <?php include "./../static/private_navbar.php"; ?>
  </div>

    <!-- main -->

    <div class="container">

        <h2>Cadastrar Imoveis</h2>
        
        <form class="form-group" method="POST" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" >
            <div class="row py-1">
                <div class="form-group col-sm-2">
                    <label for="objetivo">Objetivo:</label>
                    <select id="objetivo" name ="objetivo" class="form-control" required>
                        <option value="comprar" selected="selected">Vender</option>
                        <option value="alugar">Alugar</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="tipo">Tipo:</label>
                    <select id="tipo" name="tipo" class="form-control">
                        <option value="apto" selected="selected">Apartamento</option>
                        <option value="casa">Casa</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="nquartos">Nº de quartos:</label>
                    <select id="nquartos" name="nquartos" class="form-control">
                        <option value=1 selected="selected">1</option>
                        <option value=2>2</option>
                        <option value=3>3</option>
                        <option value=4>4</option>
                        <option value=5>5</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="nbanheiros">Nº de banheiros:</label>
                    <select id="nbanheiros" name="nbanheiros" class="form-control">
                        <option value=1 selected="selected">1</option>
                        <option value=2>2</option>
                        <option value=3>3</option>
                        <option value=4>4</option>
                        <option value=5>5</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="nsuites">Nº de suites:</label>
                    <select id="nsuites" name="nsuites" class="form-control">
                        <option value=1 selected="selected">1</option>
                        <option value=2>2</option>
                        <option value=3>3</option>
                        <option value=4>4</option>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="ngaragem">Vagas na garagem:</label>
                    <select id="ngaragem" name="ngaragem" class="form-control">
                        <option value=1>1</option>
                        <option value=2>2</option>
                        <option value=3>3</option>
                        <option value=4>4</option>
                    </select>
                </div>
            </div>

            <div class="row py-1">
                <div class="col-sm-2">
                    <label for="area">Area construida:</label>
                    <input type="number" name="area" id="area" class="form-control" placeholder="44.00" required >
                    </select>
                </div>
                <div class="col-sm-2">
                    <label for="andar">Informe o andar(apto):</label>
                    <select id="andar" name="andar" class="form-control">
                        <option value=0 selected="selected">0</option>
                        <option value=1>1</option>
                        <option value=2>2</option>
                        <option value=3>3</option>
                        <option value=4>4</option>
                    </select>
                    </select>
                </div>
                <div class="form-group col-sm-2">
                    <label for="bairro">Bairro:</label>
                    <select id="bairro" name="bairro" class="form-control"  required>
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
                    <label for="valorAluguel"> Valor do aluguel </label>
                    <div class="input-group-prepend col ">
                        <span class="input-group-text">$</span>
                        <input type="currency" class="form-control" id="valorAluguel" name="valorAluguel" required>
                    </div>
                </div>
                <div class="form-group col-sm-2">
                    <label for="valorCond"> Valor do condominio</label>
                    <div class="input-group-prepend col">
                        <span class="input-group-text">$</span>
                        <input type="currency" class="form-control" id="valorCond" name="valorCond" required>
                    </div>
                </div>
                <div class="form-group col-sm-2">
                    <br><br>
                    <input type="checkbox" value="1" id="portaria" name="portaria" required>Portaria<br>
                </div>

            </div>
            <div class="row py-1">
                <div class="col-sm-6">
                    <label for="descricao">Descrição:</label>
                    <textarea name="descricao" id="descricao" class="form-control" rows="5" required></textarea>
                </div>
                <div class="col-sm-3">
                    <label for="cod_cliente">Proprietario:</label>
                    <select name="cod_cliente" id="cod_cliente" class="form-control" required>
                    <?php
                    if ($arrayCli != null) {
                        foreach ($arrayCli as $cli) { 
                        echo " <option value=\"$cli->cod_cliente\">$cli->nome</option> ";
                        }
                    }
                    ?>  
                    </select>
                </div>
            </div>
            <div class="row py-1">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="img1">Fotos do imovel, selecione o arquivo:</label>
                        <input type="file" class="form-control-file" name="img1" id="img1">
                    </div>
                </div>
            </div>

            <div class="row py-1">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="img2">Fotos do imovel, selecione o arquivo:</label>
                        <input type="file" class="form-control-file" name="img2" id="img2">
                    </div>
                </div>
            </div>
            <div class="row py-1">
                <div class="col-sm-12">
                    <div class="form-group">
                        <label for="img3">Fotos do imovel, selecione o arquivo:</label>
                        <input type="file" class="form-control-file" name="img3" id="img3">
                    </div>
                </div>
            </div>
            <!-- fazer essa função-->
            <!-- <button type="button" onclick="" class="btn btn-info btn-sm">Adicionar mais
                fotos</button> -->
            <div style="float: right;" class="py-1">
                <button type="reset" class="btn btn-danger btn-sm">Resetar</button>
                <button type="submit" class="btn btn-success btn-sm">Enviar</button>
            </div>

        </form>

        <?php 
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            if(isset($msgErro)){
                if( $msgErro == "" ){
                $modalTitle = "Sucesso";
                $modalContent = "O imovel foi cadastrado com sucesso!";
                include "./../static/modal_template.php";
            } else {
                $modalTitle = "Error";
                $modalContent = "Erro ao cadastrar o imovel! <br/>" . $msgErro . "\n";
                include "./../static/modal_template.php";
                }
            }
        }
        ?>
    </div>

    <!-- Footer -->
     <?php include "./../static/footer.php"; ?>

</body>

</html>
