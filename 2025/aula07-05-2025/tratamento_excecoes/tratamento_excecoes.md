# Tratamento de Exceções

Exceção é a impossibilidade de execução de um código em uma determinada situação (isto é, estado do programa). Embora as
exceções possam ocorrer por erros de sintaxe (incluindo aí, problemas léxicos), problemas problemas na semântica do
código são os principais causadores de exceção.

Há basicamente duas abordagens para se evitar exceções.  A primeira consiste em um detalhado projeto do software para
antever todas os possíveis estados do programa que podem ocorrer e produzir exceções.  O problema com esta abordagem é
que ela tende a tornar a fase de projeto do software muito demorada, tomando um tempo para evitar algo que facilmente
poderia ser evitado com testes.  Ou seja, muitas vezes não é prático investir tanto tempo em detalhar o projeto ao ponto
de evitar a possibilidade de ocorrência de quaisquer exceções. A segunda abordagem propóe uma redução no tempo de projeto com um aumento no uso de testes de software para captar
exceções e, então, protegê-las com cláusulas try/except.

Não existe a forma correta, o que se tem é a mais adequada ao software em questão.  Assim, um software crítico exigirá
maior tempo de análise e projeto para evitar o risco de um exceção que provoque risco de vida como, por exemplo, no 
software que controla um avião.  Já em software onde erros provocam danos potenciais menores, costuma-se usar a aborda-
gem de tratamento de exceções.

Para ver a sintaxe adequada para tratar exceções, veja os seguintes tutoriais:

1. [Programiz](https://www.programiz.com/python-programming/exception-handling)
2. [Real Python](https://realpython.com/python-exceptions/)
3. [W3 Schools](https://www.w3schools.com/python/python_try_except.asp)
4. [GeeksforGeeks](https://www.geeksforgeeks.org/python-exception-handling/)
5. [Documentação Python](https://docs.python.org/3/tutorial/errors.html)
