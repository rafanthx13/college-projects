<?php

// bd_querys.php :: Por as funções que acessam o banco de dados

function cadastraUsuario($conn, $nome, $email, $senha) {
  $SQL = "
    SELECT Email
    FROM Usuario
    WHERE Email = '$email'
  ";
  
  if (!$resultado = $conn->query($SQL))
    throw new Exception('Falha ao buscar usuario: ' . $conn->error);
  if ($resultado->num_rows > 0)
    throw new Exception('Email ja cadastrado');
  
  // Cria uma senha hash de 60 caracteres utilizando o algoritmo
  // padrão (atualmente, o bcrypt)
  $senhaHash = password_hash($senha, PASSWORD_DEFAULT);
  $SQL = "
    INSERT INTO Usuario (Nome, Email, SenhaHash)
    VALUES ('$nome', '$email', '$senhaHash');
  ";
  
  if (!$conn->query($SQL))
    throw new Exception('Falha ao cadastrar usuario: ' . $conn->error);  
}

/* Listagem de Clientes Proprietarios */

class ClienteProprietario {
  public $cod_cliente;
  public $nome;
  public $cpf;
  public $email;
  public $telefone;
  public $sexo;
  public $profissao;
  public $estado_civil;
  public $cep;
  public $bairro;
  public $logradouro;
  public $numero;
}

function list_clients($connection) {

  $arrayClientes = null;

  $SQL = "
    SELECT *
    FROM Cliente_proprietario;
  ";

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para listagem de Clientes Proprietarios: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $client = new ClienteProprietario();
			$client->cod_cliente  = $row["cod_cliente"];
			$client->nome         = $row["nome"];
			$client->cpf          = $row["cpf"];
			$client->email        = $row["email"];
      $client->telefone     = $row["telefone"];
      $client->sexo         = $row["sexo"];
      $client->profissao    = $row["profissao"];
      $client->estado_civil = $row["estado_civil"];
      $client->cep          = $row["cep"];
      $client->bairro       = $row["bairro"];
      $client->logradouro   = $row["logradouro"];
      $client->numero       = $row["numero"];
      
      $arrayClientes[] = $client;
    }
  }

  return $arrayClientes;

}

/* Listagem de Funcionários */

class Funcionario {
  public $cod_funcionario;
  public $nome;
  public $cpf;
  public $email;
  public $telefone;
  public $endereco;
  public $cep;
  public $ingresso;
  public $cargo;
  public $salario;
  public $login;
}

function list_employes($connection) {

  $arrayFuncionarios = null;

  $SQL = "
    SELECT *
    FROM Funcionario;
  ";

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para listagem de Funcionarios: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $funcionario = new Funcionario();
			$funcionario->cod_funcionario = $row["cod_funcionario"];
			$funcionario->nome            = $row["nome"];
			$funcionario->cpf             = $row["cpf"];
			$funcionario->email           = $row["email"];
      $funcionario->telefone        = $row["telefone"];
      $funcionario->endereco        = $row["endereco"];
      $funcionario->cep             = $row["cep"];
      $funcionario->ingresso        = $row["ingresso"];
      $funcionario->cargo           = $row["cargo"];
      $funcionario->salario         = $row["salario"];
      $funcionario->login           = $row["login"];
      
      $arrayFuncionarios[] = $funcionario;
    }
  }

  return $arrayFuncionarios;

}
	
/* Listagem de Interesses de Imóveis*/

class Interesse {
  public $nome_interressado;
  public $email;
  public $telefone;
  public $comentario;
  public $id_proprietario;
  public $nome_proprietario;
  public $email_proprietario;
  public $telefone_proprietario;
  public $id_imovel;
  public $desc_imovel;
  public $bairro_imovel;
}

