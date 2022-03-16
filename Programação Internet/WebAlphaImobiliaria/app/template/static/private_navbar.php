<div class="gray-line"></div>
<nav class="py-0 navbar navbar-expand-sm my-nav">
  <div class="container">
    <ul class="nav-ul">
      <li class="nav-li">
        <div class="dropdown">

          <a class="btn btn-secondary dropdown-toggle private-nav-btn" href="#" role="button" id="dropdownMenuLink"
            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Cadastrar
          </a>

          <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <a class="dropdown-item" href="./register_imovel.php">Cadastrar Imóveis</a>
            <a class="dropdown-item" href="./register_clients.php">Cadastrar Cliente</a>
            <a class="dropdown-item" href="./register_employes.php">Cadastrar Funcionários</a>
          </div>
          
        </div>
      </li>
      <li class="nav-li">
        <div class="dropdown">

          <a class="btn btn-secondary dropdown-toggle private-nav-btn" href="#" role="button" id="dropdownMenuLink"
            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Listar
          </a>

          <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <a class="dropdown-item" href="./list_employes.php">Listar Funcionários</a>
            <a class="dropdown-item" href="./list_imovel.php">Listar Imóveis</a>
            <a class="dropdown-item" href="./list_clients.php">Listar Clientes Proprietários</a>
            <a class="dropdown-item" href="./list_interest.php">Listar Interresses em Imóveis</a>
          </div>

        </div>
      </li>
    </ul>
    <span style="float: right; ">
      <button type="button" class="btn btn-outline-primary login-button"
        onclick="document.location.href='./../static/logout.php'">
        Sair
      </button>
    </span>
  </div>
</nav>
<div class="gray-line"></div>