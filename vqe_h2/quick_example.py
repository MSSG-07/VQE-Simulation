"""
Quick Example: Running VQE H2 Without UI
Simple script to run VQE optimization directly
"""

import numpy as np
import matplotlib.pyplot as plt
from vqe_h2 import H2VQE


def example_1_basic_optimization():
    """Example 1: Basic VQE optimization"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic VQE Optimization for H₂")
    print("="*60)
    
    # Create VQE solver at equilibrium bond length
    vqe = H2VQE(bond_length=0.735)
    
    # Run optimization
    optimal_energy, optimal_params = vqe.optimize(maxiter=50)
    
    print(f"\nResults:")
    print(f"  Optimal Energy: {optimal_energy:.6f} Hartree")
    print(f"  Bond Length: {vqe.bond_length:.3f} Å")
    print(f"  Iterations: {vqe.iteration_count}")
    print(f"  Parameters: {optimal_params}")
    
    return vqe


def example_2_multiple_bond_lengths():
    """Example 2: Optimization at different bond lengths"""
    print("\n" + "="*60)
    print("EXAMPLE 2: VQE at Multiple Bond Lengths")
    print("="*60)
    
    bond_lengths = [0.5, 0.735, 1.0, 1.5]
    energies = []
    
    for r in bond_lengths:
        print(f"\nOptimizing at bond length {r:.3f} Å...")
        vqe = H2VQE(bond_length=r)
        energy, _ = vqe.optimize(maxiter=30)
        energies.append(energy)
        print(f"  Energy: {energy:.6f} Hartree")
    
    print(f"\nBond Length (Å) | Energy (Hartree)")
    print("-" * 35)
    for r, e in zip(bond_lengths, energies):
        print(f"  {r:.3f}          | {e:.6f}")
    
    return bond_lengths, energies


def example_3_energy_curve():
    """Example 3: Full potential energy surface"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Potential Energy Surface")
    print("="*60)
    
    bond_lengths = np.linspace(0.4, 2.0, 12)
    
    print(f"\nCalculating energy curve ({len(bond_lengths)} points)...")
    vqe = H2VQE()
    bond_lengths_calc, energies = vqe.get_energy_curve(bond_lengths)
    
    print(f"Bond Length (Å) | Energy (Hartree)")
    print("-" * 35)
    for r, e in zip(bond_lengths_calc, energies):
        print(f"  {r:.3f}          | {e:.6f}")
    
    # Find minimum
    min_idx = np.argmin(energies)
    print(f"\nMinimum energy: {energies[min_idx]:.6f} Hartree")
    print(f"At bond length: {bond_lengths_calc[min_idx]:.3f} Å")
    
    return bond_lengths_calc, energies


def example_4_convergence_analysis():
    """Example 4: Analyze convergence behavior"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Convergence Analysis")
    print("="*60)
    
    vqe = H2VQE(bond_length=0.735)
    optimal_energy, _ = vqe.optimize(maxiter=100)
    
    history = vqe.get_history()
    energies = history['energies']
    iterations = history['iterations']
    
    print(f"\nConvergence Statistics:")
    print(f"  Initial Energy:  {energies[0]:.6f} Hartree")
    print(f"  Final Energy:    {energies[-1]:.6f} Hartree")
    print(f"  Energy Change:   {energies[-1] - energies[0]:.6f} Hartree")
    print(f"  Total Iterations: {iterations[-1]}")
    
    # Calculate convergence rate
    if len(energies) > 1:
        mid_point = len(energies) // 2
        early_rate = (energies[10] - energies[0]) / 10 if len(energies) > 10 else 0
        late_rate = (energies[-1] - energies[mid_point]) / (len(energies) - mid_point)
        
        print(f"\nConvergence Rates:")
        print(f"  Early iterations: {early_rate:.6f} Hartree/iteration")
        print(f"  Late iterations:  {late_rate:.6f} Hartree/iteration")
    
    return vqe


def plot_results(vqe, bond_lengths=None, energies=None):
    """Create visualization plots"""
    print("\nGenerating plots...")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Convergence
    if vqe and vqe.history['energies']:
        history = vqe.get_history()
        axes[0].plot(history['iterations'], history['energies'], 'b.-', linewidth=2, markersize=6)
        axes[0].set_xlabel('Iteration', fontsize=12)
        axes[0].set_ylabel('Energy (Hartree)', fontsize=12)
        axes[0].set_title('VQE Convergence', fontsize=14, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Energy curve
    if bond_lengths is not None and energies is not None:
        axes[1].plot(bond_lengths, energies, 'ro-', linewidth=2, markersize=6)
        axes[1].axvline(x=0.735, color='g', linestyle='--', label='Equilibrium')
        axes[1].set_xlabel('Bond Length (Å)', fontsize=12)
        axes[1].set_ylabel('Energy (Hartree)', fontsize=12)
        axes[1].set_title('H₂ Potential Energy Surface', fontsize=14, fontweight='bold')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('vqe_results.png', dpi=150, bbox_inches='tight')
    print("Saved plot to: vqe_results.png")
    plt.show()


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "VQE H₂ SIMULATOR - QUICK EXAMPLES" + " "*15 + "║")
    print("╚" + "="*58 + "╝")
    
    # Run examples
    vqe1 = example_1_basic_optimization()
    
    bond_lengths, energies = example_2_multiple_bond_lengths()
    
    bond_lengths_curve, energies_curve = example_3_energy_curve()
    
    vqe4 = example_4_convergence_analysis()
    
    # Create plots
    try:
        plot_results(vqe1, bond_lengths_curve, energies_curve)
    except Exception as e:
        print(f"Note: Plotting skipped ({e})")
    
    print("\n" + "="*60)
    print("Examples completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
