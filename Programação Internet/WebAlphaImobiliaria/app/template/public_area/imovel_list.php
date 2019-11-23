<?php

session_start();
require_once("./../../../src/utils/dir_functions.php");
require_once("./../../../src/bd/connection.php");

require_once("./../../../src/bd/bd_querys.php");

class Imgs_Imovel {
	public $cod_imovel;
	public $path;
}

$msgErro = "";

if ($_SERVER["REQUEST_METHOD"] == "GET") {

  try {
    $conn = connectMySQL();
    
    if(isset($_GET["bairro"])){
        $bairro = $_GET["bairro"];
    }

    $SQL = "
      SELECT *
      FROM Imovel
      WHERE BAIRRO = '$bairro'
      UNION
      SELECT path
      FROM Imgs_imovel
      WHERE Imovel.cod_imovel = Imgs_imovel.cod_imovel
      ;
    ";

    echo $SQL;
  
    if (! $result = $conn->query($SQL))
      throw new Exception('Ocorreu uma falha ao buscar as informações ' . $conn->error);
	
    if ($result->num_rows > 0) {
      var_dump($result);
      while ($row = $result->fetch_assoc()) {
        $row = $result->fetch_assoc();
        $Imovel = new Imovel();
        $Imgs_imovel = new Imgs_imovel();

        $Imovel->nro_quartos        = $row["nro_quartos"];
        $Imovel->nro_banheiros      = $row["nro_banheiros"];
        $Imovel->nro_suites         = $row["nro_suites"];
        $Imovel->nro_garagem        = $row["nro_garagem"];	
        $Imovel->area               = $row["area"];
        $Imovel->descricao          = $row["descricao"];
        $Imovel->portaria           = $row["portaria"]; 
        $Imovel->bairro             = $row["bairro"]; 
        $Imovel->andar              = $row["andar"];
        $Imovel->valor_aluguel      = $row["valor_aluguel"];
        $Imovel->valor_cond         = $row["valor_cond"];

        $Imgs_imovel->path          = $row["path"];
        $Imgs_imovel->cod_imovel    = $row["cod_imovel"];

        $arrayImovel[]              = $Imovel;
        $arrayImgs_imovel[]         = $Imgs_imovel;
      }
      print_r($arrayImgs_imovel);
    } 

  } catch (Exception $e) {
    echo $e->getMessage();
  }

}

if ($conn != null)
  $conn->close();
  
print_r($arrayImovel);
print_r($arrayImgs_imovel);


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

    <script>
        $(document).ready(function () {

            $(".imgModal").each(function (i) {
                $(this).delay(300 * i).fadeIn();
            });

            $(".imgGalery").each(function (i) {
                $(this).delay(200 * i).fadeIn();
            });

            $(".imgGalery").hover(

                function () {
                    $(this).animate({
                        width: '280px',
                        height: '250px'
                    });
                },

                function () {
                    $(this).animate({
                        width: '230px',
                        height: '200px'
                    });
                }
            );

        });

        $('#listModal').on('shown.bs.modal', function () {
            $('#myInput').trigger('focus')
        })
    </script>


</head>

