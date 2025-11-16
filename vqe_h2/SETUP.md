# VQE H₂ Simulator - Complete Setup & Usage Guide

## 🚀 Quick Start

### Windows (PowerShell)
```powershell
cd "path\to\vqe_h2"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### Windows (Command Prompt)
```cmd
cd path\to\vqe_h2
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
```

### macOS / Linux
```bash
cd path/to/vqe_h2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 📋 Prerequisites

- **Python:** 3.8 or higher
- **pip:** Latest version
- **RAM:** At least 2GB free memory
- **Disk Space:** ~500MB for all dependencies

Check your Python version:
```bash
python --version
```

## 💾 Installation Steps

### 1. Create Virtual Environment

**Why?** Isolates project dependencies from your system Python.

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Alternative (if requirements.txt fails):**
```bash
pip install qiskit numpy scipy matplotlib plotly streamlit --upgrade
```

### 4. Verify Installation

```bash
python -c "import qiskit; print(f'Qiskit version: {qiskit.__version__}')"
python -c "import streamlit; print(f'Streamlit version: {streamlit.__version__}')"
```

## 🎮 Running the Application

### Method 1: Using Streamlit Directly (Recommended)
```bash
streamlit run app.py
```

### Method 2: Using Startup Script (Windows)
```powershell
.\run_app.ps1
```

### Method 3: Using Batch Script (Windows)
```cmd
run_app.bat
```

The app will open in your browser at: **http://localhost:8501**

## 💻 Using the VQE Algorithm Directly

### Example 1: Basic Optimization
```python
from vqe_h2 import H2VQE
import numpy as np

# Create VQE solver
vqe = H2VQE(bond_length=0.735)

# Run optimization
energy, params = vqe.optimize(maxiter=100)

print(f"Optimal Energy: {energy:.6f} Hartree")
print(f"Parameters: {params}")
```

### Example 2: Running Quick Examples
```bash
python quick_example.py
```

This will run 4 example scenarios and generate plots.

### Example 3: Running Tests
```bash
python test_vqe.py
```

## 🎛️ UI Controls Explanation

### Left Sidebar

**VQE Settings:**
- **Bond Length:** Adjust the distance between H atoms (0.3-2.0 Å)
- **Max Iterations:** Number of optimization steps (10-200)
- **Run VQE Button:** Start the optimization

**Display Options:**
- Toggle energy curve visibility
- Toggle convergence plot
- Toggle 3D visualization
- Toggle circuit information

### Main Display

**Results Summary:**
- Optimal energy in Hartree
- Bond length used
- Number of iterations
- Theoretical error

**Visualizations:**
- Convergence plot (energy vs iteration)
- Potential energy surface
- Bloch sphere representation
- Molecular geometry in 3D

## 📊 Understanding the Visualizations

### Convergence Plot
Shows how the algorithm's energy estimate improves with each iteration. Should typically decrease monotonically.

### Energy Curve
Plots the H₂ molecular potential energy surface. Should show:
- Minimum near 0.735 Å (equilibrium)
- Rising curve at short and long distances
- Asymptotic approach to -1.0 Hartree at large distances

### Bloch Sphere
3D representation of quantum states. Red lines show state vectors on the unit sphere.

### Molecular Geometry
Shows the H₂ molecule with:
- Two red dots (nuclei)
- Blue cloud (electron probability density)

## 🔧 Troubleshooting

### Issue: "Module not found" errors
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: Streamlit won't start
```bash
# Check if Streamlit is installed
pip list | grep streamlit

# Reinstall Streamlit
pip install streamlit --upgrade
```

### Issue: Slow convergence or high energy values
- Reduce max iterations to see initial behavior
- Try different bond lengths
- Check that Qiskit is properly installed

### Issue: Port 8501 already in use
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Issue: Virtual environment won't activate (Windows)
Enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📁 Project Files

```
vqe_h2/
├── app.py                    # Main Streamlit UI (RUN THIS)
├── vqe_h2.py                 # VQE algorithm core
├── quick_example.py          # Example usage
├── test_vqe.py              # Unit tests
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── SETUP.md               # This file
├── run_app.bat            # Windows startup (cmd)
├── run_app.ps1            # Windows startup (PowerShell)
└── .gitignore             # Git ignore patterns
```

## 🧪 Testing

Run comprehensive tests:
```bash
python test_vqe.py
```

Expected output:
```
test_initialization ... ok
test_bond_length_variation ... ok
test_hamiltonian_coefficients ... ok
test_ansatz_circuit ... ok
...
Ran 20 tests
OK
```

## 📈 Performance Tips

1. **First Time:** May take longer due to Qiskit compilation
2. **Bond Length:** Results vary with bond length. 0.735 Å is equilibrium
3. **Iterations:** More iterations = better convergence but longer time
4. **Energy Curve:** Sampling fewer points (5 instead of 15) is faster

## 🌐 Web Interface Tips

- **Refresh:** Cmd/Ctrl + R or browser refresh button
- **Stop:** Ctrl + C in terminal, or close browser
- **Restart:** Close and re-run `streamlit run app.py`
- **Debug:** Check terminal output for errors

## 📚 Learning Resources

- **Qiskit Docs:** https://qiskit.org/documentation/
- **VQE Paper:** arXiv:1509.04279
- **Quantum Computing:** https://www.ibm.com/quantum/
- **Streamlit Docs:** https://docs.streamlit.io/

## 💡 Physics Background

### Key Concepts

**Variational Principle:**
The expectation value of any normalized state is always ≥ ground state energy

**H₂ Molecule:**
- 2 hydrogen atoms, 2 electrons total
- Simplest covalent bond system
- Ground state energy ≈ -1.17 Hartree

**VQE Algorithm:**
1. Prepare quantum state with trainable parameters
2. Measure energy expectation value
3. Adjust parameters to minimize energy
4. Repeat until convergence

## 🎯 Expected Results

**Typical Run:**
- **Initial Energy:** -0.5 to 0.5 Hartree (random)
- **Final Energy:** -1.1 to -1.2 Hartree (good)
- **Convergence:** 20-100 iterations
- **Time:** 30-150 seconds

**Factors Affecting Results:**
- Initial parameter values (random)
- Number of iterations
- Bond length
- Optimization method

## ⚠️ Important Notes

1. **Simulation:** This uses classical simulation, not real quantum hardware
2. **Approximation:** Simplified 2-qubit Hamiltonian
3. **Performance:** Results depend on initial conditions
4. **Noise:** Real quantum hardware would have additional noise

## 🚀 Next Steps

1. Run the quick examples: `python quick_example.py`
2. Launch the UI: `streamlit run app.py`
3. Try different bond lengths (0.3-2.0 Å)
4. Observe convergence behavior
5. Experiment with iteration counts
6. Check the energy curve across different bonds

## 💬 Support & Questions

### Common Questions

**Q: Why does energy sometimes increase?**
A: Optimization algorithm may need more iterations or different starting point.

**Q: Is this real quantum computing?**
A: No, this uses classical simulator. Real quantum computers would show different behavior.

**Q: Can I modify the code?**
A: Yes! The code is fully editable and documented.

**Q: How accurate are the results?**
A: This is an approximation. Exact: -1.1743 Hartree. We typically get -1.0 to -1.15.

### Debugging

Enable verbose output:
```python
# In vqe_h2.py, add before optimization:
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📝 Citation

If using this in research, cite as:
```
VQE H₂ Simulator (2025)
Educational implementation of Variational Quantum Eigensolver
```

## 📄 License

MIT License - Free to use and modify

---

**Version:** 1.0
**Last Updated:** 2025
**Python:** 3.8+
**Status:** Working
