# Atividade - Análise de complexidade

## 1-) Push e enfileirar
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;Ambos têm **complexidade** O(1), pois, para inserir um elemento na pilha, basta alterar a cabeça da lista encadeada e endereçar a antiga cabeça como elemento posterior à nova, requerindo, portanto, um número
constante de passos. Para a fila, basta aplicar a mesma ideia na pilha de adição contida na construção da fila.
</div>

## 2-) Pop e desenfileirar
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;Pop tem **complexidade** O(1), pois basta retirar a atual cabeça e atualizar a cabeça da pilha encadeada como sendo o elemento posterior da antiga cabeça, sendo, então, um número constante de passos.

&nbsp;&nbsp;&nbsp;&nbsp;Já o desenfileirar tem um problema: o elemento cujo endereço guardamos é, na verdade, o último a sair. Assim, há  duas situações possíveis: o caso médio, em que a pilha de retirada (que é construída na ordem inversa à pilha de adição e,portanto, sua cabeça é o elemento mais antigo, seguindo a lógica da fila) não está vazia e, assim, basta retirar o elemento do seu topo, requerindo uma quantidade constante de passos e senod O(1); e o caso péssimo, em que a pilha de retirada está vazia e, assim, você tem de transferir os N elementos da pilha de adição para a pilha de retirada para poder, então, retirar o topo desta, precisando, por isso, de um algoritmo de **complexidade** O(N). Como sua **complexidade** na maior parte dos processos será O(1) e não O(N), dizemos que sua **complexidade** é O(1) amortizada.
</div>

## 3-) Topo e frente
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;Ambos têm a mesma complexidade de sua respectiva função de retirada em sua estrutura de dados, pois seguem a mesma lógica, com o diferencial de não retirar o elemento, apenas retornar seu valor. Assim, suas **complexidades** valem, respectivamente, O(1) e O(1) amortizada.
</div>

## 4-) esta_vazia
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;Ambos têm **complexidade** O(1),pois apenas analisam o próprio tamanho (função cuja **complexidade**, conforme veremos, também é O(1)).
</div>

## 5-) __len__
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;A **complexidade** de ambos é O(1), pois monitoram o próprio tamanho a cada inserção e remorção, de modo que basta retornar uma variável interna constantemente atualizada.
</div>

## 6-) __repr__
<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;A **complexidade** de ambos é O(N).

&nbsp;&nbsp;&nbsp;&nbsp;Na pilha, basta passar a representação textual de cada elemento da pilha com '-->' entre elementos consecutivos para indicar a ordem da pilha.

&nbsp;&nbsp;&nbsp;&nbsp;Na fila, por outro lado, temos de ser mais cuidadosos. Se apenas a pilha de retirada tem elementos, então basta retornar como faríamos com a representação textual de uma pilha qualquer. Se somente a pilha de adição tem elementos, passamos eles para a de retirada, salvamos a representação textual dela, voltamos eles para a original e retornamos o texto salvo. Por fim, se ambos têm elementos, salvamos, em uma variável, a representação textual da pilha de retirada, depois, salvamos em uma pilha reserva a representação textual dos elementos da pilha de adição devidamente ordenados, então os devolvemos e retornarmos texto1 + ' --> ' + texto2. De todo modo, a **complexidade** será O(N).

</div>






