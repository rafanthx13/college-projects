<?php

require_once("./connection.php");
require_once("./../utils/filter_input.php");

class Endereco {
	public $rua;
	public $bairro;
	public $cidade;
}

try {
	$conn = connectMySQL();

	$cep = "";
	if (isset($_GET["cep"]))
    $cep = filter_form($_GET["cep"]);

	$SQL = "
		SELECT endereco, bairro, cidade
		FROM Funcionario
    WHERE CEP = '$cep'
    UNION
    SELECT logradouro as endereco, bairro, ''
		FROM Cliente_proprietario
    WHERE CEP = '$cep'
    ;
  ";
  
	if (! $result = $conn->query($SQL))
		throw new Exception('Ocorreu uma falha ao buscar o endereco: ' . $conn->error);
	
	if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
		$endereco = new Endereco();

		$endereco->rua    = $row["endereco"];
		$endereco->bairro = $row["bairro"];
    $endereco->cidade = $row["cidade"];	
    
		// IMPORTANTE: a função json_encode exige que toda string no objeto esteja codificada como UTF-8.
		// Erros são comuns quando o MySQL utiliza outros padrões de codificação para caracteres
		// especiais, como cedilhas e acentos.
		if (! $jsonStr = json_encode($endereco))
			throw new Exception("Falha na funcao json_encode do PHP");
		
		echo $jsonStr;
	} 
} catch (Exception $e) {
	echo $e->getMessage();
}

if ($conn != null)
	$conn->close();

?>