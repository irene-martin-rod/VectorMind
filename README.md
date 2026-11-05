# VectorMind

**An Open-Source Scientific Information Retrieval Engine**

VectorMind is a modular information retrieval engine designed to benchmark and compare lexical, semantic, and hybrid search approaches over scientific literature.

The project focuses on reproducible experimentation, retrieval quality evaluation, and efficient local execution without requiring paid APIs or specialized hardware.

**Project status:** Early development.

## Key Features

VectorMind aims to provide:

- **Lexical Retrieval:** BM25-based document retrieval.
- **Semantic Retrieval:** Dense vector representations using Sentence Transformers.
- **Hybrid Retrieval:** Rank fusion combining lexical and semantic search.
- **Evaluation Framework:** Standard information retrieval metrics for measuring retrieval quality.
- **Reproducibility:** Configurable experiments, consistent evaluation protocols, and traceable results.
- **Local Execution:** Designed to run locally without paid external services or mandatory GPU acceleration.

## Initial Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Dataset | SciFact (BEIR) |
| Embedding Model | all-MiniLM-L6-v2 |
| Lexical Retrieval | BM25 (`rank-bm25`) |
| Dense Retrieval | Sentence Transformers |
| Vector Operations | NumPy |
| Data Processing | Pandas |
| Configuration | YAML |
| Hybrid Retrieval | Reciprocal Rank Fusion (RRF) |
| Evaluation | NDCG@10, Recall@10, MRR@10 |
| Testing | Pytest |
| Code Quality | Ruff |


## Project Structure

```text
vectormind/
│
├── configs/
│   └── baseline.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── artifacts/
│
├── reports/
│   ├── metrics/
│   └── figures/
│
├── src/
│   └── vectormind/
│       ├── __init__.py
│       │
│       ├── data/
│       │   └── __init__.py
│       │
│       ├── indexing/
│       │   └── __init__.py
│       │
│       ├── retrieval/
│       │   └── __init__.py
│       │
│       └── evaluation/
│           └── __init__.py
│
├── scripts/
├── tests/
│
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

### Directory Overview

| Directory | Purpose |
|---|---|
| `configs/` | Experiment configurations and baseline parameters. |
| `data/raw/` | Original datasets, kept separate from processed data. |
| `data/processed/` | Cleaned and transformed datasets ready for retrieval experiments. |
| `artifacts/` | Generated model artifacts, embeddings, and intermediate outputs. |
| `reports/metrics/` | Evaluation metrics and benchmark results. |
| `reports/figures/` | Visualizations and experiment charts. |
| `src/vectormind/data/` | Dataset loading, validation, and preprocessing. |
| `src/vectormind/indexing/` | Document indexing and vector index management. |
| `src/vectormind/retrieval/` | Lexical, semantic, and hybrid retrieval methods. |
| `src/vectormind/evaluation/` | Retrieval evaluation metrics and benchmarking utilities. |
| `scripts/` | Executable scripts for running experiments and project tasks. |
| `tests/` | Automated tests for project components. |

## Project Roadmap

- [ ] **v0.1 — Foundation:** Repository structure, environment setup, dataset loading, and data validation.
- [ ] **v0.2 — Retrieval Baselines:** BM25 and dense retrieval implementations.
- [ ] **v0.3 — Evaluation:** Reproducible benchmarks, retrieval metrics, and performance reporting.
- [ ] **v0.4 — Hybrid Retrieval:** Reciprocal Rank Fusion combining lexical and semantic results.
- [ ] **v1.0 — Integrated Retrieval Engine:** Complete retrieval pipeline, documented experiments, and evaluation results.

## Project Principles

1. Reproducibility over complexity.
2. Measurable improvements over assumptions.
3. Modular and maintainable architecture.
4. Zero-cost development and experimentation.
5. Hardware-independent design.
6. Open-source technologies and transparent evaluation.
7. Clear separation between experimental results and verified improvements.

## License

This project is licensed under the MIT License.

**Note:** The dataset and embedding model have their own independent licenses and usage conditions. Their terms must be respected separately from the project's source code license.
