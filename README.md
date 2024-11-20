# *projeto-media-alunos* 

## *Passo 1: Criar o repositório no GitHub*
• Foi criado um repositório chamado projeto-media-alunos no site GitHub.
• Ele serve como um lugar para guardar o projeto e registrar todas as mudanças feitas no código.

## *Passo 2: Clonar o repositório*
• O repositório foi “copiado” para o computador com o comando git clone.
• Isso permite trabalhar no projeto localmente, mas ainda manter as mudanças sincronizadas com o GitHub.

## *Passo 3: Criar o programa básico*
• Foi criado um arquivo para o programa. Nele, foi colocado um código simples que:
1. Pede 3 notas para o usuário.
2. Calcula a média dessas notas.
3. Mostra a média final.
• Depois disso, foi feito um commit para registrar essa parte do trabalho, com a mensagem: “Criação do programa básico para calcular a média”.

## *Passo 4: Adicionar a verificação de aprovação/reprovação*
• Foi criada uma nova linha de trabalho chamada branch com o nome feature/verificacao-aprovacao.
• Nessa branch, o programa foi melhorado para dizer se o aluno está aprovado ou reprovado, com base na média:
• Se a média for maior que 6, exibe “Aprovado”.
• Se for menor ou igual a 6, exibe “Reprovado”.
• Depois de fazer isso, foi feito outro commit com a mensagem: “Adiciona verificação de aprovação/reprovação”.

## *Passo 5: Unir a funcionalidade à principal*
• A branch com a funcionalidade de aprovação foi juntada à principal, chamada main.
• Isso significa que o código principal agora também mostra se o aluno foi aprovado ou reprovado.

## *Passo 6: Adicionar a verificação de recuperação*
• Foi criada outra branch chamada feature/verificacao-recuperacao.
• Foi adicionada uma parte no programa que verifica se o aluno está de recuperação:
• Se a média for entre 5 e 6, exibe “Recuperação”.
• Depois, foi feito um commit com a mensagem: “Adiciona verificação de recuperação”.
• Essa branch foi unida à principal, e o programa principal ficou mais completo.

## *Passo 7: Adicionar os pesos*
• Foi criada mais uma branch chamada feature/pesos.
• A forma de calcular a média foi mudada para considerar pesos:
• A primeira e a segunda nota têm peso 1.
• A terceira nota tem peso 2.
• Depois de ajustar isso, foi feito um commit com a mensagem: “Adiciona cálculo com pesos”.
• Essa melhoria também foi unida ao código principal.

## *Passo 8: Atualizar o README*
• O arquivo README.md foi atualizado para incluir:
• Uma explicação do que o projeto faz.
• As funções que ele tem (média, aprovação, recuperação e pesos).
• Como rodar o programa.
• Foi feito mais um commit para registrar essa explicação.