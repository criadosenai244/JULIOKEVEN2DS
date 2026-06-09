// 1. Criando as variáveis
const nomeJogador = "Julio"; 
let idade = 25;              
let isOnline = true;         

let jogoFavorito = {
    nome: "The Witcher 3",
    anoLancamento: 2015
};

let pontuacoes = [1500, 2100, 1800]; 

// Desafio: Calcular a média das 3 pontuações
let media = (pontuacoes[0] + pontuacoes[1] + pontuacoes[2]) / 3;

// 2. Pegando a área que criamos no HTML
let telaHTML = document.getElementById("resultado");

// 3. Escrevendo os resultados na tela
// Usamos a crase (`) para poder misturar texto normal com variáveis e códigos HTML
telaHTML.innerHTML = `
    <h3>=== Dados do Jogador ===</h3>
    <p><strong>Nome:</strong> ${nomeJogador} | <em>Tipo: ${typeof nomeJogador}</em></p>
    <p><strong>Idade:</strong> ${idade} | <em>Tipo: ${typeof idade}</em></p>
    <p><strong>Online:</strong> ${isOnline} | <em>Tipo: ${typeof isOnline}</em></p>
    <p><strong>Jogo Favorito:</strong> ${jogoFavorito.nome} (${jogoFavorito.anoLancamento}) | <em>Tipo: ${typeof jogoFavorito}</em></p>
    <p><strong>Pontuações:</strong> ${pontuacoes[0]}, ${pontuacoes[1]}, ${pontuacoes[2]} | <em>Tipo: ${typeof pontuacoes}</em></p>
    
    <br>
    
    <h3>=== Desafio Extra ===</h3>
    <p style="color: blue;"><strong>A média de pontos do jogador ${nomeJogador} foi: ${media.toFixed(2)}</strong></p>
`;