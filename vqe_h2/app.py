"""
Streamlit UI for VQE H2 Simulation with Interactive Visualizations
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from vqe_h2 import H2VQE


st.set_page_config(
    page_title="VQE H₂ Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTitle {
        color: #1f77b4;
    }
    h2, h3 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("⚛️ Variational Quantum Eigensolver (VQE) for H₂ Molecule")
st.markdown("### Ground State Energy Simulation using Qiskit")
st.markdown("---")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Configuration")
    
    tab1, tab2, tab3 = st.tabs(["VQE Settings", "Display", "Info"])
    
    with tab1:
        st.subheader("VQE Parameters")
        bond_length = st.slider(
            "Bond Length (Å)",
            min_value=0.3,
            max_value=2.0,
            value=0.735,
            step=0.01,
            help="Equilibrium bond length ≈ 0.735 Å"
        )
        
        max_iterations = st.slider(
            "Max Iterations",
            min_value=10,
            max_value=200,
            value=50,
            step=10
        )
        
        run_simulation = st.button("🚀 Run VQE Optimization", use_container_width=True)
    
    with tab2:
        st.subheader("Visualization Options")
        show_energy_curve = st.checkbox("Show Energy Curve", value=True)
        show_convergence = st.checkbox("Show Convergence", value=True)
        show_3d_viz = st.checkbox("Show 3D Visualization", value=True)
        show_circuit = st.checkbox("Show Circuit Info", value=True)
    
    with tab3:
        st.subheader("About")
        st.info("""
        **VQE Algorithm** combines quantum computing with classical optimization to find 
        ground state energies of molecular systems.
        
        **Key Features:**
        - Hardware-efficient ansatz
        - COBYLA optimization
        - Real-time convergence tracking
        - Interactive visualizations
        
        **H₂ Molecule:**
        - 2-qubit simulation
        - Parity mapping
        - Dynamic Hamiltonian
        """)

# Initialize session state
if 'vqe' not in st.session_state:
    st.session_state.vqe = None
if 'optimization_done' not in st.session_state:
    st.session_state.optimization_done = False

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    if run_simulation:
        st.session_state.vqe = H2VQE(bond_length=bond_length)
        
        with st.spinner(f"🔬 Optimizing VQE for bond length {bond_length:.3f} Å..."):
            try:
                initial_params = np.random.uniform(0, 2*np.pi, 8)
                
                # Run optimization directly
                optimal_energy, optimal_params = st.session_state.vqe.optimize(
                    initial_params=initial_params,
                    maxiter=max_iterations
                )
                st.session_state.optimization_done = True
                
                st.success(f"✅ Optimization completed! Optimal Energy: **{optimal_energy:.6f} Hartree**")
                
            except Exception as e:
                st.error(f"❌ Error during optimization: {str(e)}")
                import traceback
                st.error(traceback.format_exc())

# Display results if optimization is done
if st.session_state.optimization_done and st.session_state.vqe:
    vqe = st.session_state.vqe
    
    # Results summary
    st.subheader("📊 Optimization Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Optimal Energy",
            f"{vqe.optimal_energy:.6f}",
            "Hartree"
        )
    
    with col2:
        st.metric(
            "Bond Length",
            f"{vqe.bond_length:.3f}",
            "Å"
        )
    
    with col3:
        st.metric(
            "Iterations",
            vqe.iteration_count
        )
    
    with col4:
        # Approximate comparison with experimental value
        exp_energy = -1.17  # Approximate ground state energy of H2
        error = abs(vqe.optimal_energy - exp_energy)
        st.metric(
            "Error from Theory",
            f"{error:.6f}",
            "Hartree"
        )
    
    st.markdown("---")
    
    # Convergence plot
    if show_convergence and vqe.history['energies']:
        st.subheader("📈 Convergence Behavior")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=vqe.history['iterations'],
            y=vqe.history['energies'],
            mode='lines+markers',
            name='Energy',
            line=dict(color='#1f77b4', width=2),
            marker=dict(size=5)
        ))
        
        fig.update_layout(
            title=dict(text="VQE Energy vs Iteration"),
            xaxis_title="Iteration",
            yaxis_title="Energy (Hartree)",
            hovermode='x unified',
            height=400,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Energy curve
    if show_energy_curve:
        st.subheader("🔍 Energy Curve (Bond Dissociation)")
        
        bond_lengths = np.linspace(0.3, 2.0, 15)
        
        with st.spinner("Calculating energy curve..."):
            temp_vqe = H2VQE()
            bond_lengths_calc, energies = temp_vqe.get_energy_curve(bond_lengths)
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=bond_lengths_calc,
            y=energies,
            mode='lines+markers',
            name='VQE Energy',
            line=dict(color='#ff7f0e', width=2),
            marker=dict(size=6)
        ))
        
        # Add equilibrium point
        fig2.add_vline(
            x=0.735,
            line_dash="dash",
            line_color="green",
            annotation_text="Equilibrium",
            annotation_position="top right"
        )
        
        fig2.update_layout(
            title=dict(text="H₂ Potential Energy Surface"),
            xaxis_title="Bond Length (Å)",
            yaxis_title="Energy (Hartree)",
            hovermode='x unified',
            height=400,
            template='plotly_white'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")

# 3D Visualizations
if show_3d_viz:
    st.subheader("🎯 3D Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Bloch Sphere Representation**")
        
        # Create interactive 3D Bloch sphere
        fig_bloch = go.Figure(data=[
            go.Surface(
                x=np.linspace(-1, 1, 50),
                y=np.linspace(-1, 1, 50),
                z=np.sqrt(np.maximum(1 - np.linspace(-1, 1, 50)[np.newaxis,:]**2 - 
                                     np.linspace(-1, 1, 50)[:,np.newaxis]**2, 0)),
                colorscale='Viridis',
                showscale=False,
                opacity=0.3
            )
        ])
        
        # Add some random state vectors
        n_states = 5
        for i in range(n_states):
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2*np.pi)
            x = np.sin(theta) * np.cos(phi)
            y = np.sin(theta) * np.sin(phi)
            z = np.cos(theta)
            
            fig_bloch.add_trace(go.Scatter3d(
                x=[0, x],
                y=[0, y],
                z=[0, z],
                mode='lines+markers',
                line=dict(color='red', width=3),
                marker=dict(size=5),
                showlegend=False
            ))
        
        fig_bloch.update_layout(
            title=dict(text="Bloch Sphere - Quantum States"),
            scene=dict(
                xaxis=dict(title='X'),
                yaxis=dict(title='Y'),
                zaxis=dict(title='Z'),
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.3))
            ),
            height=500,
            template='plotly_white'
        )
        
        st.plotly_chart(fig_bloch, use_container_width=True)
    
    with col2:
        st.write("**Molecular Geometry**")
        
        # H2 molecule visualization
        fig_mol = go.Figure()
        
        # Add electron cloud (probability density)
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        r = 1.0
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        
        fig_mol.add_trace(go.Surface(
            x=x - 0.5,
            y=y,
            z=z,
            colorscale='Blues',
            showscale=False,
            opacity=0.4,
            name='Electron Cloud'
        ))
        
        fig_mol.add_trace(go.Surface(
            x=x + 0.5,
            y=y,
            z=z,
            colorscale='Blues',
            showscale=False,
            opacity=0.4,
            name='Electron Cloud'
        ))
        
        # Add nuclei
        fig_mol.add_trace(go.Scatter3d(
            x=[-0.5, 0.5],
            y=[0, 0],
            z=[0, 0],
            mode='markers',
            marker=dict(size=15, color='red', symbol='circle'),
            name='Nuclei'
        ))
        
        fig_mol.update_layout(
            title=dict(text="H₂ Molecular Geometry"),
            scene=dict(
                xaxis=dict(title='X (Å)'),
                yaxis=dict(title='Y (Å)'),
                zaxis=dict(title='Z (Å)'),
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.3))
            ),
            height=500,
            template='plotly_white'
        )
        
        st.plotly_chart(fig_mol, use_container_width=True)

# Circuit information
if show_circuit:
    st.markdown("---")
    st.subheader("🔌 Quantum Circuit Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ansatz Circuit Structure:**")
        st.code("""
