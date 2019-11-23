function buscaEndereco(cep, option) {
      
  if (cep.length != 9){
    if(cep[4] != '-')
      return;
  }

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onload = function (e) {
    if (xmlhttp.status == 200) {
      if (xmlhttp.responseText != "") {
        try {
          endereco = JSON.parse(xmlhttp.responseText);
          if(option == "cliente"){
            document.forms[0]["logradouro"].value = endereco.rua;
            document.forms[0]["bairro"].value = endereco.bairro;
          } else {
            document.forms[0]["address"].value = endereco.rua;
            document.forms[0]["bairro"].value = endereco.bairro;
            document.forms[0]["city"].value = endereco.cidade;
          }
          
        } catch (e) {
          alert("A string retornada pelo servidor não é um JSON válido: " + xmlhttp.responseText);
        }
      }
    }
  }

  xmlhttp.open("GET", "./../../../src/bd/search_address.php?cep=" + cep, true);
  xmlhttp.send();
}