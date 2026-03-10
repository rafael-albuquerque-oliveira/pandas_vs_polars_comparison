# 🚀 Data Engineering Bootcamp - Semana 1: Modern Python & Polars

Este repositório contém o desenvolvimento prático da primeira semana do Bootcamp de Engenharia de Dados Moderna, com foco na transição de ferramentas tradicionais para ecossistemas baseados em Rust para alta performance.

## 🎯 Objetivo do Projeto
O objetivo desta etapa foi construir e validar um pipeline de ingestão e processamento de dados robusto, substituindo o Pandas pelo Polars para lidar com volumes médios/grandes de dados (GBs) localmente, garantindo eficiência extrema no uso de memória RAM e tempo de execução.

## 📊 O Desafio: "O Benchmark"
Para provar a eficiência da nova stack, desenvolvi um script de estresse comparando o processamento de um grande volume de dados (NYC Taxi Dataset) usando **Pandas (Eager Evaluation)** e **Polars (Lazy Evaluation)**.

O pipeline de teste consistiu em:
1. Leitura de um arquivo CSV (> 1GB).
2. Filtragem de registros (corridas com mais de 1 passageiro).
3. Agregação de dados (cálculo do valor médio da tarifa por local de embarque).
4. Ordenação dos resultados.

### Resultados Obtidos
Abaixo está o gráfico gerado automaticamente pelo script de benchmark, evidenciando o consumo de recursos:

![Resultados do Benchmark](benchmark_real_resultado.png)

* **Tempo de Execução:** O Polars processou o dataset em **[2.84]s**, contra **[16.07]s** do Pandas (uma redução de tempo de X%).
* **Consumo de Memória (Pico RAM):** O Polars utilizou apenas **[1142]MB**, enquanto o Pandas exigiu **[1623]MB** da máquina.

## 💼 Impacto no Negócio
A adoção do Apache Arrow e da avaliação preguiçosa (Lazy Evaluation) pelo Polars não é apenas uma melhoria de sintaxe, mas uma mudança arquitetural que gera valor direto para o negócio:
* **Redução de Custos de Infraestrutura (Cloud):** A drástica diminuição no pico de memória RAM permite processar os mesmos dados em máquinas virtuais muito mais baratas.
* **Agilidade na Tomada de Decisão:** Reduzir o tempo de processamento de horas para minutos garante que as áreas de negócio e modelos de Machine Learning recebam dados atualizados mais rapidamente, mitigando gargalos operacionais.

## 🛠️ Tech Stack Utilizada
* **Python 3.12+**
* **Polars** (Processamento Lazy e Zero-copy memory)
* **Pandas** (Para baseline de comparação)
* **Matplotlib & Memory-Profiler** (Para medição e visualização de performance)

---
*Projeto desenvolvido como parte do aprimoramento contínuo em arquiteturas de dados modernas e eficientes.*
