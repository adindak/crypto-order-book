# Crypto Order Book

---

## Features

- **Add Orders:**  Bids (buy orders) and asks (sell orders) with custom prices and quantities.
- **Order Matching:** Automatically matches bids and asks based on price and quantity criteria.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook
- pip (Python package manager) --> Install Tabulate
- 

### Steps to Install

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repository/crypto-order-book.git
   cd crypto-order-book
   
Installation Tabulate
------------

To install the Python library and the command line utility, run:

```shell
pip install tabulate
```

The command line utility will be installed as `tabulate` to `bin` on
Linux (e.g. `/usr/bin`); or as `tabulate.exe` to `Scripts` in your
Python installation on Windows (e.g. `C:\Python39\Scripts\tabulate.exe`).

You may consider installing the library only for the current user:

```shell
pip install tabulate --user
```

In this case the command line utility will be installed to
`~/.local/bin/tabulate` on Linux and to
`%APPDATA%\Python\Scripts\tabulate.exe` on Windows.

To install just the library on Unix-like operating systems:

```shell
TABULATE_INSTALL=lib-only pip install tabulate
```

On Windows:

```shell
set TABULATE_INSTALL=lib-only
pip install tabulate
```

How To Run
------------

1. **Option 1: Run Locally**  
- Open a terminal in the project directory.
- Launch the Jupyter Notebook:
  
```shell
jupyter notebook
```
- Open the `crypto_order_book.ipynb` file.
- Execute the cells sequentially to add orders, match them, and visualize the results.

2. **Option 2: Run Online Using Google Colab**  
- Upload the `crypto_order_book.ipynb` file to Google Colab.
- Install the required dependencies in the first cell:
```shell
!pip install tabulate
```
- Run the cells to interact with the application.
