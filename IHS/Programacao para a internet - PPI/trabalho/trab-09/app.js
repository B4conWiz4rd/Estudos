let pts = prompt('Pontuação alcançada (1 a 150):')
if (pts >= 100) {
    alert(`
        Parabêns você venceu!
        `)
} else if (pts == 150) {
    alert(`
        Um high score! Parabéns
        `)
} else {
    alert (`
        Game Over, você perdeu!
        `)
}