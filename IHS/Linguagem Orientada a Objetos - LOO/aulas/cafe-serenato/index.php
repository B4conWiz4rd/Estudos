<?php
echo "Olá Mundo!";
$produtoCafe = [
    [
        'nome' => "Café Cremoso",
        'descricao' => "Café cremosos irresitivel sauve e que envolve o paladar",
        'preco' => "5,00",
        'imagem' => "assets/img/cafe-cremoso.jpg",
    ],
    [
        'nome' => "Café com Leite",
        'descricao' => "A harmonia perfeita do café do leite, uma experiência reconfortante",
        'preco' => "2,00",
        'imagem' => "assets/img/cafe-com-leite.jpg",
    ],
    [
        'nome' => "Cappunccino",
        'descricao' => "Café suave, leite cremoso e uma pitada de sabor adocicado",
        'preco' => "7,00",
        'imagem' => "assets/img/cappuccino.jpg",
    ],
    [
        'nome' => "Café Gelado",
        'descricao' => "Café gekadi refrescante, adoçado e com notas sutis de baunilha e com notas sutis de baunilha ou caramelo",
        'preco' => "3,00",
        'imagem' => "assets/img/cafe-gelado.jpg",
    ]
];

$produtoAlmoco = [
    [
        'nome' => "Bifão",
        'descricao' => "Bife, arroz com feijão e uma deliciosa batata frita",
        'preco' => "27,90",
        'imagem' => "assets/img/bife.jpg"
    ],
    [
        'nome' => "Filé de peixe",
        'descricao' => "Filé de peixe salmão assado, arros, feijão verde e tomate.",
        'preco' => "24,99",
        'imagem' => "assets/img/prato-peixe.jpg"
    ],
    [
        'nome' => "Frangão",
        'descricao' => "Saboroso frango à milanesa com batatas fritas, salada de repolho e molho picante",
        'preco' => "23,00",
        'imagem' => "assets/img/prato-frango.jpg"
    ],
    [
        'nome' => "Fettuccinezudo",
        'descricao' => "Prato italiano autêntico da massa do fettuccine com peito de frango grelhado",
        'preco' => "22,50",
        'imagem' => "assets/img/fettuccine.jpg"
    ],
];
?>

<!doctype html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="assets/css/reset.css">
    <link rel="stylesheet" href="assets/css/index.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="icon" href="assets/img/icone-serenatto.png" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;900&display=swap"
        rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
    <title>Serenatto - Cardápio</title>
</head>

<body>
    <main>
        <section class="container-banner">
            <div class="container-texto-banner">
                <img src="assets/img/logo-serenatto.png" class="logo" alt="logo-serenatto">
            </div>
        </section>
        <h2>Cardápio Digital</h2>
        <section class="container-cafe-manha">
            <div class="container-cafe-manha-titulo">
                <h3>Opções para o Café</h3>
                <img class="ornaments" src="assets/img/ornaments-coffee.png" alt="ornaments">
            </div>
            <div class="container-cafe-manha-produtos">
                <?php foreach ($produtoCafe as $cafe): ?>
                    <div class="container-produto">
                        <div class="container-foto">
                            <img src="<?php echo $cafe['imagem'] ?>">
                        </div>
                        <p><?php echo $cafe['nome'] ?></p>
                        <p><?php echo $cafe['descricao'] ?></p>
                        <p><?php echo $cafe['preco'] ?> </p>
                    </div>
                <?php endforeach; ?>
            </div>
        </section>
        <section class="container-almoco">
            <div class="container-almoco-titulo">
                <h3>Opções para o Almoço</h3>
                <img class="ornaments" src="assets/img/ornaments-coffee.png" alt="ornaments">
            </div>
            <div class="container-almoco-produtos">
                <?php foreach ($produtoAlmoco as $almoco): ?>
                    <div class="container-produto">
                        <div class="container-foto">
                            <img src="<?php echo $almoco['imagem'] ?>">
                        </div>
                        <p><?php echo $almoco['nome'] ?></p>
                        <p><?php echo $almoco['descricao'] ?></p>
                        <p><?php echo $almoco['preco'] ?> </p>
                    </div>
                <?php endforeach; ?>
        </section>
    </main>
</body>

</html>