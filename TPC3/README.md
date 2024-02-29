# Somador ON/OFF

## Descrição

Este script Python lê um ficheiro de texto e soma as sequencias de digitos encontrados.
A soma é condicional, ou seja é ativada e desativada consoante encontre a sequencia "On" ou "Off", em qualquel combinação de maiusculas e minusculas.
Quando é encontrado o caracter "=", ele imprime a soma acumulada até aquele ponto.

## Funcionalidades

- **Ativar/Desativar da Soma:** O script começa com o somador ligado. Ao encontrar a palavra "On" no texto, o script ativa a funcionalidade de soma. Quando encontra a palavra "Off", a funcionalidade de soma é desativada.

- **Soma de Números:** Enquanto a soma está ativada, o script soma todas as sequências de dígitos (tratadas como números inteiros) encontradas no texto.

- **Exibição da Soma:** Ao encontrar o caractere "=", o script imprime a soma acumulada até aquele momento.
