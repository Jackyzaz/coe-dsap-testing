# Unittest with python
by Soravit Sukkarn Student ID: 6710110428

Assignment from **Data structure Algorithm and Programming module (240-123)**


## Coverage Test Result

![image](https://github.com/user-attachments/assets/82ecc4dc-de29-41f7-9b9f-1e171999fea7)



## Getting Start

```sh
python -m venv venv
```

### Window

```sh
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```sh
python3 -m venv venv
source/venv/bin/activate
```

### Install Package

```sh
pip install -r requirements.txt
```

<br/>

## Run Test

### Run a unit test

```sh
python -m unittest tests/test_(filename).py
```

### Run Coverage test

run every file start with `test_`

```sh
python -m coverage run -m unittest discover -s tests -p "test_*.py"
```

Print Report on terminal

```sh
python -m coverage report -m
```

(Optional) Convert to html file

```sh
coverage html
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS / linux
```