function list_interest($connection) {

  $arrayInteresses = null;

  $SQL = "
    SELECT 
      Interesse.nome as nome_interressado,
      Interesse.email as email,
      Interesse.telefone as telefone,
      Interesse.comentario as comentario,
      Interesse.cod_cliente as id_proprietario,
      Cliente_proprietario.nome as nome_proprietario,
      Cliente_proprietario.email as email_proprietario,
      Cliente_proprietario.telefone as telefone_proprietario,
      Interesse.cod_imovel as id_imovel,
      Imovel.descricao as desc_imovel,
      Imovel.bairro as bairro_imovel
    FROM Interesse 
      INNER JOIN Cliente_proprietario
        ON Interesse.cod_cliente = Cliente_proprietario.cod_cliente
      INNER JOIN Imovel
        ON Interesse.cod_imovel = Imovel.cod_imovel
    ;
  ";

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para listagem de Interesse de Imóveis: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $inte = new Interesse();
			$inte->nome_interressado     = $row["nome_interressado"];
			$inte->email                 = $row["email"];
			$inte->telefone              = $row["telefone"];
			$inte->comentario            = $row["comentario"];
      $inte->id_proprietario       = $row["id_proprietario"];
      $inte->nome_proprietario     = $row["nome_proprietario"];
      $inte->email_proprietario    = $row["email_proprietario"];
      $inte->telefone_proprietario = $row["telefone_proprietario"];
      $inte->id_imovel             = $row["id_imovel"];
      $inte->desc_imovel           = $row["desc_imovel"];
      $inte->bairro_imovel         = $row["bairro_imovel"];
      
      $arrayInteresses[] = $inte;
    }
  }

  return $arrayInteresses;


}

/* Listagem de Imóveis */

class Imovel {
  public $id;
  public $nro_quartos;
  public $nro_banheiros;
  public $nro_suites;
  public $nro_garagem;
  public $area;
  public $descricao;
  public $portaria;
  public $bairro;
  public $cod_cliente;
  public $nome_proprietario;
}

function list_imovel($connection) {

  $arrayImoveis = null;

  $SQL = "
    SELECT *
    FROM Imovel 
      INNER JOIN Cliente_proprietario
        ON Imovel.cod_cliente = Cliente_proprietario.cod_cliente
    ;
  ";

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para listagem de Interesse de Imóveis: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $imovel = new Imovel();
			$imovel->cod_imovel    = $row["cod_imovel"];
			$imovel->nro_quartos   = $row["nro_quartos"];
			$imovel->nro_banheiros = $row["nro_banheiros"];
			$imovel->nro_suites    = $row["nro_suites"];
      $imovel->nro_garagem   = $row["nro_garagem"];
      $imovel->area          = $row["area"];
      $imovel->descricao     = $row["descricao"];
      $imovel->portaria      = $row["portaria"];
      $imovel->bairro        = $row["bairro"];
      $imovel->cod_cliente   = $row["cod_cliente"];
      $imovel->nome_proprietario  = $row["nome"];
      
      $arrayImoveis[] = $imovel;
    }
  }

  return $arrayImoveis;

}

/* Listar por AJAX Bairros */

class Bairro {
  public $bairro;
}

function list_bairro($connection) {

  $arrayBairros = null;

  $SQL = "
    SELECT DISTINCT bairro 
    FROM Imovel;"
  ;

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para lsitar bairros: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $bairro = new Bairro();
			$bairro->bairro    = $row["bairro"];
      
      $arrayBairros[] = $bairro;
    }
  }

  return $arrayBairros;

}

/* Listar por AJAX Cli */

class Cli {
  public $cod_cliente;
  public $nome;
}

function list_cli($connection) {

  $arrayCli = null;

  $SQL = "
    SELECT cod_cliente, nome 
    FROM Cliente_proprietario;"
  ;

  $result = $connection->query($SQL);
	if (! $result)
		throw new Exception('Ocorreu uma falha ao Acessar Banco para lsitar bairros: ' . $connection->error);

	if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      $cli = new Cli();
      $cli->cod_cliente    = $row["cod_cliente"];
      $cli->nome    = $row["nome"];
      $arrayCli[] = $cli;
    }
  }

  return $arrayCli;

}

function handle_images($img1, $img2, $img3){
  
}


?>

