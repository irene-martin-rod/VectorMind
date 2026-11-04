# VectorMind

**An Open-Source Scientific Information Retrieval Engine**

VectorMind is a modular information retrieval engine designed to benchmark and compare lexical, semantic, and hybrid search approaches over scientific literature.

The project focuses on reproducible experimentation, retrieval quality evaluation, and efficient local execution without requiring paid APIs or specialized hardware.

## Key Features

- **Lexical Retrieval:** BM25-based document retrieval.
- **Semantic Retrieval:** Dense vector representations using Sentence Transformers.
- **Hybrid Retrieval:** Rank fusion combining lexical and semantic search.
- **Evaluation Framework:** Standard information retrieval metrics.
- **Reproducibility:** Configurable experiments and traceable results.
- **Local Execution:** Designed to run without paid external services.

## Initial Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| Dataset | SciFact (BEIR) |
| Embedding Model | all-MiniLM-L6-v2 |
| Lexical Search | BM25 |
| Vector Operations | NumPy |
| Hybrid Search | Reciprocal Rank Fusion |
| Evaluation | NDCG@10, Recall@10, MRR@10 |
| Testing | Pytest |
| Code Quality | Ruff |

## Project Roadmap

- [ ] **v0.1 — Foundation:** Repository structure, dataset loading and validation.
- [ ] **v0.2 — Baselines:** BM25 and dense retrieval implementations.
- [ ] **v0.3 — Evaluation:** Reproducible benchmark and performance reporting.
- [ ] **v0.4 — Hybrid Retrieval:** Reciprocal Rank Fusion.
- [ ] **v1.0 — Intelligent Retrieval Engine:** Integrated retrieval pipeline and documented evaluation results.

## Project Principles

1. Reproducibility over complexity.
2. Measurable improvements over assumptions.
3. Modular architecture.
4. Zero-cost development environment.
5. Hardware-independent design.
6. Open-source technologies and transparent evaluation.

## License

This project is licensed under the MIT License.

**Note:** Dataset and model licenses are independent of the project's source code license.