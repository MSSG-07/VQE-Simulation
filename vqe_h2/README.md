# VQE H₂ Simulator

A Streamlit-based interactive application for simulating the Variational Quantum Eigensolver (VQE) algorithm to find the ground state energy of the H₂ molecule.

## Features

✨ **Core Features:**
- Variational Quantum Eigensolver implementation using Qiskit
- Interactive Streamlit UI with real-time visualizations
- Dynamic bond length adjustment
- Energy curve (potential energy surface) calculation
- Convergence tracking and analysis
- Hardware-efficient ansatz circuit
- COBYLA classical optimization

📊 **Visualizations:**
- Real-time convergence plots
- Energy vs. iteration graphs
- Molecular potential energy surfaces
- 3D Bloch sphere representation
- H₂ molecular geometry visualization
- Circuit structure information

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Create and activate virtual environment:**
```bash
cd vqe_h2
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install qiskit numpy scipy matplotlib plotly streamlit
```

## Usage

### Running the Application

```bash
streamlit run app.py
```

This will open the web interface in your default browser (typically at `http://localhost:8501`).

### Using the VQE Algorithm Directly

```python
from vqe_h2 import H2VQE
import numpy as np

# Create VQE solver
vqe = H2VQE(bond_length=0.735)

# Run optimization
optimal_energy, optimal_params = vqe.optimize(maxiter=100)

print(f"Optimal Energy: {optimal_energy:.6f} Hartree")
print(f"Bond Length: {vqe.bond_length:.3f} Å")

# Get optimization history
history = vqe.get_history()
```

## Application Interface

### Sidebar Controls

1. **VQE Settings Tab:**
   - Bond Length slider (0.3 - 2.0 Å)
   - Maximum iterations selector
   - Run VQE button

2. **Display Options Tab:**
   - Show/hide energy curve
   - Show/hide convergence plot
   - Show/hide 3D visualization
   - Show/hide circuit information

3. **Info Tab:**
   - About VQE algorithm
   - About H₂ molecule
   - About Qiskit

### Main Display

- **Results Summary:** Energy, bond length, iterations, error metrics
- **Convergence Plot:** Energy vs. iteration during optimization
- **Energy Curve:** Potential energy surface as function of bond length
- **3D Visualizations:** Bloch sphere and molecular geometry
- **Circuit Details:** Gate structure and Hamiltonian information

## Algorithm Details

### VQE Overview

The Variational Quantum Eigensolver combines quantum computing with classical optimization:

1. **Ansatz Design:** Hardware-efficient parameterized circuit
2. **Hamiltonian Mapping:** Electronic Hamiltonian → Qubit operators
3. **Energy Measurement:** Expectation value on quantum simulator
4. **Classical Optimization:** COBYLA minimizes energy
5. **Iteration:** Repeat until convergence

### Ansatz Circuit

The hardware-efficient ansatz consists of:
- Initial Hadamard layer (superposition)
- Parameterized rotation layers (RZ and RX gates)
- Entangling layer (CX gates)
- Second parameterized layer
- **Total parameters:** 8
- **Qubits:** 2

### H₂ Hamiltonian

The H₂ molecular Hamiltonian is mapped to a 2-qubit system:

```
H = h_II · I⊗I
  + h_ZZ · Z⊗Z
  + h_ZI · Z⊗I
  + h_IZ · I⊗Z
```

Coefficients depend on:
- Bond length (r)
- Electronic structure (empirically fitted)

### Optimization

The optimization uses the **COBYLA** (Constrained Optimization BY Linear Approximation) method:
- Derivative-free optimization
- Suitable for noisy quantum systems
- Max iterations: configurable (default 50)

## Expected Results

For a properly tuned VQE:
- **Equilibrium Energy:** ≈ -1.17 Hartree
- **Equilibrium Bond Length:** ≈ 0.735 Å
- **Convergence:** Typically 30-100 iterations

## Project Structure

```
vqe_h2/
├── app.py                 # Streamlit UI application
├── vqe_h2.py             # VQE algorithm implementation
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── test_vqe.py          # Unit tests
└── examples/
    └── quick_example.py  # Quick start example
```

## Requirements

See `requirements.txt`:
- qiskit >= 0.39
- qiskit-aer >= 0.12
- numpy >= 1.21
- scipy >= 1.7
- matplotlib >= 3.5
- plotly >= 5.0
- streamlit >= 1.20

## Physics Background

### H₂ Molecule

The hydrogen molecule (H₂) is the simplest neutral molecule:
- **Electronic Configuration:** 1s¹_A 1s¹_B
- **Ground State:** Singlet (both electrons paired)
- **Basis Functions:** Usually 2-4 (STO-3G to cc-pVTZ)

### Ground State Energy

The quantum mechanical ground state energy of H₂:
- **At equilibrium (r = 0.735 Å):** E₀ ≈ -1.1743 Hartree
- **Dissociation limit (r → ∞):** E → -1.0 Hartree (2 × E(H atom))

### Energy Curve

The potential energy surface exhibits:
- **Minimum** at equilibrium bond length
- **Attractive region** at short-to-medium distances
- **Repulsive region** at very short distances
- **Attractive-repulsive crossover**

## Troubleshooting

### Installation Issues

**Problem:** Qiskit installation fails
```bash
# Solution: Install Qiskit separately
pip install --upgrade pip setuptools wheel
pip install qiskit --no-cache-dir
```

**Problem:** Streamlit not found
```bash
# Solution: Ensure virtual environment is activated
pip install streamlit
```

### Runtime Issues

**Problem:** Simulation takes too long
- Reduce max iterations
- Lower bond curve sampling points
- Use default bond length (0.735 Å)

**Problem:** Energy curve shows unrealistic values
- This is normal for very short/long distances
- Physical range: 0.3 - 2.0 Å

## Performance Notes

- **Simulation Speed:** ~1-5 seconds per iteration (CPU)
- **Full Optimization:** ~30-150 seconds (50-100 iterations)
- **Energy Curve:** ~15-30 seconds (15 points)

For faster computation, consider:
- GPU acceleration (via Qiskit GPU support)
- Fewer iterations
- Smaller ansatz circuit

## Educational Value

This project demonstrates:
1. Quantum circuit design principles
2. Variational quantum algorithms
3. Classical-quantum hybrid optimization
4. Molecular simulation basics
5. Interactive scientific computing
6. Quantum chemistry foundations

## Further Reading

- Qiskit Documentation: https://qiskit.org/documentation/
- VQE Papers: https://arxiv.org/abs/1509.04279
- Quantum Chemistry: https://www.nature.com/articles/nature23879

## References

1. Aspuru-Guzik, A., et al. (2005). "Simulated quantum computation of molecular energies." Science, 309(5741), 1704-1707.

2. O'Malley, P. J. J., et al. (2016). "Scalable Quantum Simulation of Molecular Energies." Physical Review X, 6(3), 031007.

3. Cao, Y., et al. (2019). "Quantum chemistry in the age of quantum computing." Chemical Reviews, 119(19), 10856-10915.

## License

MIT License - See LICENSE file for details

## Author

VQE H₂ Simulator Project
Created: 2025

## Support

For issues, questions, or suggestions:
- Check the troubleshooting section
- Review Qiskit documentation
- Consult quantum chemistry resources

---

**Disclaimer:** This is an educational tool. Results are approximations based on simplified models and classical simulation. Actual quantum hardware will have different characteristics due to noise and decoherence.
