# VQE H₂ Simulator - Quick Start Guide

## ⚡ 30-Second Start

### Windows Users:
```powershell
cd "C:\Users\M S Surya Gayathri\Desktop\New folder\vqe_h2"
.\run_app.ps1
```

The app will open automatically in your browser at `http://localhost:8501` ✨

---

## 📋 Complete Setup (5 minutes)

### Step 1: Navigate to Project
```bash
cd "C:\Users\M S Surya Gayathri\Desktop\New folder\vqe_h2"
```

### Step 2: Activate Virtual Environment
```bash
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Or Windows Command Prompt:
.venv\Scripts\activate.bat

# Or macOS/Linux:
source venv/bin/activate
```

### Step 3: Verify Installation
```bash
python verify_installation.py
```

You should see:
```
✓ Qiskit                 2.2.3
✓ NumPy                  2.3.4
✓ SciPy                  1.16.3
✓ Matplotlib             3.10.7
✓ Plotly                 6.4.0
✓ Streamlit              1.51.0
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

Browser opens automatically → Enjoy! 🎉

---

## 🎮 Using the Interface

### Left Sidebar
1. **Bond Length** - Drag to change (0.3 - 2.0 Å)
2. **Max Iterations** - Select 10-200 (default: 50)
3. **Run VQE Button** - Click to start optimization
4. Toggle visualization options

### Main Display
- **Results** - Energy, iterations, error metrics
- **Convergence Plot** - Watch energy decrease
- **Energy Curve** - Potential energy surface
- **3D Visualizations** - Bloch sphere and molecule
- **Circuit Info** - Gate structure details

---

## 💡 First Run Tips

1. **Default Settings**: Already optimized for learning
2. **Try This First**:
   - Click "Run VQE" (keeps default 0.735 Å)
   - Watch convergence for 1-2 minutes
   - Observe the energy decrease

3. **Then Experiment**:
   - Increase bond length to 1.0 Å
   - Run VQE again - energy goes UP ✓
   - Decrease to 0.5 Å - energy also UP ✓
   - Back to 0.735 Å - minimum energy ✓

4. **Explore Visualizations**:
   - Check "Convergence" - see optimization quality
   - Check "Energy Curve" - see molecular behavior
   - Check "3D Visualization" - rotate to explore

---

## 📚 Examples

### Quick Example Scripts
```bash
# Run 4 example scenarios
python quick_example.py

# Run unit tests
python test_vqe.py

# Verify installation
python verify_installation.py
```

### Direct Python Usage
```python
from vqe_h2 import H2VQE

# Create VQE solver
vqe = H2VQE(bond_length=0.735)

# Run optimization
energy, params = vqe.optimize(maxiter=100)

# Print results
print(f"Optimal Energy: {energy:.6f} Hartree")
print(f"Iterations: {vqe.iteration_count}")
```

---

## 🔍 Understanding Results

### Expected Values
- **Initial Energy**: -0.5 to +0.5 Hartree (random)
- **Final Energy**: -1.1 to -1.2 Hartree (optimized)
- **Theoretical**: -1.174 Hartree
- **Time**: 30-150 seconds

### Energy Curve Shape
```
Energy
  ↑
  │      *
  │    *   *
  │  *       *
  │*           *
  └────────────────→ Bond Length
      0.735 Å ← Minimum here
```

### Convergence Behavior
```
Energy
  ↑
-0.5├         
-1.0├   ╲╲
-1.1├      ╲╲╲___
-1.2├            ╲____
  └──────────────────→ Iteration
     Fast drop then plateaus ✓
```

---

## ⚙️ Common Adjustments

### Want Faster Results?
→ Reduce "Max Iterations" to 20-30

### Want Better Accuracy?
→ Increase "Max Iterations" to 100-200

### Want to See Different Molecular States?
→ Adjust "Bond Length" slider:
- 0.3 Å = Atoms very close (repulsive)
- 0.735 Å = Equilibrium (attractive minimum)
- 2.0 Å = Atoms far apart (separated)

### Want to Disable Animations?
→ Uncheck visualizations in sidebar

---

## 🚨 If Something Goes Wrong

### Port Already in Use?
```bash
streamlit run app.py --server.port 8502
```

### Dependencies Missing?
```bash
pip install -r requirements.txt --upgrade
```

### Virtual Environment Issues?
```bash
# Recreate environment
python -m venv venv_new
.venv_new\Scripts\activate
pip install -r requirements.txt
```

### Still Problems?
```bash
python verify_installation.py
python test_vqe.py
```

---

## 📖 Documentation

Quick Reference:
- **README.md** - Project overview
- **SETUP.md** - Installation troubleshooting
- **DOCUMENTATION.md** - Technical details
- **PROJECT_SUMMARY.md** - Complete status

---

## 🎯 Learning Path

### Beginner (30 mins)
1. Launch app and explore UI
2. Run VQE with default settings
3. Observe convergence
4. Try different bond lengths

### Intermediate (1-2 hours)
1. Study DOCUMENTATION.md
2. Run quick_example.py
3. Modify parameters in code
4. Run unit tests
5. Read algorithm details

### Advanced (2+ hours)
1. Study vqe_h2.py source code
2. Study app.py visualizations
3. Modify Hamiltonian coefficients
4. Implement custom ansatz
5. Add new features

---

## 🔗 Useful Resources

- **Qiskit Docs:** https://qiskit.org/documentation/
- **VQE Theory:** https://arxiv.org/abs/1509.04279
- **H₂ Chemistry:** Any quantum chemistry textbook
- **Streamlit Docs:** https://docs.streamlit.io/

---

## ✨ What You'll Learn

By using this simulator, you'll understand:
- ✅ Quantum circuits and gates
- ✅ Variational quantum algorithms
- ✅ Classical-quantum optimization
- ✅ Molecular quantum chemistry
- ✅ Energy calculations
- ✅ Scientific visualization

---

## 🎉 You're Ready!

Everything is installed and configured.

### To Start Now:
```bash
cd "C:\Users\M S Surya Gayathri\Desktop\New folder\vqe_h2"
.\run_app.ps1
```

### Have Fun Exploring Quantum Computing! 🚀⚛️

---

**Status:** ✅ Ready to Use
**Time to First Run:** < 1 minute
**Learning Curve:** Beginner-friendly
**Support:** Full documentation included
