<?php

// Cria e conecta ao banco de dados
$dbPath = '../src/data/pcBolado.sqlite';
$pdo = new PDO("sqlite:$dbPath");
echo "Banco de dados criado e conectado com sucesso! \n";



// Cria a tabela
$pdo->exec('CREATE TABLE computador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    situacao TEXT NOT NULL,
    marca TEXT NOT NULL,
    descricao TEXT NOT NULL,
    imagem TEXT NOT NULL,
);');
echo "Tabela 'computador' criada com sucesso! \n";


// Executa os INSERTs
$sql = "
INSERT INTO computador (situacao, marca, descricao, imagem) VALUES 
('FUNCIONANDO','DATEN','Computador Daten funcionando.','/assets/img/daten/funcionando/daten01-func.jpeg'),
('FUNCIONANDO','DATEN','Computador Daten funcionando.','/assets/img/daten/funcionando/daten02-func.jpeg'),
('FUNCIONANDO','DATEN','Computador Daten funcionando.','/assets/img/daten/funcionando/daten03-func.jpeg'),
('FUNCIONANDO','DATEN','Computador Daten funcionando.','/assets/img/daten/funcionando/daten01-func.jpeg'),
('FUNCIONANDO','POSITIVO','Computador Positvo funcionando.','/assets/img/positivo/funcionando/posi01-func.jpeg'),
('NAO-FUNCIONANDO','DATEN','Computador Daten não está funcionando.','/assets/img/daten/nao-funcionando/daten01-nfunc.jpeg'),
('NAO-FUNCIONANDO','DATEN','Computador Daten não está funcionando.','/assets/img/daten/nao-funcionando/daten02-nfunc.jpeg'),
('NAO-FUNCIONANDO','DATEN','Computador Daten não está funcionando.','/assets/img/daten/nao-funcionando/daten03-nfunc.jpeg'),
('NAO-FUNCIONANDO','DATEN','Computador Daten não está funcionando.','/assets/img/daten/nao-funcionando/daten04-nfunc.jpeg'),
('NAO-FUNCIONANDO','POSITIVO','Computador Positvo não está funcionando.','/assets/img/positivo/nao-funcionando/posi01-nfunc.jpeg'),
('NAO-FUNCIONANDO','POSITIVO','Computador Positvo não está funcionando.','/assets/img/positivo/nao-funcionando/posi02-nfunc.jpeg'),
('NAO-FUNCIONANDO','POSITIVO','Computador Positvo não está funcionando.','/assets/img/positivo/nao-funcionando/posi03-nfunc.jpeg'),
('NAO-FUNCIONANDO','POSITIVO','Computador Positvo não está funcionando.','/assets/img/positivo/nao-funcionando/posi04-nfunc.jpeg'),
('NAO-FUNCIONANDO','POSITIVO','Computador Positvo não está funcionando.','/assets/img/positivo/nao-funcionando/posi05-nfunc.jpeg');
";

$pdo->exec($sql);
echo "Produtos inseridos com sucesso!";