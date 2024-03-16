# TPC 5 de PL2024
## Visão Global
Esta pasta contém dois ficheiros relevantes:
- `vending.py`: Ficheiro da aplicação.
- `vending_tests.py`: Ficheiro destinado a testes unitários, utilizado somente para a validação de determinadas funções.

A estrutura da aplicação divide-se em duas classes fundamentais:
- `Menu`: Encarregue da interface de interação com o utilizador.
- `Produtos`: Responsável pela gestão dos produtos.

Adicionalmente, há um ficheiro relacionado com a base de dados dos produtos:
- `produtos.json`

Este ficheiro permite a edição das quantidades de produto existentes e a adição de novos produtos. A gestão é realizada manualmente. Quando o programa é iniciado, ele carrega as configurações e procede com a atualização do ficheiro conforme necessário.

Para iniciar a aplicação, execute o seguinte comando:
```bash
python vending.py
```
