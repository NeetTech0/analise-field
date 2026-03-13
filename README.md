# Gerador de Incidentes (Universo Umbra)

## Descrição

Este projeto é um **gerador probabilístico de eventos** dentro de um universo fictício que criei.
O sistema simula incidentes (ex: ataques de monstros em cidades/zonas) utilizando **pesos probabilísticos definidos no próprio código**.

Cada evento gerado possui:

* tipo de monstro (no universo é chamado "Eidryan")
* nível de ameaça do monstro (nivel 1 à 5)
* localização (cidade / zona)
* resultado do incidente (contido, falha, fuga)
* entre outros

Após gerar o evento e o resultado, o sistema **registra o incidente em um banco de dados**.

---

## Como o sistema funciona

O código é dividido em algumas partes principais:

### 1. Regras do universo

Arquivo responsável por definir os **pesos probabilísticos** utilizados na geração.

Aqui são definidos, por exemplo:

* probabilidade de tipos de ataque
* probabilidade de incidente por zona
* probabilidade de monstro por zona
* níveis de ameaça
* modificadores
* tempo de resposta por unidade
* distribuição de cidades e zonas

Esses pesos controlam **como o gerador se comporta**.

---

### 2. Gerador de eventos

Responsável por gerar o incidente em si.

Exemplo de evento gerado:

```
{'Região': 'TŌHOKU', 'Cidade': 'Miyagi', 'Zona': 'urbano', 'Eidryan': 'Incaris', 'Nivel': '3', 'Unidade': 'regular', 'Tempo': 'lenta'}
```

A geração utiliza os pesos definidos nas regras do universo.

---

### 3. Gerador de resultado do incidente

Depois que o evento é criado, o sistema gera o **resultado do incidente**, também usando probabilidades.

Exemplos:

* Contido
* Falha
* Fuga

---

### 4. Conexão com banco de dados

O arquivo `conexao.py` faz a conexão com o banco de dados.

⚠️ O sistema **não cria o banco automaticamente**.
Ele apenas **insere os eventos gerados**.

Portanto, o banco precisa existir antes de rodar o código.
O banco de dados utilizado no código se chama "decorp_field" e possui 3 entidades:

* eidryans (o tipo de monstro, raça e nivel)
* localidades (as cidades e zonas)
* incidentes (aqui é onde o código trabalha)

A entidade incidente faz relação com as entidades eidryans e localidades através das chaves:
* id_eidryan
* id_local

## Estrutura das Tabelas do Banco

### Tabela: `localidades`

| id  | regiao | zona         | cidade |
| --- | ------ | ------------ | ------ |
| 1   | Kanto  | urbano_denso | Tóquio |
| 2   | Kansai | urbano_denso | Osaka  |
| ... | ...    | ...          | ...    |

---

### Tabela: `eidryans`

| id  | tipo     | nivel_min | nivel_max |
| --- | -------- | --------- | --------- |
| 1   | Incaris  | 1         | 4         |
| 2   | Karnak   | 2         | 4         |
| ... | ...      | ...       | ...       |

---

### Tabela: `incidentes`

| id  | id_eidryan | id_local | nivel_eidryan | unidade       | tempo_resposta | resultado |
| --- | ---------- | -------- | ------------- | ------------- | -------------- | --------- |
| 1   | 1          | 8        | 1             | regular       | lenta          | contido   |
| 2   | 1          | 3        | 3             | especializada | muito_rapida   | contido   |
| ... | ...        | ...      | ...           | ...           | ...            | ...       |

---

### 5. Arquivo principal

O `main.py` é responsável por:

1. conectar ao banco
2. chamar o gerador de eventos
3. gerar o resultado do incidente
4. salvar o incidente no banco

---

## Requisitos

* Python 3.14.2
* Banco de dados configurado
* Estrutura do banco já criada

---

## Configuração do banco

Antes de rodar o projeto:

1. Crie o banco de dados manualmente
2. Garanta que a estrutura (tabelas) já esteja criada e normalizada
3. Edite o arquivo `conexao.py` com suas credenciais

Exemplo:

```
host = "127.0.0.1"
database = "nome_do_banco"
user = "usuario"
password = "senha"
```

---

## Observações

* Este projeto é um **experimento pessoal / hobby**.
* O objetivo é simular incidentes dentro de um universo fictício utilizando geração probabilística.
* O código foi desenvolvido como prática de programação, modelagem de dados e lógica de simulação.
