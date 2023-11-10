**Parsing cryptocurrency info by symbols**

**How to use:**

1. Clone repo:

**HTTPS:**  `https://github.com/vadbash/Pars-crypto-info-symbols.git`

**SSH:**  `git@github.com:vadbash/Pars-crypto-info-symbols.git`

2. Install all libraries with command `pip install -r requirements.txt`
3. There is folder **symbols** with all symbols and file named `symbols.py`
If you run that file all of symbols from that folder will be extract into **one csv file**.
4. **There is existing file with all of symbols (`symbols.csv`) so you can skip second point.**
5. Insert your **twelvedata api key** into `main.py` and run project.
6. You will see info about all of **cryptocurrency**(*symbol*, *datetime*, *open*, *high*, *low*, *close*) in the `data.csv`.