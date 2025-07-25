# Simulador de Memória Cache em Python

Este projeto é uma implementação de um simulador de memória cache, desenvolvido em Python para a disciplina de Arquitetura e Organização de Computadores. O programa simula o comportamento de diferentes configurações de cache (mapeamento, políticas de substituição) e analisa seu desempenho.

### 🎯 Descrição do Projeto

O simulador lê uma sequência de endereços de memória de 32 bits a partir de um arquivo de entrada. Para cada endereço, ele determina se o acesso resulta em um **hit** (o dado já está na cache) ou um **miss** (o dado precisa ser buscado na memória principal).

Ao final da simulação, o programa exibe estatísticas detalhadas de desempenho, incluindo a classificação dos misses em três categorias:
- **Miss Compulsório:** Ocorre na primeira referência a um bloco de memória. É inevitável.
- **Miss de Capacidade:** Ocorre quando a cache está cheia e o bloco desejado já foi descartado para dar espaço a outro, mesmo que não houvesse conflito de índice.
- **Miss de Conflito:** Ocorre em caches de mapeamento direto ou associativo por conjunto, quando dois blocos disputam o mesmo conjunto e um deles é descartado, mesmo que existam espaços vazios em outros conjuntos.

### ✨ Funcionalidades Implementadas

* **Tipos de Mapeamento:**
    * [x] Mapeamento Direto (`assoc = 1`)
    * [x] Mapeamento Associativo por Conjunto (`assoc > 1`)
    * [x] Mapeamento Totalmente Associativo (caso especial com `nsets = 1`)
* **Políticas de Substituição:**
    * [x] LRU (Least Recently Used)
    * [x] FIFO (First-In, First-Out)
    * [x] Aleatório (Random)
* **Estatísticas de Saída:**
    * Contagem total de acessos, hits e misses.
    * Contagem detalhada de misses (compulsório, capacidade, conflito).
    * Cálculo de taxas de acerto e erro para cada categoria.

### 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* Bibliotecas padrão: `sys`, `math`, `random`.

---

### 🚀 Como Executar

Para executá-lo, utilize o interpretador Python 3 e passe os parâmetros da simulação via linha de comando.

**1. Clone o Repositório**
```bash
git clone [https://github.com/PMota173/cache-simulator.git](https://github.com/PMota173/cache-simulator.git)
cd cache-simulator
```

**2. Execute o Simulador**

O script deve ser executado com 6 argumentos, seguindo o formato abaixo:

```bash
python cache_simulator.py <nsets> <bsize> <assoc> <subst> <flag_saida> <arquivo_bin>
```

**Parâmetros:**

* `<nsets>`: Número de conjuntos (linhas) na cache.
* `<bsize>`: Tamanho do bloco (em bytes).
* `<assoc>`: Nível de associatividade (número de vias por conjunto).
* `<subst>`: Política de substituição a ser usada:
    * `L` ou `l` para **LRU**.
    * `F` ou `f` para **FIFO**.
    * `R` ou `r` para **Random**.
* `<flag_saida>`: Formato da saída dos resultados:
    * `0` para o formato completo e legível.
    * `1` para um formato compacto, ideal para scripts.
* `<arquivo>`: Caminho para o arquivo de binário.

**Exemplo de Execução:**
```bash
python cache_simulator.py 64 8 2 l ../Testes/bin_100.bin
```

### 📈 Saída do Programa

Dependendo da `flag_saida`, o programa exibirá as estatísticas de duas formas:

**`flag_saida = 0` (Formato Completo):**
```
Total acessos:           100000
Total hits:              87491
Total misses:            12509
Total misses comp:       3134
Total misses cap:        0
Total misses conf:       9375
Taxa hit:                87.49%
Taxa miss:               12.51%
Taxa miss compulsório:   25.05%
Taxa miss de capacidade: 0.00%
Taxa miss de conflito:   74.95%
```

**`flag_saida = 1` (Formato Compacto):**
```
100000 0.8749 0.1251 0.25 0.00 0.75
```
*(Valores correspondem a: Total de acessos, Taxa de Hit, Taxa de Miss, Taxa de Miss Compulsório, Taxa de Miss de Capacidade, Taxa de Miss de Conflito)*

---
### Autores

* **Pedro Mota** - [GitHub](https://github.com/PMota173)
* **Marlon Weber** - [GitHub](https://github.com/MarlonWeber1)
