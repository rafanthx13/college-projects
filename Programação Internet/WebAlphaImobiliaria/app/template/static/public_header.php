<?php

// require "dir_functions.php"
$prefix_dir_img = (choose_prefix_header());
$prefix_dir_login = choose_prefix_home();

?>

<header class="pb-0 header">
  <div class="red-line"></div>
  <a href="<?php echo $prefix_dir_login;?>">
    <div style="text-align: center;">
      <img class="logoHeader" src="<?php echo $prefix_dir_img . "logo3.png" ;?>" alt="">
    </div>
  </a>
  
</header>  