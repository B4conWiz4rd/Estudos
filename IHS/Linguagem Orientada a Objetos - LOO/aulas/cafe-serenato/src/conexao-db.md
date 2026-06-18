<?php

// Cria e conecta ao banco de dados
$dbPath = '../serenatto.sqlite';
$pdo = new PDO("sqlite:$dbPath");
echo "Banco de dados criado e conectado com sucesso! \n";



// Cria a tabela 'produtos'
$pdo->exec('CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    imagem TEXT NOT NULL,
    preco DECIMAL(5,2) NOT NULL
);');
echo "Tabela 'produtos' criada com sucesso! \n";


// Executa os INSERTs
$sql = "
INSERT INTO produtos (tipo, nome, descricao, imagem, preco) VALUES 
('Café', 'Café Cremoso', 'Café cremoso irresistivelmente suave e que envolve seu paladar', 'assets/img/cafe-cremoso.jpg', 5.00),
('Café', 'Café com Leite', 'A harmonia perfeita do café e do leite, uma experiência reconfortante', 'assets/img/cafe-com-leite.jpg', 2.00),
('Café', 'Cappuccino', 'Café suave, leite cremoso e uma pitada de sabor adocicado', 'assets/img/cappuccino.jpg', 7.00),
('Café', 'Café Gelado', 'Café gelado refrescante, adoçado e com notas sutis de baunilha ou caramelo.', 'assets/img/cafe-gelado.jpg', 3.00),
('Almoço', 'Bife', 'Bife, arroz com feijão e uma deliciosa batata frita', 'assets/img/bife.jpg', 27.90),
('Almoço', 'Filé de peixe', 'Filé de peixe salmão assado, arroz, feijão verde e tomate.', 'assets/img/prato-peixe.jpg', 24.99),
('Almoço', 'Frango', 'Saboroso frango à milanesa com batatas fritas, salada de repolho e molho picante', 'assets/img/prato-frango.jpg', 23.00),
('Almoço', 'Fettuccine', 'Prato italiano autêntico da massa do fettuccine com peito de frango grelhado', 'assets/img/fettuccine.jpg', 22.50);
";

$pdo->exec($sql);
echo "Produtos inseridos com sucesso!";