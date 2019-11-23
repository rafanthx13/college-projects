<?php

session_start();

require_once("./../utils/filter_input.php");
require_once("./connection.php");

function login_user($user, $password, $mysqli){

  $SQL = "
    SELECT cod_funcionario, login, senha
    FROM Funcionario
    WHERE login = ?
    LIMIT 1;
  ";

  try {
    $user = filter_form($user);
    $stmt = $mysqli->prepare($SQL);
    $stmt->bind_param('s', $user);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($cod_funcionario, $nomeUsuario, $password_hash);
    $stmt->fetch();
  } catch (Exception $e) {
    return false;
  }
  
  if ($stmt->num_rows == 1){
    $hashed_password = hash('sha512', $password);
    if (strcmp($hashed_password, $password_hash) == 0) {
            
      // Senha Correta: Dados de sessão
      $_SESSION['user_id'] = $cod_funcionario;
      $_SESSION['user_name'] = $nomeUsuario;
      $_SESSION['login_key'] = hash('sha512', $password_hash . $_SERVER['HTTP_USER_AGENT']);
      
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}


if ($_SERVER["REQUEST_METHOD"] == "GET") {

  try {

    $user     = $_GET["user"];     
    $password = $_GET["password"];
    $conection = connectMySQL();
    
    if(login_user($user, $password, $conection)){
      // header("Location: ../../../alpha/app/template/private_area/private_index.php"); // localhost
      header("Location: ../../../app/template/private_area/private_index.php");
      exit();
    } else {
      session_destroy();
      // header("Location: ../../../alpha/index.php?page=login_wrong"); // localhost
      header("Location: ../../../index.php?page=login_wrong");
      exit();
    }

  } catch (Exception $e) {
    http_response_code(500);
    $msgErro = $e->getMessage();
    echo $msgErro;
  }

  $conection->close();
  
}

?>