Hardware-Efficient Variational Form:

1. Initial Layer: Hadamard on all qubits
2. Variational Layer 1:
   - RZ(θ₀) and RX(θ₁) on q0
   - RZ(θ₂) and RX(θ₃) on q1
3. Entangling Layer:
   - CX(q0 → q1)
4. Variational Layer 2:
   - RZ(θ₄) and RX(θ₅) on q0
   - RZ(θ₆) and RX(θ₇) on q1

Total Parameters: 8
Depth: ~6 gates
        """, language="text")
    
    with col2:
        st.write("**Hamiltonian Terms:**")
        st.code("""
H₂ Hamiltonian (2-qubit):

H = h_II · I⊗I
  + h_ZZ · Z⊗Z
  + h_ZI · Z⊗I
  + h_IZ · I⊗Z

Where coefficients depend on:
- Bond length r
- Electronic structure

Measurement: Z⊗Z expectation value
        """, language="text")

# Footer with educational info
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("**About VQE**: Variational Quantum Eigensolver finds ground state energies by varying quantum circuit parameters to minimize energy expectation value.")

with col2:
    st.info("**H₂ Molecule**: Simplest neutral molecule. Ground state energy ≈ -1.17 Hartree at equilibrium bond length ≈ 0.735 Å.")

with col3:
    st.info("**Qiskit**: Quantum computing framework providing tools for quantum circuit design, simulation, and optimization.")

# Display technical details in expandable section
with st.expander("📚 Technical Details"):
    st.markdown("""
    ### How VQE Works:
    
    1. **Ansatz Design**: Creates a parameterized quantum circuit
    2. **Hamiltonian Mapping**: Maps molecular Hamiltonian to qubits
    3. **Energy Measurement**: Measures expectation value on quantum simulator
    4. **Classical Optimization**: Uses COBYLA to minimize energy
    5. **Iteration**: Repeats until convergence
    
    ### Key Equations:
    
    **Energy Expectation Value:**
    $E(\\theta) = \\langle \\psi(\\theta) | H | \\psi(\\theta) \\rangle$
    
    **Optimization:**
    $\\theta^* = \\arg\\min_\\theta E(\\theta)$
    
    **Error Metric:**
    $\\text{Error} = |E_{VQE} - E_{\\text{exact}}|$
    """)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>VQE H₂ Simulator | Powered by Qiskit & Streamlit | 2025</p>", unsafe_allow_html=True)
