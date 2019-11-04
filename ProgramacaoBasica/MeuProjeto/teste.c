#include <stdio.h>
// std = standard (padr�o)
// io = input/ouput

int main (){
     //Declaracao de variaveis
     int num1, num2, soma, multiplicacao;

     //Entradas
     printf("Informe o primeiro numero: ");
     scanf("%d", &num1);

     printf("Informe o segundo numero: ");
     scanf("%d", &num2);

     //Processamentos
     soma = num1 + num2;
     multiplicacao = soma * num1;

     //Saida
     printf("O resultado da multiplicacao é %d", multiplicacao);

}
