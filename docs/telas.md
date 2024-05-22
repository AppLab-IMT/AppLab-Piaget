<style>
*{
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}
</style>

# Telas

## 01. TELA INICIAL (t01)
A tela inicial consta de um texto com o a frase "Bem-Vindo a: AppLab" uma imagem com os personagens tema da solucao, e 2 botoes:
- Botao Login: Renderiza uma nova tela com a funcionalidade de login para todos os usuarios.
- Botao Matricula: Renderiza uma nova tela com a funcionalidade de formulario de cadastro (matricula) para estudantes 

<img src="./mockups/t01.png" alt="img tela t01" style="width:auto ; height: 300px">


## 02. TELA LOGIN (t02)
A tela de login apresenta o nome da aplicacao seguida do label email institucional junto a seu input texto e o label senha junto ao seu input tipo texto e abaixo 2 botoes , botao entrar e botao voltar, os componentes funcionais em esta tela sao:
- Input para e-mail institucional: recebe a entrada do usuario que devera ser uma email institucional que siga o padrao nome.ultimosobrenome@jpiaget.g12.br para alunos ou nome.ultimosobrenome@jpiaget.pro.br para professores ou nome.ultimosobrenome@jpiaget.com.br para outros funcionarios que nao sejam professores
- Input para Senha: O usuario devera ingressar sua senha que sera comparada com a senha hasheada guardada em banco de dados
- Botao Entrar : Tera sua funcionalidade ativada sempre quando os campos para email e senha estejam preenchidos com algo, em este caso ao clicar em botao ocorre a verificacao do email e senha com base de dados e se correto redireciona para tela de perfil do contrario mostra um messagebox(alert) de que nao foi possivel ingressar
- Botao Voltar: Ao clicar em botao voltar da tela de login o usuario retorna a pagina inicial da solucao 

<img src="./mockups/t02.png" alt="img tela t01" style="width:auto ; height: 300px">