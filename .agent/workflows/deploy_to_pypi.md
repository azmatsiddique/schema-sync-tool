---
description: How to deploy schema-sync to PyPI
---

This workflow describes the steps to build and deploy the `schema-sync` package to PyPI.

## Prerequisites
Ensure `pip` is up to date and install build tools.

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build twine
```

## 1. Build the Package
Generate distribution archives (sdist and wheel).

```bash
// turbo
python3 -m build
```

This will create a `dist/` directory containing the `.tar.gz` and `.whl` files.

## 2. Upload to TestPyPI (Optional but Recommended)
Upload to TestPyPI to verify everything looks correct. You will need a TestPyPI account.

```bash
python3 -m twine upload --repository testpypi dist/*
```

## 3. Upload to PyPI
Upload the package to the real PyPI. You will need a PyPI account.

```bash
python3 -m twine upload dist/*
```
