# IPSS-R Calculator

## How to run locally

1. Clone the project and switch into the directory.
```sh
git clone https://github.com/vkapur2202/ipss-r-calculator.git calc
cd calc
```
2. Setup a python3 virtual environment and install the requirements.
We assume you have virtualenv and python3
```sh
# create the environment
virtualenv -p python3 venv
# activate the environment
source venv/bin/activate
# Install the requirements
pip install -r requirements.txt
```
3. Run the program within your virtual environment.
```sh
python calc.py
```
4. It should show you that it is listening on localhost:5000.

5. Open [http://localhost:5000](http://localhost:5000) in your browser.

6. Profit!
