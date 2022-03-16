
getcwd() : String :: Retorna caminho completo do diretorio que se esta
/opt/lampp/htdocs/alpha/app/template/public_area

Usar PHP em HTML
````php
<?php
  $param = "test";
?>
<a href="http://www.whatever.com/<?php echo htmlspecialchars($param);?>">Click Here</a>
````

comparar string

strcmp($dir, "alpha") == 0

Projteo
+ Para reajnar os direotiros, colocar require nas páginas com acaminhos diferentes

Jogar execao

throw new Exception("O email do aluno deve ser fornecido");

Cath

catch (Exception $e) {
        // altera o código de retorno de status para '400 Bad Request'.
        // A função http_response_code deve ser chamada antes do script enviar qualquer
        // texto para a saída padrão
        http_response_code(400);

        $msgErro = $e->getMessage();
        echo $msgErro;
    }


    <?php ?>