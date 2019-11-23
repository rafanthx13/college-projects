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
	$telphone            = filter_form($_POST["telphone"]);
  $telphone_celphone   = filter_form($_POST["telphone_celphone"]);
  $telphone_contact    = filter_form($_POST["telphone_contact"]);
  $cep                 = filter_form($_POST["cep"]);
  $city                = filter_form($_POST["city"]);
  $bairro              = filter_form($_POST["bairro"]);
  $address             = filter_form($_POST["address"]);
  $numero              = filter_form($_POST["numero"]);
  $ingresso            = filter_form($_POST["date_enter"]);
  $cargo               = filter_form($_POST["cargo"]);
  $user                = filter_form($_POST["user"]);
  $salario             = filter_form($_POST["salario"]);
  $password            = hash('sha512', filter_form($_POST["password"]));


	try {    
		$conn = connectMySQL();

		$sql = "
      INSERT INTO `Funcionario` 
      (`nome`, `cpf`, `email`, `telefone`, `telefone_celular`,`telefone_contato`,
       `endereco`, `cep`, `cidade`, `bairro`, `numero`, `ingresso`,
        `cargo`, `salario`, `login`, `senha`) 
      VALUES
      ( '$nome', '$cpf', '$email', '$telphone', '$telphone_celphone', '$telphone_contact',
       '$address', '$cep', '$city', '$bairro', $numero, '$ingresso',
        '$cargo', $salario, '$user', '$password');
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

    <h2>Cadastrar Funcionários</h2>

    <form class="form-group" method="POST"
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
          <input type="email" name="email" id="email" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="telphone">Telefone</label>
          <input type="text" name="telphone" id="telphone" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="telphone_celphone">Telefone Celular</label>
          <input type="number" name="telphone_celphone" id="telphone_celphone" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="telphone_contact">Telefone Contato</label>
          <input type="text" name="telphone_contact" id="telphone_contact" class="form-control">
        </div>
      </div>

      <div class="row py-1">
        <div class="col-sm-2">
          <label for="cep">CEP</label>
          <input type="text" name="cep" id="cep" 
            placeholder="#####-###" class="form-control"
            pattern="[0-9]{5}-[\d]{3}" required maxlength="9" 
            onkeyup="buscaEndereco(this.value, 'funcionario')"
          >
        </div>
        <div class="col-sm-2">
          <label for="city">Cidade</label>
          <input type="text" name="city" id="city" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="bairro">Bairro</label>
          <input type="number" name="bairro" id="bairro" class="form-control">
        </div>
        <div class="col-sm-2">
          <label for="address">Endereço</label>
          <input type="text" name="address" id="address" class="form-control">
        </div>
        <div class="col-sm-1">
          <label for="numero">Número</label>
          <input type="number" name="numero" id="numero" class="form-control">
        </div>
      </div>

      <div class="row py-1">
        <div class="col-sm-2">
            <label for="cargo">Cargo</label>
            <input type="text" name="cargo" id="cargo" class="form-control" required>
          </div>
          <div class="col-sm-2">
            <label for="salario">Salario</label>
            <input type="number" name="salario" id="salario" class="form-control" required>
          </div>
          <div class="col-sm-2">
            <label for="date_enter">Data de Engresso</label>
            <input type="date" name="date_enter" id="date_enter" class="form-control" required>
          </div>
      </div>

      <div class="row py-1">
        <div class="col-sm-2">
          <label for="user">Usuário</label>
          <input type="text" name="user" id="user" class="form-control" required>
        </div>
        <div class="col-sm-2">
          <label for="password">Senha</label>
          <input type="password" name="password" id="password" class="form-control" required>
        </div>
        <div class="col-sm-7 py-1 align-items-end submit-button">
          <button type="reset" class="btn btn-default btn-sm">Resetar</button>
          <button type="submit" class="btn btn-success btn-sm">Enviar</button>
        </div>
      </div>

    </form>

    <?php 
      if(isset($msgErro)){
        if( $msgErro == ""){
          $modalTitle = "Sucesso";
          $modalContent = "O Funcionário foi cadastrado com Sucesso!";
          include "./../static/modal_template.php";
        }else{
          $modalTitle = "Error";
          $modalContent = "Erro ao cadastrar o funcionário! <br/>" . $msgErro . "\n";
          include "./../static/modal_template.php";
        }
      }
    ?>

  </div>

  <!-- Footer -->
  <?php include "./../static/footer.php"; ?>

</body>

</html>
