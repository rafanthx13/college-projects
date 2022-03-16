<?php

session_start();

$_SESSION = array(); // unset session

setcookie (session_id(), "", time() - 3600);
session_destroy();
session_write_close();

// header("Location: /alpha/index.php"); // localhost
header("Location: ../../../index.php"); // site

exit();

?>