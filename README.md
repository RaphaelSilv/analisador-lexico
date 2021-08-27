# Analisador Léxico

```python
import introducao from compiladores

grupo = 3

alunos = {

    'Luiz Felipe Ribeiro Baroncello': '18250266',
    'Luiz Fernando de Souza': '16204445',
    'Raphael Ramos da Silva': '18102523',
    'Vinicius Maximiano Alves': '15205399'
}

```

## Executando com o make

```sh
make run FILE="path/<file>.lcc"
make run RAW="int foo = 7;"
```

Exemplo de output esperado:

```sh
$ make run FILE="path/<filename>.lcc"

```
```sh
python3 main.py --file "path/<filename>.lcc"

['{', '{', 'FLOAT', 'IDENT', ';', 'FLOAT', 'IDENT', ';', 'INT', 'IDENT', ';', 'INT', 'IDENT', ';', 'IDENT', '=', 'INT_CONSTANT', ';', 'IDENT', '=', 'INT_CONSTANT', ';', 'FOR', '(', 'IDENT', '=', 'INT_CONSTANT', ';', 'IDENT', 'RELOP', 'IDENT', ';', 'IDENT', '=', 'IDENT', '+', 'INT_CONSTANT', ')', '{', 'PRINT', 'IDENT', ';', 'IDENT', '=', 'IDENT', '+', 'FLOAT_CONSTANT', ';', 'IDENT', '=', 'IDENT', ';', 'IF', '(', 'IDENT', 'RELOP', 'IDENT', ')', '{', 'PRINT', 'STRING_CONSTANT', ';', 'BREAK', ';', '}', '}', '}']

Tabela de Simbolos
Ident: x linhas:  [4, 8, 11, 12, 13, 14]
Ident: z linhas:  [5, 13, 14]
Ident: i linhas:  [6, 10]
Ident: max linhas:  [7, 9, 10]

```
## Executando com o python3

```sh
python3 main.py --file path/<filename>.lcc
python3 main.py --raw "int foo = 5;"
```

Exemplo de output esperado:

```python
$ python3 main.py --raw "float x = 5;"
```
```sh
['FLOAT', 'IDENT', '=', 'INT_CONSTANT', ';']
Tabela de Simbolos
Ident: x linhas:  [1]
```
