import es
import aritmetico



def main():
    # Atribuição de variáveis
    numeros = []
    soma = 0
    op = ""
    # Entrada de dados
    numeros = es.leitora_numeros()
    
    # Processamento de dados
    soma = aritmetico.adicao(numeros[0], numeros[1])
    multiplica = aritmetico.mult(numeros[0], numeros[1])
    divide = aritmetico.div(numeros[0], numeros[1])
    subtrai = aritmetico.sub(numeros[0], numeros[1])
  
    
    # Saída de dados
    es.escritora_numeros(numeros[0], numeros[1], op)
    
    
    
# Invocando a função principal

if __name__ == "__main__":
    main()

