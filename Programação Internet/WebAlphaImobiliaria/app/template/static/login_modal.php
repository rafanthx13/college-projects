<?php

$prefix_dir_private = choose_prefix_private() . "private_index.php";

$prefix_login = choose_prefix_login() . "login.php";

// echo $prefix_login . "\n";

?>


<div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">

      <div class="modal-header">
        <h6 class="modal-title" id="exampleModalLabel">Tela de Login</h6>
          <img style="width: 20%;" src="./app/img/logo-form.png" alt="">
      </div>

      <!-- <form class="modal-content animate" action=" <?php echo ($prefix_login) ;?> " method="POST"> -->
      <form class="modal-content animate" action="" method="POST">
        <div class="modal-body">
          <div class="container">
            
              <div class="form-group row">
                <label for="user">Usuário</label>
                <input type="text" name="user" id="user" class="form-control" placeholder="Digite o usuário">
              </div>
              <div class="form-group row">
                <label for="password">Senha</label>
                <input type="password" name="password" id="password" class="form-control" placeholder="Digite a Senha">
              </div>
            

          </div>
        </div>

        <div class="modal-footer">
          <button class="btn btn-danger btn-sm" data-dismiss="modal">Fechar</button>
          <!-- <button onclick="document.location.href=' <?php echo ($prefix_dir_private) ;?>' ">Entrar</button> -->

          <!-- <button class="btn btn-success btn-sm" type="submit">Login</button>  -->

          <!-- sendForm esta separada em login.php -->
          <button class="btn btn-success btn-sm" onclick="send_form_login(document.forms[0]['user'].value, document.forms[0]['password'].value)">Entrar</button>
          
          
        </div>

      </form>

    </div>
  </div>
</div>