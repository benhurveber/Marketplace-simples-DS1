# Marketplace Simples

Projeto desenvolvido em Django, utilizando de ferramentas próprias do framework, como é o caso do Django REST Framework e a utilização de autenticação por meio de JWT. Trabalho foi desenvolvido para fins de estudo da disciplina e exercício prático dos conteúdos trabalhados no decorrer das aulas.

O sistema simula um marketplace onde vendedores podem cadastrar produtos, clientes podem realizar pedidos e o sistema mantém controle de estoque automaticamente após a confirmação de um pedido.

---

# Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- JWT a partir do DRF
- SQLite

---

# Funcionalidades

- Cadastro de vendedores
- Cadastro de clientes
- Cadastro de produtos
- Associação de tags a produtos
- Registro de pedidos
- Registro de itens de pedido
- Consulta de produtos vendidos
- Estatísticas de produtos
- Consulta de pedidos abertos
- Controle automático de estoque via Signals
- API REST utilizando ViewSets

---

# Modelo de Dados

## PerfilVendedor

Representa os vendedores cadastrados na plataforma.

Campos:

- user
- cpf
- data_nascimento
- telefone

## PerfilCliente

Representa os clientes da plataforma.

Campos:

- user
- cpf
- data_nascimento
- telefone

## Tag

Categorias aplicadas aos produtos.

Campos:

- nome

## Produto

Representa um produto anunciado.

Campos:

- vendedor
- tags
- nome
- descricao
- preco
- quantidade_estoque

## Pedido

Representa uma compra realizada por um cliente.

Campos:

- cliente
- data_pedido
- status

Status possíveis:

- Aberto
- Confirmado
- Cancelado

## ItemPedido

Tabela intermediária entre Pedido e Produto.

Campos:

- pedido
- produto
- quantidade
- preco_venda

---

# Regras de Negócio

## Pedidos Abertos

Foi implementado um Manager customizado para retornar apenas pedidos cujo status seja "aberto". Com ele foi trabalhado o Padrão Factory do Django, sendo possível observá-lo no endpoint `/api/pedidos-abertos/`

## Preço da Venda

Ao criar um ItemPedido, o campo `preco_venda` recebe automaticamente o preço atual do produto.

Isso garante que alterações futuras no preço do produto não afetem vendas antigas. Vale ressaltar que essa foi uma mudança pessoal no projeto, feita com o objetivo de resolver um problema real e também eliminar a necessidade de dupla inserção do valor do produto.

## Controle de Estoque

Foi implementado um Signal utilizando `post_save`, assim, o estoque de produtos passa a ser atualizado automaticamente pelo próprio Django. Com a utilização desse Signal conseguimos observar mais um Padrão de Projeto do Django, sendo este o Padrão Observer.

Quando um pedido é alterado para:

CONFIRMADO

O sistema:

1. Percorre todos os itens do pedido.
2. Obtém os produtos associados.
3. Subtrai a quantidade vendida do estoque.
4. Salva o produto atualizado.

---

# Instalação e Execução

Clone o repositório em um diretório de sua preferência:

```bash
git clone https://github.com/benhurveber/Marketplace-simples-DS1.git
```

Entre na pasta do projeto:

```
cd Marketplace-simples-DS1
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

O projeto já contém um arquivo `db.sqlite3` com dados de exemplo para testes. Abaixo, segue o comando que pode ser executado para garantir que as migrações estejam sincronizadas e também a resposta que deve ser retornada pelo Django:

```bash
python manage.py migrate
```

```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, marketplace, sessions
Running migrations:
  No migrations to apply.
