# DataScience_AI_ML_NUS_EM

This repository contains a simple Python-based starter project for data science, machine learning, deep learning, and ETL experimentation.

## Project contents

- Python environment with NumPy, pandas, scikit-learn, TensorFlow, Keras, and PySpark
- Sample machine learning example in `src/hello.py`
- Simple TensorFlow example in `src/tensorflow_example.py`
- Basic PySpark ETL example in `src/pyspark_example.py`
- Tests under `tests/`

## Setup

Create and activate a virtual environment:

```bash
cd /workspaces/DataScience_AI_ML_NUS_EM
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Java requirement for PySpark

PySpark works best with Java 17 in this environment. Set the following before running Spark examples:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"
```

## Run examples

### Machine learning example

```bash
python main.py
```

### TensorFlow example

```bash
python src/tensorflow_example.py
```

### PySpark ETL example

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"
python src/pyspark_example.py
```

## Run tests

```bash
pytest -q
```
