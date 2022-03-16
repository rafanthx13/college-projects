<!-- Definir antes: $modalTitle , $modalContent -->
<div class="modal fade" id="meuModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="false" data-target="#meuModal">
<div class="modal-dialog" role="document">
  <div class="modal-content text-center"">

    <div class="modal-header" style="display: inline;">
      <div style="align-self: center;">
        <h6 class="modal-title" id="exampleModalLabel" style="margin-left: 0%;"><?php echo $modalTitle; ?></h6>
      </div>
    </div>

      <div class="modal-body">
        <div class="container">
          <?php echo $modalContent; ?>
        </div>
      </div>

  </div>
</div>
</div>

<?php 
  echo '<script language="javascript">';
  echo "  $('#meuModal').modal('show')";
  echo '</script>';
?>