```

Uma vez que você seguiu corretamente todos os passos até aqui, deve agora criar seu super usuário para acessar o painel administrativo do Django.

Execute o comando abaixo, definindo usuário e senha que serão utilizados mais tarde:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Por padrão, o Django inicializa o servidor remoto na porta 8000 do computador e já disponibiliza um painel admiministrativo próprio, permitindo melhor visualização e controle dos dados. Acesse o painel pelo endpoint a seguir, informando seu usuário e senha criados para super usuário no passo anterior.

Endpoint admin:

```http
localhost:8000/admin/
```

---

# Endpoints Disponíveis

## Produtos

| Método | Endpoint | Descrição | Autenticação |
|---------|---------|---------|---------|
| GET | `/api/produtos/` | Lista todos os produtos | Não |
| GET | `/api/produtos/{id}/` | Retorna um produto | Não |
| POST | `/api/produtos/` | Cria um produto | Sim |
| PUT | `/api/produtos/{id}/` | Atualiza um produto | Sim |
| PATCH | `/api/produtos/{id}/` | Atualiza parcialmente um produto | Sim |
| DELETE | `/api/produtos/{id}/` | Remove um produto | Sim |

## Vendedores

| Método | Endpoint | Descrição | Autenticação |
|---------|---------|---------|---------|
| GET | `/api/vendedores/` | Lista todos os vendedores | Sim |
| GET | `/api/vendedores/{id}/` | Retorna um vendedor | Sim |
| POST | `/api/vendedores/` | Cria um vendedor | Sim |
| PUT | `/api/vendedores/{id}/` | Atualiza um vendedor | Sim |
| PATCH | `/api/vendedores/{id}/` | Atualiza parcialmente um vendedor | Sim |
| DELETE | `/api/vendedores/{id}/` | Remove um vendedor | Sim |


## Consultas e Estatísiticas
| Método | Endpoint | Descrição | Autenticação |
|---------|---------|---------|---------|
| GET | `/api/estatisticas-produtos/` | Estatísticas utilizando aggregate() | Não |
| GET | `/api/produtos-vendidos/` | Relatório utilizando annotate() | Não |
| GET | `/api/pedidos-abertos/` | Consulta utilizando Manager customizado | Não |


## Estatísticas dos Produtos

### Endpoint

```http
GET /api/estatisticas-produtos/
```

### Descrição

Retorna as estatísticas gerais dos produtos cadastrados. Endpoint criado a partir de QuerySets avançados, nesse caso, utilizando de aggregate.

### Exemplo de Resposta

```json
{
    "quantidade_produtos": 120,
    "preco_medio": 350.50,
    "maior_preco": 1200.00,
    "menor_preco": 49.99
}
```

---

## Produtos Vendidos

### Endpoint

```http
GET /api/produtos-vendidos/
```

### Descrição

Retorna a quantidade total vendida por  cada produto cadastrado. Nesse endpoint foi utilizado outro QuerySet avançado, dessa vez, annotate.

### Exemplo de Resposta

```json
[
  {
    "id": 1,
    "nome": "Monitor Gamer 24/ Full HD",
    "total_vendido": 2
  },
  {
    "id": 2,
    "nome": "Mouse Sem Fio Ergonomia",
    "total_vendido": null
  }
]
```

---

## Pedidos Abertos

### Endpoint

```http
GET /api/pedidos-abertos/
```

### Descrição

Retorna apenas pedidos cujo status esteja definido como aberto.

Como já informado anteriormente, esse endpoint foi construído a partir do Padrão Factory do Django. Nele foi possível utilizar de um  Manager personalizado para filtrar pedidos com status em aberto e retorná-los diretamento do gerenciador de objetos.

### Exemplo de Resposta

```json
[
  {
    "id": 3,
    "data_pedido": "2026-09-23T14:22:37.203634-03:00",
    "status": "aberto",
    "cliente": 1
  }
]
```

---

## Produtos

Os endpoints que utilizam das ViewSets são protegidos por meio de classes de permissão, se baseando em autenticação com JWT. Esse endpoint em específico pertence a classe "IsAuthenticatedOrReadOnly", sendo assim, é possível acessá-lo pelo método GET (leitura) sem a necessidade de qualquer autenticação.

Entretanto, para os demais métodos do protocolo HTTP (POST, PUT, PATCH e DELETE) se faz necessária a autenticação por meio do token JWT. A maneira de se obter o token e demais informações a seu respeito estão expostas mais abaixo no material.

### Listar Produtos

Retorna `200 OK`

```http
GET /api/produtos/
```

### Buscar Produto

```http
GET /api/produtos/{id}/
```

### Criar Produto (Autenticação necessária)

Retorna `201 Created`

```http
POST /api/produtos/
```

#### Exemplo de Requisição POST

```json
{
    "nome": "Controle de Xbox",
    "descricao": "Controle de Xbox sem fio",
    "preco": "299.90",
    "quantidade_estoque": 3,
    "vendedor": 1,
    "tags": [
        1
    ]
}
```

### Atualizar Produto (Autenticação necessária)

Retorna `200 OK`

```http
PUT /api/produtos/{id}/
```

#### Exemplo de Requisição PUT

```http
PUT /api/produtos/10/
```

```json
{
    "nome": "Controle de Xbox",
    "descricao": "Controle de Xbox sem fio",
    "preco": "199.90",
    "quantidade_estoque": 0,
    "vendedor": 1,
    "tags": [
        1,
        2
    ]
}
```

### Atualização Parcial (Autenticação necessária)

Retorna `200 OK`

```http
PATCH /api/produtos/{id}/
```

#### Exemplo de Requisição PATCH

```http
PATCH /api/produtos/10/
```

```json
{
    "preco": "149.90"
}
```

### Excluir Produto (Autenticação necessária)

```http
DELETE /api/produtos/{id}/
```

#### Exemplos de Requisição DELETE

Retorna `204 No Content`

```http
DELETE /api/produtos/10/
```

---

## Vendedores

O endpoint de Vendedores também é protegido e possui uma classe de permissão, sendo essa a "IsAuthenticated". Entretanto, diferente do endpoint de Produtos, aqui todos os métodos HTTP exigem autenticação por meio de JWT, desde um simples GET para listar as informações até a deleção de um produto.

### Listar Vendedores (Autenticação necessária)

Retorna `200 OK`

```http
GET /vendedores/
```

### Buscar Vendedor (Autenticação necessária)

```http
GET /vendedores/{id}/
```

### Criar Vendedor (Autenticação necessária)

Retorna `201 Created`

```http
POST /api/vendedores/
```

#### Exemplo de Requisição POST

```json
{
    "cpf": "80560080399",
    "data_nascimento": "2000-09-01",
    "telefone": "51992884920",
    "user": 2,
    "produtos": [
    ]
}
```

### Atualizar Vendedor (Autenticação necessária)

Retorna `200 OK`

```http
PUT /vendedores/{id}/
```

#### Exemplo de Requisição PUT

```jsojn
PUT /api/vendedores/1/
```

```json
{
    "cpf": "25680589933",
    "data_nascimento": "2006-09-25",
    "telefone": "51992884920",
    "user": 2,
    "produtos": [
    ]
}
```

### Atualização Parcial (Autenticação necessária)

Retorna `200 OK`

```http
PATCH /vendedores/{id}/
```

#### Exemplo de Requisição PATCH

```jsojn
PUT /api/vendedores/10/
```

```json
{
    "data_nascimento": "2006-09-25"
}
```

### Excluir Vendedor (Autenticação necessária)

```http
DELETE /vendedores/{id}/
```

#### Exemplo de Requisição DELETE

Retorna `204 No Content`

```jsojn
PUT /api/vendedores/10/
```

---

# Autenticação com JWT

A partir do próprio Django Rest Framework foram utilizadas ferramentas para configurar autenticação com JWT funcional (obtenção e renovação de token). Além disso, também foi possível manter o endpoint de Vendedores totalmente protegido, só sendo acessível para usuários devidamente autenticados.

## Como funciona?

Inicialmente cada usuário deve solicitar a criação do seu par de tokens (access e refresh), devendo fazer isso ao acessar o seguinte endpoint:

```http
POST /api/token/
```

Enviando no corpo da requisição seu usuário e senha no formato JSON.

```json
{
    "username": "fulano",
    "password": "ciclano"
}
```

Após isso, deve ser obtido como resposta duas chaves de acesso, sendo elas "refresh" e "access", respectivamente.

Segue exemplo:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc5MTMxMTI1MywiaWF0IjoxNzkxMjI0ODUzLCJqdGkiOiJjOGE2OTUxMGY5YWE0N2JlYWI4NjI2OWU3YTZlODNmZSIsInVzZXJfaWQiOiIxIn0.HGNlxgh0H3zBCFCOTNQGLjX4F8HpO1_kXDXTNAinCH8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxMjI1MTUzLCJpYXQiOjE3OTEyMjQ4NTMsImp0aSI6IjQ2NDk0YWIzZGZlMDQyMmVhOGFlMGUyOTM5ODI1YmJlIiwidXNlcl9pZCI6IjEifQ._BHHj7h3hB1Dia-xoSsHWfKfuyUo7iMG7HkMqzRIXB8"
}
```

