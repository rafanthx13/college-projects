<?php

session_start();
require_once("./../../../src/bd/connection.php");
require_once("./../../../src/bd/authenticate.php");
autentify();

require_once("./../../../src/utils/filter_input.php");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $msgErro = "";

	$nome                = filter_form($_POST["nome"]);     
  $cpf                 = filter_form($_POST["cpf"]);
  $email               = filter_form($_POST["email"]);
	$telefone            = filter_form($_POST["telefone"]);
  $sexo                = filter_form($_POST["sexo"]);
  $estado_civil        = filter_form($_POST["estado_civil"]);
  $profissao           = filter_form($_POST["profissao"]);
  $cep                 = filter_form($_POST["cep"]);
  $bairro              = filter_form($_POST["bairro"]);
  $logradouro          = filter_form($_POST["logradouro"]);
  $numero              = filter_form($_POST["numero"]);

	try {    
		$conn = connectMySQL();

		$sql = "
      INSERT INTO `Cliente_proprietario` 
      (`nome`, `cpf`, `email`, `telefone`, `sexo`, `profissao`,
       `estado_civil`, `cep`, `bairro`, `logradouro`, `numero`) 
      VALUES
      ( '$nome', '$cpf', '$email', '$telefone', '$sexo', '$profissao',
       '$estado_civil', '$cep', '$bairro', $logradouro, $numero)
      ;
		";

		if (! $conn->query($sql)){
      throw new Exception($conn->error);
    }

	}	catch (Exception $e) {
    $msgErro = $e->getMessage();
  }

  if(isset($conection))
    $conection->close();
  
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
  <script src="./../../js/search_address.js"></script>

</head>

<body>

  <!-- Header and NavBar -->
  <div class="sticky-top">
    <?php include "./../static/private_header.php"; ?>
    <?php include "./../static/private_navbar.php"; ?>
  </div>

  <!-- Main -->
  <div class="container">

    <h2>Cadastrar Usuários</h2>

    <form  class="form-group" method="POST"
      action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>"
    >

      <div class="row py-1">
        <div class="col-sm-2">
          <label for="nome">Nome</label>
          <input type="text" name="nome" id="nome" class="form-control" required>
        </div>
        <div class="col-sm-2">
          <label for="cpf">CPF</label>
          <input type="text" name="cpf" id="cpf" class="form-control" required>
        </div>
        <div class="col-sm-2">
          <label for="email">Email</label>
          <input type="email" name="email" id="email" class="form-control" required>
        </div>
        <div class="col-sm-2">
          <label for="telefone">Telefone</label>
          <input type="text" name="telefone" id="telefone" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="sexo">Sexo</label>
          <select name="sexo" id="sexo" class="form-control">
            <option value="male">Homem</option>
            <option value="female">Mulher</option>
          </select>
        </div>
        <div class="col-sm-2">
          <label for="estado_civil">Estado Civil</label>
          <select name="estado_civil" id="estado_civil" class="form-control">
            <option value="Casado">Casado(a)</option>
            <option value="Solteiro">Solteiro(a)</option>
            <option value="Divorciado">Divorciado(a)</option>
            <option value="Viuvo">Viuvo(a)</option>
          </select>
        </div>
      </div>

      <div class="row py-1">
        <div class="col-sm-2">
          <label for="profissao">Profissão</label>
          <input type="text" name="profissao" id="profissao" class="form-control" >
        </div>
        <div class="col-sm-2">
          <label for="cep">CEP</label>
          <input type="text" name="cep" id="cep" 
            placeholder="#####-###" class="form-control"
            pattern="[0-9]{5}-[\d]{3}" required maxlength="9" 
            onkeyup="buscaEndereco(this.value, 'cliente')"
          >
        </div>
        <div class="col-sm-2">
          <label for="bairro">Bairro</label>
          <input type="text" name="bairro" id="bairro" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="logradouro">Logradouro</label>
          <input type="text" name="logradouro" id="logradouro" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="numero">Número</label>
          <input type="number" name="numero" id="numero" class="form-control">
        </div>
        <div class="col-sm-2 py-1 align-items-end submit-button">
          <button type="reset" class="btn btn-default btn-sm">Resetar</button>
          <button type="submit" class="btn btn-success btn-sm">Enviar</button>
        </div>
      </div>

    </form>

    <?php 
      if(isset($msgErro)){
        if( $msgErro == "" ){
          $modalTitle = "Sucesso";
          $modalContent = "O Cliente foi cadastrado com Sucesso!";
          include "./../static/modal_template.php";
        } else {
          $modalTitle = "Error";
          $modalContent = "Erro ao cadastrar o cliente! <br/>" . $msgErro . "\n";
          include "./../static/modal_template.php";
        }
      }
    ?>

  </div>

  <!-- Footer -->
  <?php include "./../static/footer.php"; ?>

</body>

</html>