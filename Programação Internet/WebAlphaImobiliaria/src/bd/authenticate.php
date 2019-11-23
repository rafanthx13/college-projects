<?php

/* check_login_user()
Verifica a variavel de sessão: se nâo existir retorna falso.
 Se existir então verifica se esses dados são os mesmos que estão no banco
 Verificando se $_SESSION['login_key'], que é o hash da senha com uma constante
 $_SERVER['HTTP_USER_AGENT'] (que é o navegador do user)

*/
function check_login_user($mysqli) {
  // Check if all session variables are set
  if (!isset($_SESSION['user_id'], $_SESSION['login_key'])){
    return false;
  }
  
  $idUsuario = $_SESSION['user_id'];
  $login_key = $_SESSION['login_key'];
    
  $SQL = "
    SELECT senha 
    FROM Funcionario
    WHERE cod_funcionario = ?
    LIMIT 1
  ";
  
  $stmt = $mysqli->prepare($SQL);
  $stmt->bind_param('i', $idUsuario);
  $stmt->execute();
  $stmt->store_result();
  
  if ($stmt->num_rows == 1)  {

    $stmt->bind_result($senhaHash);
    $stmt->fetch();
    
    $login_keyCheck = hash('sha512', $senhaHash . $_SERVER['HTTP_USER_AGENT']);
    if (hash_equals($login_keyCheck, $login_key)){
      return true;
    }
  }
  
  return false;
}

function autentify(){
  try {
    $conection = connectMySQL();
    if (check_login_user($conection))  {
      $conection->close();
    } else {
      exit_session();
    }
  } catch (Exception $e) {
    exit_session();
  }
}

function exit_session() {
	session_destroy();
	header("Location: ./../../../index.php?page=no_session");
}


?>