O token fornecido pela chave "access" serve para acessar os endpoints protegidos, assunto ao qual abordaremos mais a frente, possuindo curta duração de vida (5 minutos por padrão).

Uma vez que o token de acesso expire e você precisa de nova autenticação, deve agora acessar um novo endpoint exclusivo para solicitar recarregamento das chaves. A partir dele é possível obter como resposta um JSON com seu novo token de acesso.

Segue endpoint de refresh e exemplo de resposta do mesmo.

Endpoint:
```http
/api/token/refresh/
```

Exemplo de resposta esperada:
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxMjI4ODgzLCJpYXQiOjE3OTEyMjg1ODMsImp0aSI6IjE3YjA4YTdiYTNhZjQxOTViOTBhM2E2OWU1MDJhMjczIiwidXNlcl9pZCI6IjEifQ.LXRVeu7jkZ_vH7ZwHKY74aJk3JfcXK6_k0tMQp7MxjU"
}
```

## Utilizando token de acesso

Agora que você já sabe como obter seu token de acesso e até mesmo recarregá-lo, deve entender como utilizá-lo para se autenticar.

Leve em conta que vamos acessar o seguinte endpoint do projeto:

```http
GET /api/vendedores/
```

Por ele ser protegido, caso tente acessá-lo sem qualquer autenticação deve ser retornado o erro `401 Unauthorized`.

Para evitar isso, devemos passar no cabeçalho da requisição HTTP (Headers) o seguinte comando junto do token de acesso:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxMjI4ODgzLCJpYXQiOjE3OTEyMjg1ODMsImp0aSI6IjE3YjA4YTdiYTNhZjQxOTViOTBhM2E2OWU1MDJhMjczIiwidXNlcl9pZCI6IjEifQ.LXRVeu7jkZ_vH7ZwHKY74aJk3JfcXK6_k0tMQp7MxjU
```