<body>

    <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./../static/public_header.php"; ?>
    <?php include "./../static/public_navbar.php"; ?>
  </div>

    <br><br>
    <!-- main -->
    <div class="container">
        <div class="aptosList">
            <h1>Informações sobre os apartamentos</h1>
            <table class="right">
                <tr>
                    <td>
                        <h2 class="aptoSelecionadosBairros">Santa monica</h2>
                        <p class="aptoSelecionados">Suítes: 1 , Banheiros: 1 , Salas: 1 , Quartos: 2 , Garagens: 1,
                            Área construida: 72.00 m², Área total: 72.00 m² </p>
                        <button type="button" class="btn btn-info btn-sm" data-toggle="modal"
                            data-target="#listModal">Mais Fotos</button>
                        <button style="float: right; " type="button" class="btn btn-danger btn-sm" data-toggle="modal"
                            data-target="#interesseModal">Tenho
                            Interesse</button>
                    </td>
                    <td><img class="imgGalery" src="../../img/apto1-0.jpeg" id="img01"></td>
                    <td><img class="imgGalery" src="../../img/apto1-1.jpeg" id="img02"></td>
                    <td><img class="imgGalery" src="../../img/apto1-2.jpeg" id="img03"></td>
                </tr>
            </table>
        </div>
        <div class="aptosList">
            <table class="center">
                <tr>
                    <td>
                        <h2 class="aptoSelecionadosBairros">Santa monica</h2>
                        <p class="aptoSelecionados">Quartos: 1 , Banheiros: 1 , Garagens: 1 , Salas: 1,
                            Área construida: 60.00 m², Área total: 65.00 m² </p>
                        <button type="button" class="btn btn-info btn-sm" data-toggle="modal"
                            data-target="#listModal">Mais Fotos</button>
                        <button style="float: right; " type="button" class="btn btn-danger btn-sm" data-toggle="modal"
                            data-target="#interesseModal">Tenho
                            Interesse</button>
                    </td>
                    <?php
			            if ($arrayImgs_imovel != null)
			                {
				                foreach ($arrayImgs_imovel as $Imgs_imovel)
				                {       
					                echo "
                                    <tr>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img05\"></td>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img06\"></td>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img07\"></td>
					                 </tr> 
					                ";
				                }
			                }
		            ?>  
                </tr>
            </table>
        </div>
        <div class="aptosList">
            <table class="center">
                <tr>
                    <td>
                        <h2 class="aptoSelecionadosBairros">Tibery</h2>
                        <p class="aptoSelecionados">Suítes: 1 , Garagens: 1 , Salas: 1 , Banheiros: 2 , Quartos: 3 ,
                            Área construida: 72.00 m², Área total: 72.00 m² </p>
                        <button type="button" class="btn btn-info btn-sm" data-toggle="modal"
                            data-target="#listModal">Mais Fotos</button>
                        <button style="float: right; " type="button" class="btn btn-danger btn-sm" data-toggle="modal"
                            data-target="#interesseModal">Tenho
                            Interesse</button>
                    </td>
                    <?php
			            if ($arrayImgs_imovel != null)
			                {
				                foreach ($arrayImgs_imovel as $Imgs_imovel)
				                {       
					                echo "
                                    <tr>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img05\"></td>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img06\"></td>
                                    <td><img class=\"imgGalery\" src=\"$Imgs_imovel->path\" id=\"img07\"></td>
					                 </tr> 
					                ";
				                }
			                }
		            ?>  
                </tr>
            </table>
        </div>

    </div>

    <!-- Footer and LoginModal -->
  <?php include "./../static/footer.php"; ?>
  <?php include "./../static/login_modal.php"; ?>

    <!--Modal list-->
    <div class="modal fade " id="listModal" role="dialog">
        <div class="modal-dialog modal-lg">

            <!-- Conteúdo -->
            <div class="modal-content">

                <div class="modal-header">
                    <h6 class="modal-title text-align: center">Mais Fotos</h6>
                    <img style="width: 10%;" src="../../img/logo-form.png" alt="">
                </div>

                <div class="modal-body">
                    <p class="codigoApto">Codigo 11234</p>
                    <p class="maisInfoApto">Apartamento com 02 quartos, Sala c/ sacada, banheiro social, cozinha
                        conjugada c/ área de serviço,
                        estacionamento p/01 vaga. Cond. aprox.280,00 tem taxa de mudança entrada e saida. </p>
                    <img class="imgModal py-3" src="../../img/apto1-0.jpeg" id="img01">
                    <img class="imgModal py-3" src="../../img/apto1-1.jpeg" id="img02">
                    <img class="imgModal py-3" src="../../img/apto1-2.jpeg" id="img03">
                    <img class="imgModal py-3" src="../../img/apto1-3.jpeg" id="img04">
                    <img class="imgModal py-3" src="../../img/apto1-0.jpeg" id="img05">
                    <img class="imgModal py-3" src="../../img/apto1-1.jpeg" id="img06">
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-dismiss="modal">Voltar</button>
                </div>
            </div>

        </div>
    </div>

    <!-- Modal tenho interesse -->
    <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">

                <div class="modal-header">
                    <h6 class="modal-title" id="exampleModalLabel">Tela de Login</h5>
                        <img style="width: 20%;" src="../../img/logo-form.png" alt="">
                </div>

                <div class="modal-body">
                    <div class="container">
                        <form action="">
                            <div class="form-group row">
                                <label for="user">Usuário</label>
                                <input type="text" name="user" id="user" class="form-control"
                                    placeholder="Digite o usuário">
                            </div>
                            <div class="form-group row">
                                <label for="password">Senha</label>
                                <input type="text" name="password" id="password" class="form-control"
                                    placeholder="Digite a Senha">
                            </div>

                        </form>
                    </div>
                </div>

                <div class="modal-footer">
                    <button class="btn btn-danger btn-sm" data-dismiss="modal">Close</button>
                    <button class="btn btn-success btn-sm"
                        onclick="document.location.href='./../private_area/private_index.html'"
                    >Entrar</button>
                </div>

            </div>
        </div>
    </div>

</body>

</html>
