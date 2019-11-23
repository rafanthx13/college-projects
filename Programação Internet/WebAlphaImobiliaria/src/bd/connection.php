<?php

// LocalHost
// define("HOST"    , "localhost"); 
// define("USER"    ,  "root");
// define("PASSWORD", ""); 
// define("DATABASE", "3198912_trabalho");


// Site
define("HOST"    , "fdb23.awardspace.net"); 
define("USER"    ,  "3198912_trabalho");
define("PASSWORD", "alphaimobiliaria1"); 
define("DATABASE", "3198912_trabalho");

function connectMySQL(){
	$conn = new mysqli(HOST, USER, PASSWORD, DATABASE);
	if ($conn->connect_error){
		throw new Exception('Falha na conexão com o MySQL: ' . $conn->connect_error);
		die("Algo Bizarro aconteceu");
	}
	return $conn;   
}

?>
