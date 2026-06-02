# TB_graphene_nanotubes
This project performs graphene and single-walled nanotubes electronic band structure calculations with the tight binding method and nearest neighbours approximation. Written for the "Computational materials physics" and "Software and computing for applied physics" Unibo master courses.

---
## Features

**Graphene**
- Simulate pi-band dispersion along high symmetry lines in the Brillouin zone ($M$ to $\Gamma$ to $K$ to $M$)
- Customize precision (number of evaluated k-points)
- Customize tight-binding parameters or use default reasonable values (see paper referencia)
- Plot the energy bands, plot saving can be done manually with the GUI interface

**Nanotubes**
- Simulate arbitrary (n,m) nanotube energy bands inside the 1D restricted brillouin zone ($\Gamma$ to $X$)
- Customize precision (number of evaluated k-points)
- Customize tight-binding parameters or use default reasonable values (see paper referencia)
- Plot the energy bands, plot saving can be done manually with the GUI interface

---
## Requirements

**Software**
- [Python](https://www.python.org/) 3.12 or newer 

**Python libraries**
- [NumPy](https://numpy.org/) 
- [Matplotlib](https://matplotlib.org/)
- [Pytest](https://docs.pytest.org/en/stable/)

**For correct font in plotting window**
- Times New Roman font installed

---
## Running and testing the program

Clone the repository and open its main folder, then:

- In windows PowerShell:  
  
```powershell
python.exe main.py  
```  

- In WSL or other Linux bash:

```bash
python3 main.py  
```  

**Input**
The program will ask:  

1. Material type (`graphene` or `nanotube`)  
2. Nanotube indices (`n` and `m`) if you chose nanotube (non negative integers and at least one of them nonzero) 
3. Reciprocal-space resolution/precision (integer greater than 1) 
4. If you want to use custom tight-binding parameters ($\epsilon_{2p}$, $\gamma_0$, $s_0$) and in case you do it asks for their values (numbers convertible to floats)

**Output**
The program will:

- Print the calculated energy bandgap for the chosen material in the terminal
- Display the calculated band structure on a Matplotlib window.

**Testing**
Still inside the main folder, write:

```
pytest
```

Works both inside PowerShell and bash. Use the option -v for more detailed info.

---
## Physics background

For a detailed explanation of the relevant theory aspects behind this simulation, please refer to the documentation file referencia.

---

## Project Structure  

**Import dependencies visualization:**

```text  
TB_graphene_nanotubes/  
│  
├── main.py  
	└─ input_handler.py
	└─ eb_simulation.py
		└─ graphene_space.py
		└─ nanotube_space.py
		└─ tb_simple_nn.py
```
  
| File                | Purpose                                      | **Imports**                                  |
| ------------------- | -------------------------------------------- | -------------------------------------------- |
| `main.py`           | Program entry point and plotting             | eb_simulation, input_handler                 |
| `eb_simulation.py`  | Band structure calculations                  | graphene_space, nanotube_space, tb_simple_nn |
| `graphene_space.py` | Graphene reciprocal-space paths construction |                                              |
| `nanotube_space.py` | Nanotube reciprocal-space paths construction |                                              |
| `tb_simple_nn.py`   | Tight-binding equations                      |                                              |
| `input_handler.py`  | User input management                        |                                              |
| `tests/`            | Automated pytest test suite                  | each test_name.py imports at least name.py   |
  
---

## Suggested future improvements

- Density of states (DOS) calculations addon 
- Better handling of bandgap calculation and band plotting near the $K$ symmetry points when using low precision 