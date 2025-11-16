"""
Verification script to check if all dependencies are properly installed
"""

import sys
import importlib


def check_module(module_name, display_name=None):
    """Check if a module is installed"""
    display_name = display_name or module_name
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, '__version__'):
            version = module.__version__
            print(f"✓ {display_name:<20} {version}")
        else:
            print(f"✓ {display_name:<20} (installed)")
        return True
    except ImportError:
        print(f"✗ {display_name:<20} (NOT INSTALLED)")
        return False


def main():
    print("\n" + "="*60)
    print("VQE H₂ SIMULATOR - DEPENDENCY VERIFICATION")
    print("="*60 + "\n")
    
    modules_to_check = [
        ('qiskit', 'Qiskit'),
        ('qiskit_aer', 'Qiskit-Aer'),
        ('numpy', 'NumPy'),
        ('scipy', 'SciPy'),
        ('matplotlib', 'Matplotlib'),
        ('plotly', 'Plotly'),
        ('streamlit', 'Streamlit'),
    ]
    
    print("Checking installed packages:\n")
    
    all_installed = True
    for module_name, display_name in modules_to_check:
        if not check_module(module_name, display_name):
            all_installed = False
    
    print("\n" + "-"*60)
    
    if all_installed:
        print("✓ All required dependencies are installed!")
        print("\nYou can now run:")
        print("  streamlit run app.py")
        return 0
    else:
        print("✗ Some dependencies are missing.")
        print("\nInstall them with:")
        print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
