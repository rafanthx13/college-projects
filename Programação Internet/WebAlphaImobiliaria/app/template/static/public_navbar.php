<?php

// require "dir_functions.php"
$prefix_dir = choose_prefix_navbar();

?>

<nav class="navbar navbar-expand-sm py-0 my-nav navbar-inverse bg-inverse">
  <div class="container navbar-collapse">

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
      aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon svg-hamburguer"><img src="app/img/bars-solid.svg" alt="." style="fill:#7E7E7E;"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarCollapse">
      <!-- NavBar - Parte da Esquerda -->
      <ul class="navbar-nav mr-auto">
        <li class="nav-li nav-item">
          <a class="py-2 nav-link" href="<?php echo $prefix_dir . "who_we_are.php";?>" >Quem Somos</a>
        </li>
        <li class="nav-li nav-item">
          <a class="py-2 nav-link" href="<?php echo $prefix_dir . "imovel_search.php" ;?>" >Buscar Imóvel</a>
        </li>
      </ul>
      <!-- NavBar - Parte da Direita -->
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <button type="button" class="btn btn-outline-primary login-button" data-toggle="modal"
            data-target="#loginModal">
            Login
          </button>
        </li>
      </ul>

    </div>

  </div>
</nav>