-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 11-Nov-2019 às 15:11
-- Versão do servidor: 10.4.8-MariaDB
-- versão do PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `3198912_trabalho`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `Cliente_proprietario`
--

CREATE TABLE `Cliente_proprietario` (
  `cod_cliente` int(8) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `email` varchar(30) NOT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `profissao` varchar(30) DEFAULT NULL,
  `estado_civil` varchar(20) DEFAULT NULL,
  `cep` varchar(9) NOT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  `logradouro` varchar(50) DEFAULT NULL,
  `numero` int(5) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Cliente_proprietario`
--

INSERT INTO `Cliente_proprietario` (`cod_cliente`, `nome`, `cpf`, `email`, `telefone`, `sexo`, `profissao`, `estado_civil`, `cep`, `bairro`, `logradouro`, `numero`) VALUES
(1, 'Jose Eustaquio Silva', '117.197.255-23', 'joseeustaqui@gmail.com', '992579919', 'masculino', 'professor', 'casado', '38474-000', 'Morada Nova', 'Alameda das Seringueiras ', 1002),
(2, 'Nathan Augusto Coelho dos Santos', '196.802.736-09', 'nathanaugusto@gmail.com', '992673782', 'masculino', 'programador', 'solteiro', '38405-325', 'Brasil', 'Afonso Pena', 4282),
(3, 'nome1', '25352', 'rafa@gmail.com', '53252', 'male', 't5', 'Solteiro', '38659-394', '24355', '64564', 534353),
(4, 'nome2', '64574574', 'gsdgdsg@gmail.com', '53252523', 'female', '52532', 'Divorciado', '23495-123', '2524', '23424', 234242),
(5, 'Rafael Morais de23', '52523', '5235235@gmail.com', '53464363', 'female', '643643', 'Solteiro', '43534-999', '45345', '435435', 43534),
(6, 'afsfa', 'fsafa', 'farrewrew@gmail.com', 'y538453453', 'female', '4fegdt34', 'Divorciado', '38408-194', '34', '52352352', 4454);

-- --------------------------------------------------------

--
-- Estrutura da tabela `Funcionario`
--

CREATE TABLE `Funcionario` (
  `cod_funcionario` int(8) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `telefone_celular` varchar(12) DEFAULT NULL,
  `telefone_contato` varchar(12) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `cep` varchar(9) NOT NULL,
  `cidade` varchar(30) DEFAULT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  `numero` int(5) DEFAULT NULL,
  `ingresso` date NOT NULL,
  `cargo` varchar(30) NOT NULL,
  `salario` float NOT NULL,
  `login` varchar(20) NOT NULL,
  `senha` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Funcionario`
--

INSERT INTO `Funcionario` (`cod_funcionario`, `nome`, `cpf`, `email`, `telefone`, `telefone_celular`, `telefone_contato`, `endereco`, `cep`, `cidade`, `bairro`, `numero`, `ingresso`, `cargo`, `salario`, `login`, `senha`) VALUES
(1, 'Miguel Henrique de Brito Pereira', '118.156.786-23', 'miguelhbrito@gmail.com', '997268236', '997268236', NULL, 'Alameda das Seringueiras 6003', '38400-012', 'Uberlandia', 'Cazeca', 1352, '2019-03-13', 'Vendedor', 1200, 'miguelbrito', '123456'),
(2, 'Rafael Morais de Assis', '34.156.786-23', 'rafaassis15@gmail.com', '997268236', '997268236', NULL, 'Rua Boulevard 452', '38400-012', 'Uberlandia', 'Gnaja Marileusa', 1352, '2019-03-13', 'Gerente', 1200, 'admin', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec'),
(3, 'Rafael Morais de Assi', '04638784500', 'rafaassis15@gmail.com', '525252', '43', '4345435', '52352352', '38408-194', '5252352', '34', 2, '2019-11-04', '53252', 3, 'rafael', 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'),
(4, 'Rafael Morais de2', '235235', 'taasga@gmail.com', '25234', '24234', '24234', '5235', '38408-192', '3252', '52352', 2, '2019-11-12', '5235', 2535, 'ary', '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2'),
(5, '42432', '42342', 'rafa@gmail.com', '324324', '23', '42342', '242', '4234', '23423', '4234', 423, '2019-11-15', '4234', 2423, '4234', 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'),
(6, '4234', '23425', '235252@gmail.com', '3525', '23252', '5323523', '678678', '56575722', '574', '745', -186, '2019-11-05', '679', 96, '54373', '352905f30b6bd8405ed983cf0eab7d90b2fe7f2a2d0298dc05fd5c6e9dac260d81fe115048f79d847d9a9abe80a3fe3780f9d0d870fa4871f8606e79a95f5327'),
(7, '3333', '33333', '333@gags.com', '333', '3333', '3333', '3333', '33333', '3333', '333', 33, '2019-11-23', '333', 333, 'rafael123', 'a4f2f198bd93e532d294e53faee9a5edc261a00c0779836e270a1c27b26cd15283b2dc7370aeda9893db3660c8b92a8e9fac68f6c35c91842f8a839e43fbc649');

-- --------------------------------------------------------

--
-- Estrutura da tabela `Imgs_imovel`
--

CREATE TABLE `Imgs_imovel` (
  `cod_imovel` int(11) NOT NULL,
  `path` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `Imovel`
--

CREATE TABLE `Imovel` (
  `objetivo` varchar(128) NOT NULL,
  `tipo` varchar(30) DEFAULT NULL,
  `cod_imovel` int(11) NOT NULL,
  `nro_quartos` int(11) DEFAULT NULL,
  `nro_banheiros` int(11) DEFAULT NULL,
  `nro_suites` int(11) DEFAULT NULL,
  `nro_garagem` int(11) DEFAULT NULL,
  `area` float DEFAULT NULL,
  `descricao` varchar(200) DEFAULT NULL,
  `portaria` tinyint(1) NOT NULL,
  `bairro` varchar(20) NOT NULL,
  `cod_cliente` int(11) NOT NULL,
  `andar` int(8) DEFAULT NULL,
  `valor_cond` float DEFAULT NULL,
  `valor_aluguel` float DEFAULT NULL,
  `disponivel` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Imovel`
--

INSERT INTO `Imovel` (`objetivo`, `tipo`, `cod_imovel`, `nro_quartos`, `nro_banheiros`, `nro_suites`, `nro_garagem`, `area`, `descricao`, `portaria`, `bairro`, `cod_cliente`, `andar`, `valor_cond`, `valor_aluguel`, `disponivel`) VALUES
('Vender', NULL, 1, 2, 2, 1, 1, 44, 'Piso de ceramica e janelas em blindex.', 1, 'Santa Monica', 1, NULL, NULL, NULL, NULL),
('Vender', NULL, 2, 3, 2, 1, 2, 55, '3 quartos, 2 banheiros, 1 suite, garagem pra 2 carros e pintura recem feita.', 1, 'Finotti', 2, NULL, NULL, NULL, NULL),
('comprar', 'apto', 3, 1, 1, 1, 1, 42342, '432423', 1, 'Santa Monica', 5, 1, 23424, 3424, NULL),
('alugar', 'casa', 4, 3, 3, 3, 4, 153252, 'deve ir a imagem', 1, 'Santa Monica', 5, 3, 43, 43242, NULL),
('alugar', 'casa', 5, 3, 3, 3, 4, 153252, 'deve ir a imagem', 1, 'Santa Monica', 5, 3, 43, 43242, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `Interesse`
--

CREATE TABLE `Interesse` (
  `cod_imovel` int(11) NOT NULL,
  `cod_cliente` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  `telefone` varchar(14) NOT NULL,
  `comentario` varchar(200) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `Interesse`
--

INSERT INTO `Interesse` (`cod_imovel`, `cod_cliente`, `nome`, `email`, `telefone`, `comentario`) VALUES
(1, 1, 'David Eduardo Costa e Silva', 'davidcosta@gmail.com', '998657871', 'Tenho interesse no seu imovel, estou de acordo com o preço e caso queira esclarecer alguma coisa entre em contato. ');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `Cliente_proprietario`
--
ALTER TABLE `Cliente_proprietario`
  ADD PRIMARY KEY (`cod_cliente`),
  ADD UNIQUE KEY `cpf` (`cpf`);

--
-- Índices para tabela `Funcionario`
--
ALTER TABLE `Funcionario`
  ADD PRIMARY KEY (`cod_funcionario`),
  ADD UNIQUE KEY `cpf` (`cpf`),
  ADD UNIQUE KEY `login` (`login`);

--
-- Índices para tabela `Imgs_imovel`
--
ALTER TABLE `Imgs_imovel`
  ADD PRIMARY KEY (`cod_imovel`),
  ADD UNIQUE KEY `path` (`path`);

--
-- Índices para tabela `Imovel`
--
ALTER TABLE `Imovel`
  ADD PRIMARY KEY (`cod_imovel`),
  ADD KEY `fk_cod_cliente` (`cod_cliente`);

--
-- Índices para tabela `Interesse`
--
ALTER TABLE `Interesse`
  ADD PRIMARY KEY (`cod_imovel`,`cod_cliente`),
  ADD KEY `fk_cod_cliente` (`cod_cliente`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Cliente_proprietario`
--
ALTER TABLE `Cliente_proprietario`
  MODIFY `cod_cliente` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `Funcionario`
--
ALTER TABLE `Funcionario`
  MODIFY `cod_funcionario` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `Imovel`
--
ALTER TABLE `Imovel`
  MODIFY `cod_imovel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
