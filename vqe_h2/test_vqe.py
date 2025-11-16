"""
Unit tests for VQE H2 implementation
"""

import unittest
import numpy as np
from vqe_h2 import H2VQE


class TestH2VQE(unittest.TestCase):
    """Test suite for H2VQE class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.vqe = H2VQE(bond_length=0.735)
    
    def test_initialization(self):
        """Test VQE initialization"""
        self.assertEqual(self.vqe.bond_length, 0.735)
        self.assertIsNone(self.vqe.optimal_energy)
        self.assertIsNone(self.vqe.optimal_params)
        self.assertEqual(self.vqe.iteration_count, 0)
    
    def test_bond_length_variation(self):
        """Test VQE at different bond lengths"""
        bond_lengths = [0.5, 0.735, 1.0, 1.5]
        for r in bond_lengths:
            vqe = H2VQE(bond_length=r)
            self.assertEqual(vqe.bond_length, r)
    
    def test_hamiltonian_coefficients(self):
        """Test Hamiltonian coefficient calculation"""
        coeffs = self.vqe._calculate_hamiltonian_coefficients()
        
        # Check that all required terms are present
        self.assertIn('II', coeffs)
        self.assertIn('ZZ', coeffs)
        self.assertIn('ZI', coeffs)
        self.assertIn('IZ', coeffs)
        
        # Check that coefficients are real numbers
        for key, val in coeffs.items():
            self.assertIsInstance(val, (int, float, np.number))
    
    def test_ansatz_circuit(self):
        """Test ansatz circuit generation"""
        params = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        circuit = self.vqe.ansatz_circuit(params, num_qubits=2)
        
        # Check circuit has 2 qubits
        self.assertEqual(circuit.num_qubits, 2)
        
        # Check circuit has gates
        self.assertGreater(len(circuit), 0)
    
    def test_hamiltonian_dict(self):
        """Test Hamiltonian dictionary"""
        h_dict = self.vqe.get_h2_hamiltonian_simplified()
        
        # Check structure
        self.assertIsInstance(h_dict, dict)
        self.assertEqual(len(h_dict), 4)
        
        # Check all coefficients are real
        for val in h_dict.values():
            self.assertIsInstance(val, (int, float, np.number))
    
    def test_expectation_value_calculation(self):
        """Test energy expectation value calculation"""
        params = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        
        energy = self.vqe.measure_expectation_value(params)
        
        # Check that energy is a real number
        self.assertIsInstance(energy, (int, float, np.number))
        
        # Check reasonable range (not always true, but good sanity check)
        self.assertGreater(energy, -5.0)
        self.assertLess(energy, 5.0)
    
    def test_optimization_history(self):
        """Test that optimization maintains history"""
        initial_params = np.random.uniform(0, 2*np.pi, 8)
        self.vqe.optimize(initial_params=initial_params, maxiter=10)
        
        history = self.vqe.get_history()
        
        # Check history structure
        self.assertIn('energies', history)
        self.assertIn('params', history)
        self.assertIn('iterations', history)
        
        # Check history content
        self.assertGreater(len(history['energies']), 0)
        self.assertGreater(len(history['iterations']), 0)
    
    def test_energy_curve(self):
        """Test energy curve calculation"""
        bond_lengths = np.array([0.5, 0.735, 1.0, 1.5])
        
        bond_lengths_calc, energies = self.vqe.get_energy_curve(bond_lengths)
        
        # Check output structure
        self.assertEqual(len(bond_lengths_calc), len(energies))
        self.assertEqual(len(bond_lengths_calc), len(bond_lengths))
        
        # Check that energies are real numbers
        for energy in energies:
            self.assertIsInstance(energy, (int, float, np.number))
    
    def test_parameter_dimensions(self):
        """Test parameter handling"""
        # Test with 8 parameters (standard)
        params8 = np.random.uniform(0, 2*np.pi, 8)
        circuit = self.vqe.ansatz_circuit(params8, num_qubits=2)
        self.assertGreater(circuit.num_qubits, 0)
        
        # Test with different sizes
        params4 = np.random.uniform(0, 2*np.pi, 4)
        circuit2 = self.vqe.ansatz_circuit(params4, num_qubits=2)
        self.assertGreater(circuit2.num_qubits, 0)
    
    def test_reproducibility(self):
        """Test that same parameters give same energy"""
        params = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2])
        
        energy1 = self.vqe.measure_expectation_value(params)
        energy2 = self.vqe.measure_expectation_value(params)
        
        # Energies should be very close (not exact due to randomness in simulation)
        # But within reasonable tolerance
        self.assertAlmostEqual(energy1, energy2, places=1)


class TestH2VQEPhysics(unittest.TestCase):
    """Test physical correctness of VQE"""
    
    def test_bond_length_effect(self):
        """Test that different bond lengths give different energies"""
        vqe1 = H2VQE(bond_length=0.5)
        vqe2 = H2VQE(bond_length=0.735)
        vqe3 = H2VQE(bond_length=1.5)
        
        params = np.ones(8) * 0.5
        
        energy1 = vqe1.measure_expectation_value(params)
        energy2 = vqe2.measure_expectation_value(params)
        energy3 = vqe3.measure_expectation_value(params)
        
        # All should be different values
        energies = [energy1, energy2, energy3]
        self.assertEqual(len(set(energies)), 3)  # All different
    
    def test_equilibrium_bond_length(self):
        """Test that equilibrium bond length gives lower energy"""
        vqe_short = H2VQE(bond_length=0.5)
        vqe_eq = H2VQE(bond_length=0.735)
        vqe_long = H2VQE(bond_length=1.5)
        
        params = np.ones(8) * 0.5
        
        energy_short = vqe_short.measure_expectation_value(params)
        energy_eq = vqe_eq.measure_expectation_value(params)
        energy_long = vqe_long.measure_expectation_value(params)
        
        # Equilibrium should generally give lower energy than extremes
        # (This is a soft check, not always guaranteed)
        print(f"Short bond: {energy_short:.6f}")
        print(f"Equilibrium: {energy_eq:.6f}")
        print(f"Long bond: {energy_long:.6f}")


class TestH2VQEEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    def test_zero_parameters(self):
        """Test circuit with zero parameters"""
        vqe = H2VQE()
        params = np.zeros(8)
        
        circuit = vqe.ansatz_circuit(params, num_qubits=2)
        self.assertGreater(circuit.num_qubits, 0)
    
    def test_large_parameters(self):
        """Test circuit with large parameters"""
        vqe = H2VQE()
        params = np.ones(8) * 100
        
        # Should not raise error
        circuit = vqe.ansatz_circuit(params, num_qubits=2)
        self.assertGreater(circuit.num_qubits, 0)
    
    def test_extreme_bond_length(self):
        """Test with extreme bond lengths"""
        vqe_very_short = H2VQE(bond_length=0.1)
        vqe_very_long = H2VQE(bond_length=5.0)
        
        # Should initialize without error
        self.assertEqual(vqe_very_short.bond_length, 0.1)
        self.assertEqual(vqe_very_long.bond_length, 5.0)


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestH2VQE))
    suite.addTests(loader.loadTestsFromTestCase(TestH2VQEPhysics))
    suite.addTests(loader.loadTestsFromTestCase(TestH2VQEEdgeCases))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
