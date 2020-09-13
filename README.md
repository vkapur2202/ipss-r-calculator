# IPSS-R Calculator

## How to run locally

0. Clone the project and switch into the directory

```sh
git clone https://github.com/vkapur2202/ipss-r-calculator.git calc
cd calc
```

0. Setup a python3 virtual env and install the requirements.
We assume you have virtualenv and python3 installed.
```sh
# create the environment
virtualenv -p python3 venv
# activate the environment
source venv/bin/activate
# Install the requirements
pip install -r requirements.txt
```

0. Start the server
```sh
python calc.py
```

0. It should show you that it is listening on localhost:5000

0. Open (http://localhost:5000)[http://localhost:5000] in your browser.

0. Profit!
