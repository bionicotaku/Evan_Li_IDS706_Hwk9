# Data Analysis Performance Comparison: Python vs Rust

[![Python CI/CD Pipeline](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk9/actions/workflows/pythonCI.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk9/actions/workflows/pythonCI.yml)
[![Rust CI/CD Pipeline](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk9/actions/workflows/rustCI.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk9/actions/workflows/rustCI.yml)

This project implements identical data analysis tasks in both Python and Rust, utilizing the Polars library for data processing. The analysis is performed on the Data Engineer Salary 2024 dataset, with performance metrics tracked for both implementations.

## Dataset

The data is sourced from [Kaggle's Data Engineer Salary in 2024 dataset](https://www.kaggle.com/datasets/chopper53/data-engineer-salary-in-2024), containing information about:
- Salary
- Job title
- Experience level
- Employment type
- Employee residence
- Remote work ratio
- Company location
- Company size

## Analysis Features

Both implementations perform the following analyses:
1. Top 20 Job Titles Distribution
2. Experience Level Distribution
3. Salary Statistics by Experience Level

## Python Implementation

### Setup and Running
1. Install dependencies: `make python_install`
2. Run analysis: `python python_proj/main.py`
3. Check code quality:
   - Format: `make python_format`
   - Lint: `make python_lint`
   - Test: `make python_test`

## Rust Implementation

### Setup and Running
1. Install dependencies: `make rust_install`
2. Run analysis: `cargo run`
3. Check code quality:
   - Format: `make rust_format`
   - Lint: `make rust_lint`
   - Test: `make rust_test`

## Performance Comparison

Performance metrics are automatically generated and saved to markdown files through GitHub Actions:
- [Python Performance Results](python_performance.md)
- [Rust Performance Results](rust_performance.md)

### Key Findings
Our analysis reveals that while the Rust implementation shows significantly lower memory consumption, the execution time improvement wasn't as dramatic as we'd typically expect. This interesting outcome might be attributed to several factors:

1. Differences in how the Polars library is implemented in Python versus Rust
2. Potential optimization opportunities in our Rust code due to limited expertise
3. The specific nature of our data processing tasks might not fully showcase Rust's performance advantages

## CI/CD Pipeline
Both implementations include automated CI/CD pipelines that:
- Run tests
- Check code formatting
- Perform linting
- Generate performance metrics
- Push results to the repository
