function send_form_login(user, password) {

  // if(valid_login(user, password)){

  // } else {

  // }

  var win = window.open("./src/bd/login.php?user=" + user + "&" + "password=" + password, '_blank');
  win.focus();

  // $.ajax({

  //     url: './src/bd/login.php',
  //     type: 'POST',
  //     async: false,
  //     dataType: 'json',
  //     data: {'user': user, 'password': password},

  //     success: function (result) {

  //         console.log("JS : Sucess");

  //         // se dataType fosse 'html', então seria necessário
  //         // converter a string JSON recebida em um objeto JavaScript
  //         // manualmente (utilizando a função JavasScript JSON.parse)

  //         // Neste exemplo, como dataType foi definido para o valor 'json', então a conversão
  //         // da string para um objeto JavaScript é realizada automaticamente.

  //         // NOTA IMPORTANTE 1: Entretanto, todo conteúdo gerado
  //         // pelo script PHP precisa ser convertido para JSON (no servidor, em PHP).
  //         // Caso contrário, teremos um erro de conversão para
  //         // JSON no JavaScript/jQuery, o que faz com que esta parte
  //         // do código (success:) não seja executada, mas sim a parte
  //         // definida em 'error:'. Isto pode acontecer mesmo
  //         // quando o script PHP termina sem gerar erros.

  //         // NOTA IMPORTANTE 2: Em algumas situações esta funçao pode ser
  //         // executada mesmo quando o script PHP não termina com sucesso
  //         // (por exemplo, quando ocorrem erros de sintaxe na linguagem PHP). Isto acontece
  //         // porque o PHP (em conjunto com o servidor web) pode retornar
  //         // o código de STATUS '200-OK' mesmo quando há erros/warnings no script.

  //         // if (result != "") {
  //         //     document.forms[0]["rua"].value = result.rua;
  //         //     document.forms[0]["bairro"].value = result.bairro;
  //         //     document.forms[0]["cidade"].value = result.cidade;
  //         // }

  //         console.log("result:", result);

  //         if(result){
  //           window.open("./app/template/private_area/private_index.php", '_blank');
  //         }
  //     },

  //     error: function (xhr, textStatus, error) {
  //         console.log("JS : Failed");
  //         // xhr é o objecto XMLHttpRequest
  //         // No caso de um erro HTTP, o terceiro parametro 'error' contem a string 
  //         // correspondente ao código do erro, como "Not found" ou "Internal Server Error"
  //         alert(textStatus + error + xhr.responseText);
  //     }

  // });

}

function valid_login(user, password){

  $.ajax({

    url: './src/bd/login.php',
    type: 'GET',
    async: false,
    dataType: 'json',
    data: {'user': user, 'password': password},

    success: function (result) {
        return result;
    },

    error: function (xhr, textStatus, error) {
        return false;
    }

  });

}

function enter_login(user, password){

  $.ajax({

    url: './src/bd/login.php',
    type: 'POST',
    async: false,
    dataType: 'json',
    data: {'user': user, 'password': password},

    success: function (result) {

        console.log("JS : Sucess");

        // se dataType fosse 'html', então seria necessário
        // converter a string JSON recebida em um objeto JavaScript
        // manualmente (utilizando a função JavasScript JSON.parse)

        // Neste exemplo, como dataType foi definido para o valor 'json', então a conversão
        // da string para um objeto JavaScript é realizada automaticamente.

        // NOTA IMPORTANTE 1: Entretanto, todo conteúdo gerado
        // pelo script PHP precisa ser convertido para JSON (no servidor, em PHP).
        // Caso contrário, teremos um erro de conversão para
        // JSON no JavaScript/jQuery, o que faz com que esta parte
        // do código (success:) não seja executada, mas sim a parte
        // definida em 'error:'. Isto pode acontecer mesmo
        // quando o script PHP termina sem gerar erros.

        // NOTA IMPORTANTE 2: Em algumas situações esta funçao pode ser
        // executada mesmo quando o script PHP não termina com sucesso
        // (por exemplo, quando ocorrem erros de sintaxe na linguagem PHP). Isto acontece
        // porque o PHP (em conjunto com o servidor web) pode retornar
        // o código de STATUS '200-OK' mesmo quando há erros/warnings no script.

        // if (result != "") {
        //     document.forms[0]["rua"].value = result.rua;
        //     document.forms[0]["bairro"].value = result.bairro;
        //     document.forms[0]["cidade"].value = result.cidade;
        // }

        console.log("result:", result);

        if(result){
          window.open("./app/template/private_area/private_index.php", '_blank');
        }
    },

    error: function (xhr, textStatus, error) {
        console.log("JS : Failed");
        // xhr é o objecto XMLHttpRequest
        // No caso de um erro HTTP, o terceiro parametro 'error' contem a string 
        // correspondente ao código do erro, como "Not found" ou "Internal Server Error"
        alert(textStatus + error + xhr.responseText);
    }

});

}