Agora sendo possível acessá-lo e também visualizar o resultado esperado.

```json
[
    {
        "id": 1,
        "cpf": "60080580033",
        "data_nascimento": "2006-09-25",
        "telefone": "51994394987",
        "user": 2,
        "produtos": [
            {
                "id": 1,
                "nome": "Monitor Gamer 24/ Full HD",
                "descricao": "Monitor LED Full HD com taxa de atualização de 165Hz.",
                "preco": "899.90",
                "quantidade_estoque": 15,
                "vendedor": 1,
                "tags": [
                    1,
                    2
                ]
            }
        ]
    }
]
```

---

# Coleção Postman

O projeto inclui uma pequena coleção do Postman contendo um passo a passo demonstrando a obtenção e o correto funcionando dos tokens por JWT.

Essa coleção pode ser encontrada na raíz do projeto, basta procurar pelo seguinte arquivo:

`Marketplace.postman_collection.json`

### Importação

1. Abra o Postman.
2. Procure pela seta apontando para baixo no canto superior esquerdo.
2. Expanda o menu "file" e clique em **Import**.
3. Opte por escolher um arquivo e selecione `Marketplace.postman_collection.json`, presente na raíz do projeto.
4. Pronto! A coleção será carregada automaticamente.

---

# Recursos do Django Utilizados

- ModelSerializer
- ModelViewSet
- DefaultRouter
- ForeignKey
- OneToOneField
- ManyToManyField
- Custom Manager
- Custom QuerySet
- Signals
- aggregate()
- annotate()
- DRF
- JWT

---

# Autor

Ben-Hur Mattos Veber

Estudante de Análise e Desenvolvimento de Sistemas, atualmente no 4º período. Projeto destinado para a disciplina de Desenvolvimento de Sistemas I.
