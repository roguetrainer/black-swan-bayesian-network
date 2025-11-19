"""
Bayesian Network Implementation of Rebonato-Denev Eurozone Crisis Scenario
============================================================================

This implements a simplified version of the stress testing methodology from
"Portfolio Management under Stress" by Riccardo Rebonato and Alexander Denev.

The example models a "black swan" event: the potential breakup of the Eurozone,
and its causal impact on financial markets.

Key features of Rebonato-Denev methodology:
1. Causal modeling (not just correlations)
2. Forward-looking stress scenarios
3. Conditional probability tables for extreme events
4. Asset allocation under stress conditions
"""

import numpy as np
import networkx as nx
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from itertools import product


class BayesianNetwork:
    """
    Simple Bayesian Network implementation for stress testing.
    
    Based on Rebonato-Denev methodology for modeling causal relationships
    in financial markets during crisis scenarios.
    """
    
    def __init__(self):
        self.graph = nx.DiGraph()
        self.cpds = {}  # Conditional Probability Distributions
        self.states = {}  # Possible states for each variable
        
    def add_node(self, node: str, states: List[str]):
        """Add a node with its possible states."""
        self.graph.add_node(node)
        self.states[node] = states
        
    def add_edge(self, parent: str, child: str):
        """Add a causal edge from parent to child."""
        self.graph.add_edge(parent, child)
        
    def set_cpd(self, node: str, cpd: np.ndarray, parent_order: List[str] = None):
        """
        Set the conditional probability distribution for a node.
        
        Parameters:
        -----------
        node : str
            The node for which to set the CPD
        cpd : np.ndarray
            The conditional probability table
        parent_order : List[str]
            Order of parents (important for indexing CPD correctly)
        """
        self.cpds[node] = {
            'table': cpd,
            'parents': parent_order if parent_order else []
        }
        
    def get_probability(self, evidence: Dict[str, str]) -> Dict[str, float]:
        """
        Calculate probabilities given evidence using inference.
        
        This is a simplified exact inference for the small network.
        """
        # For this demo, we'll use enumeration
        return self._variable_elimination(evidence)
    
    def _variable_elimination(self, evidence: Dict[str, str]) -> Dict[str, Dict[str, float]]:
        """Simple variable elimination for inference."""
        results = {}
        
        # Get all nodes not in evidence
        hidden_nodes = [n for n in self.graph.nodes() if n not in evidence]
        
        # For each hidden variable, marginalize over all other hidden variables
        for query_node in hidden_nodes:
            probs = {}
            
            for query_state in self.states[query_node]:
                total_prob = 0.0
                
                # Generate all possible assignments for other hidden nodes
                other_hidden = [n for n in hidden_nodes if n != query_node]
                
                if not other_hidden:
                    # Only this node is hidden
                    assignment = {**evidence, query_node: query_state}
                    total_prob = self._calculate_joint_probability(assignment)
                else:
                    # Enumerate over all combinations of other hidden variables
                    other_states = [self.states[n] for n in other_hidden]
                    
                    for state_combo in product(*other_states):
                        assignment = {**evidence, query_node: query_state}
                        for i, node in enumerate(other_hidden):
                            assignment[node] = state_combo[i]
                        
                        total_prob += self._calculate_joint_probability(assignment)
                
                probs[query_state] = total_prob
            
            # Normalize
            total = sum(probs.values())
            if total > 0:
                probs = {k: v/total for k, v in probs.items()}
            results[query_node] = probs
            
        return results
    
    def _calculate_joint_probability(self, assignment: Dict[str, str]) -> float:
        """Calculate joint probability of a complete assignment."""
        prob = 1.0
        
        for node in nx.topological_sort(self.graph):
            if node not in assignment:
                return 0.0
                
            parents = list(self.graph.predecessors(node))
            
            if not parents:
                # Root node - use prior
                cpd = self.cpds[node]['table']
                node_state_idx = self.states[node].index(assignment[node])
                prob *= cpd[node_state_idx]
            else:
                # Get parent states
                parent_states = tuple(assignment[p] for p in self.cpds[node]['parents'])
                
                # Find index in CPD
                cpd = self.cpds[node]['table']
                node_state_idx = self.states[node].index(assignment[node])
                
                # Calculate parent combination index
                parent_indices = []
                for i, parent in enumerate(self.cpds[node]['parents']):
                    parent_state_idx = self.states[parent].index(assignment[parent])
                    parent_indices.append(parent_state_idx)
                
                # Index into CPD (node_state, parent1_state, parent2_state, ...)
                indices = [node_state_idx] + parent_indices
                prob *= cpd[tuple(indices)]
                
        return prob
    
    def sample(self, evidence: Dict[str, str] = None, n_samples: int = 1000) -> Dict[str, np.ndarray]:
        """
        Forward sampling from the network.
        """
        samples = {node: [] for node in self.graph.nodes()}
        
        for _ in range(n_samples):
            assignment = evidence.copy() if evidence else {}
            
            for node in nx.topological_sort(self.graph):
                if node in assignment:
                    samples[node].append(assignment[node])
                    continue
                    
                parents = list(self.graph.predecessors(node))
                
                if not parents:
                    # Sample from prior
                    probs = self.cpds[node]['table']
                    state = np.random.choice(self.states[node], p=probs)
                else:
                    # Sample conditional on parents
                    parent_states = [assignment[p] for p in self.cpds[node]['parents']]
                    parent_indices = [self.states[p].index(parent_states[i]) 
                                    for i, p in enumerate(self.cpds[node]['parents'])]
                    
                    # Get conditional distribution
                    cpd = self.cpds[node]['table']
                    
                    # Build the index tuple
                    index = [slice(None)] + parent_indices  # slice(None) for the node dimension
                    cond_probs = cpd[tuple(index)]
                    
                    # Ensure it's 1D and normalized
                    cond_probs = np.array(cond_probs).flatten()
                    if cond_probs.sum() > 0:
                        cond_probs = cond_probs / cond_probs.sum()
                    else:
                        # Uniform distribution as fallback
                        cond_probs = np.ones(len(self.states[node])) / len(self.states[node])
                    
                    state = np.random.choice(self.states[node], p=cond_probs)
                
                assignment[node] = state
                samples[node].append(state)
                
        return samples
    
    def visualize(self, filename: str = None):
        """Visualize the Bayesian network structure."""
        plt.figure(figsize=(12, 8))
        
        # Use hierarchical layout
        pos = nx.spring_layout(self.graph, k=2, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', 
                              node_size=3000, alpha=0.9)
        
        # Draw edges with arrows
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', 
                              arrows=True, arrowsize=20, width=2,
                              arrowstyle='->', connectionstyle='arc3,rad=0.1')
        
        # Draw labels
        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_weight='bold')
        
        plt.title("Bayesian Network: Eurozone Crisis Scenario\n(Rebonato-Denev Methodology)", 
                 fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        
        if filename:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()


def build_eurozone_crisis_network() -> BayesianNetwork:
    """
    Build a Bayesian network for Eurozone crisis scenario.
    
    This is inspired by Rebonato-Denev's approach to modeling
    the Euro breakup as a "black swan" event with causal structure.
    
    Network Structure:
    ------------------
    Political_Instability → Eurozone_Breakup
    Economic_Weakness → Eurozone_Breakup
    Eurozone_Breakup → Credit_Spreads
    Eurozone_Breakup → Flight_to_Quality
    Credit_Spreads → Corporate_Bonds
    Flight_to_Quality → Government_Bonds
    Credit_Spreads → Equities
    Flight_to_Quality → Equities
    
    States:
    -------
    - Binary (Low/High) for most variables
    - This captures extreme vs. normal scenarios
    """
    
    bn = BayesianNetwork()
    
    # Define nodes and their states
    nodes = {
        'Political_Instability': ['Low', 'High'],
        'Economic_Weakness': ['Low', 'High'],
        'Eurozone_Breakup': ['No', 'Yes'],
        'Credit_Spreads': ['Normal', 'Widening'],
        'Flight_to_Quality': ['No', 'Yes'],
        'Corporate_Bonds': ['Stable', 'Falling'],
        'Government_Bonds': ['Stable', 'Rally'],
        'Equities': ['Stable', 'Falling']
    }
    
    for node, states in nodes.items():
        bn.add_node(node, states)
    
    # Define causal structure
    edges = [
        ('Political_Instability', 'Eurozone_Breakup'),
        ('Economic_Weakness', 'Eurozone_Breakup'),
        ('Eurozone_Breakup', 'Credit_Spreads'),
        ('Eurozone_Breakup', 'Flight_to_Quality'),
        ('Credit_Spreads', 'Corporate_Bonds'),
        ('Flight_to_Quality', 'Government_Bonds'),
        ('Credit_Spreads', 'Equities'),
        ('Flight_to_Quality', 'Equities')
    ]
    
    for parent, child in edges:
        bn.add_edge(parent, child)
    
    # Set Conditional Probability Distributions
    # These are subjective probabilities reflecting expert judgment (Rebonato-Denev approach)
    
    # Root nodes - prior probabilities
    # P(Political_Instability)
    bn.set_cpd('Political_Instability', np.array([0.7, 0.3]))  # [Low, High]
    
    # P(Economic_Weakness)
    bn.set_cpd('Economic_Weakness', np.array([0.6, 0.4]))  # [Low, High]
    
    # P(Eurozone_Breakup | Political_Instability, Economic_Weakness)
    # Shape: (2, 2, 2) - [Breakup_state, Political_state, Economic_state]
    eurozone_cpd = np.array([
        # Economic_Weakness = Low
        [[0.95, 0.70],   # Political = Low, High | Breakup = No
         [0.05, 0.30]],  # Political = Low, High | Breakup = Yes
        # Economic_Weakness = High
        [[0.80, 0.30],   # Political = Low, High | Breakup = No
         [0.20, 0.70]]   # Political = Low, High | Breakup = Yes
    ])
    
    # Reshape to proper format: [node_state, parent1_state, parent2_state]
    eurozone_cpd_formatted = np.zeros((2, 2, 2))
    for pol in range(2):
        for econ in range(2):
            eurozone_cpd_formatted[0, pol, econ] = eurozone_cpd[econ][0][pol]  # No
            eurozone_cpd_formatted[1, pol, econ] = eurozone_cpd[econ][1][pol]  # Yes
    
    bn.set_cpd('Eurozone_Breakup', eurozone_cpd_formatted, 
              ['Political_Instability', 'Economic_Weakness'])
    
    # P(Credit_Spreads | Eurozone_Breakup)
    credit_cpd = np.array([
        [0.80, 0.10],  # [Normal, Widening] | Breakup = No
        [0.20, 0.90]   # [Normal, Widening] | Breakup = Yes
    ])
    bn.set_cpd('Credit_Spreads', credit_cpd.T, ['Eurozone_Breakup'])
    
    # P(Flight_to_Quality | Eurozone_Breakup)
    flight_cpd = np.array([
        [0.85, 0.10],  # [No, Yes] | Breakup = No
        [0.15, 0.90]   # [No, Yes] | Breakup = Yes
    ])
    bn.set_cpd('Flight_to_Quality', flight_cpd.T, ['Eurozone_Breakup'])
    
    # P(Corporate_Bonds | Credit_Spreads)
    corp_bonds_cpd = np.array([
        [0.90, 0.20],  # [Stable, Falling] | Spreads = Normal
        [0.10, 0.80]   # [Stable, Falling] | Spreads = Widening
    ])
    bn.set_cpd('Corporate_Bonds', corp_bonds_cpd.T, ['Credit_Spreads'])
    
    # P(Government_Bonds | Flight_to_Quality)
    gov_bonds_cpd = np.array([
        [0.80, 0.10],  # [Stable, Rally] | Flight = No
        [0.20, 0.90]   # [Stable, Rally] | Flight = Yes
    ])
    bn.set_cpd('Government_Bonds', gov_bonds_cpd.T, ['Flight_to_Quality'])
    
    # P(Equities | Credit_Spreads, Flight_to_Quality)
    # More complex - equities affected by both spreads and flight to quality
    equities_cpd = np.zeros((2, 2, 2))
    
    # Credit_Spreads = Normal, Flight_to_Quality = No
    equities_cpd[0, 0, 0] = 0.90  # Stable
    equities_cpd[1, 0, 0] = 0.10  # Falling
    
    # Credit_Spreads = Normal, Flight_to_Quality = Yes
    equities_cpd[0, 0, 1] = 0.60  # Stable
    equities_cpd[1, 0, 1] = 0.40  # Falling
    
    # Credit_Spreads = Widening, Flight_to_Quality = No
    equities_cpd[0, 1, 0] = 0.40  # Stable
    equities_cpd[1, 1, 0] = 0.60  # Falling
    
    # Credit_Spreads = Widening, Flight_to_Quality = Yes
    equities_cpd[0, 1, 1] = 0.10  # Stable
    equities_cpd[1, 1, 1] = 0.90  # Falling
    
    bn.set_cpd('Equities', equities_cpd, ['Credit_Spreads', 'Flight_to_Quality'])
    
    return bn


def analyze_stress_scenarios(bn: BayesianNetwork):
    """
    Analyze different stress scenarios using the Bayesian network.
    
    This demonstrates the Rebonato-Denev approach to stress testing:
    1. Define extreme scenarios
    2. Propagate them through causal network
    3. Assess impact on asset classes
    """
    
    print("=" * 80)
    print("STRESS SCENARIO ANALYSIS: Eurozone Crisis")
    print("Based on Rebonato-Denev Bayesian Network Methodology")
    print("=" * 80)
    print()
    
    # Scenario 1: Normal Times (Base Case)
    print("SCENARIO 1: Normal Times (Base Case)")
    print("-" * 80)
    evidence1 = {
        'Political_Instability': 'Low',
        'Economic_Weakness': 'Low'
    }
    
    results1 = bn.get_probability(evidence1)
    print(f"Evidence: {evidence1}")
    print("\nPosterior Probabilities:")
    for var, probs in results1.items():
        print(f"  {var}:")
        for state, prob in probs.items():
            print(f"    {state}: {prob:.2%}")
    print()
    
    # Scenario 2: Black Swan - High Political Instability + Economic Weakness
    print("\nSCENARIO 2: Black Swan - Political Crisis + Economic Weakness")
    print("-" * 80)
    evidence2 = {
        'Political_Instability': 'High',
        'Economic_Weakness': 'High'
    }
    
    results2 = bn.get_probability(evidence2)
    print(f"Evidence: {evidence2}")
    print("\nPosterior Probabilities:")
    for var, probs in results2.items():
        print(f"  {var}:")
        for state, prob in probs.items():
            print(f"    {state}: {prob:.2%}")
    print()
    
    # Scenario 3: Eurozone Breakup (Given)
    print("\nSCENARIO 3: Eurozone Breakup Occurs (Stress Test)")
    print("-" * 80)
    evidence3 = {
        'Eurozone_Breakup': 'Yes'
    }
    
    results3 = bn.get_probability(evidence3)
    print(f"Evidence: {evidence3}")
    print("\nPosterior Probabilities:")
    for var, probs in results3.items():
        print(f"  {var}:")
        for state, prob in probs.items():
            print(f"    {state}: {prob:.2%}")
    print()
    
    # Scenario 4: Credit Spreads Widening + Flight to Quality
    print("\nSCENARIO 4: Market Stress (Widening Spreads + Flight to Quality)")
    print("-" * 80)
    evidence4 = {
        'Credit_Spreads': 'Widening',
        'Flight_to_Quality': 'Yes'
    }
    
    results4 = bn.get_probability(evidence4)
    print(f"Evidence: {evidence4}")
    print("\nPosterior Probabilities:")
    for var, probs in results4.items():
        print(f"  {var}:")
        for state, prob in probs.items():
            print(f"    {state}: {prob:.2%}")
    print()
    
    return results1, results2, results3, results4


def portfolio_implications(scenario_results: Dict):
    """
    Analyze portfolio implications based on scenario analysis.
    
    This follows Rebonato-Denev's approach to translating
    stress scenarios into portfolio adjustments.
    """
    
    print("=" * 80)
    print("PORTFOLIO ALLOCATION IMPLICATIONS")
    print("=" * 80)
    print()
    
    print("Asset Class Attractiveness Under Different Scenarios:")
    print("-" * 80)
    print()
    
    assets = ['Corporate_Bonds', 'Government_Bonds', 'Equities']
    scenarios = ['Normal', 'Political Crisis', 'Eurozone Breakup', 'Market Stress']
    
    # Extract probability of adverse outcomes
    print(f"{'Scenario':<25} {'Corp Bonds':<15} {'Gov Bonds':<15} {'Equities':<15}")
    print(f"{'':25} {'Falling':<15} {'Rally':<15} {'Falling':<15}")
    print("-" * 80)
    
    for i, scenario_name in enumerate(scenarios):
        results = scenario_results[i]
        
        corp_prob = results.get('Corporate_Bonds', {}).get('Falling', 0)
        gov_prob = results.get('Government_Bonds', {}).get('Rally', 0)
        equity_prob = results.get('Equities', {}).get('Falling', 0)
        
        print(f"{scenario_name:<25} {corp_prob:>6.1%}{'':9} {gov_prob:>6.1%}{'':9} {equity_prob:>6.1%}")
    
    print()
    print("Key Insights:")
    print("-" * 80)
    print("1. Normal Times: All asset classes relatively stable")
    print("2. Political Crisis: Increased risk across the board, especially equities")
    print("3. Eurozone Breakup: Severe stress - gov bonds benefit, corp bonds/equities suffer")
    print("4. Market Stress: Flight to quality benefits government bonds")
    print()
    print("Portfolio Recommendations (Rebonato-Denev Approach):")
    print("-" * 80)
    print("• Overweight government bonds in high-stress scenarios")
    print("• Reduce corporate bond and equity exposure when breakup risk elevated")
    print("• Use scenario probabilities to adjust portfolio weights dynamically")
    print("• Consider ambiguity aversion - scenarios may have uncertain probabilities")
    print()


def monte_carlo_simulation(bn: BayesianNetwork, evidence: Dict = None, n_sims: int = 10000):
    """
    Perform Monte Carlo simulation for portfolio stress testing.
    
    This demonstrates how to use the Bayesian network for
    large-scale portfolio simulations.
    """
    
    print("=" * 80)
    print("MONTE CARLO SIMULATION")
    print(f"Number of simulations: {n_sims:,}")
    print("=" * 80)
    print()
    
    samples = bn.sample(evidence=evidence, n_samples=n_sims)
    
    print("Simulation Results:")
    print("-" * 80)
    
    for node in bn.graph.nodes():
        if evidence and node in evidence:
            continue
        print(f"\n{node}:")
        states = bn.states[node]
        for state in states:
            count = samples[node].count(state)
            prob = count / n_sims
            print(f"  {state}: {prob:.2%} ({count:,} occurrences)")
    
    # Calculate conditional statistics
    print("\n" + "=" * 80)
    print("CONDITIONAL STATISTICS")
    print("=" * 80)
    
    # Find scenarios where Eurozone breaks up
    breakup_indices = [i for i, v in enumerate(samples['Eurozone_Breakup']) if v == 'Yes']
    n_breakup = len(breakup_indices)
    
    if n_breakup > 0:
        print(f"\nIn scenarios with Eurozone Breakup ({n_breakup:,} cases, {n_breakup/n_sims:.1%}):")
        print("-" * 80)
        
        for asset in ['Corporate_Bonds', 'Government_Bonds', 'Equities']:
            falling_count = sum(1 for i in breakup_indices 
                              if samples[asset][i] in ['Falling', 'Rally'])
            state_name = 'Rally' if asset == 'Government_Bonds' else 'Falling'
            print(f"  {asset} {state_name}: {falling_count/n_breakup:.1%}")
    
    return samples


def main():
    """Main execution function."""
    
    # Build the network
    print("Building Eurozone Crisis Bayesian Network...")
    print("Based on Rebonato-Denev 'Portfolio Management under Stress'")
    print()
    
    bn = build_eurozone_crisis_network()
    
    # Visualize the network
    print("Generating network visualization...")
    bn.visualize('/mnt/user-data/outputs/eurozone_crisis_network.png')
    print("✓ Network structure saved")
    print()
    
    # Analyze scenarios
    results = analyze_stress_scenarios(bn)
    
    # Portfolio implications
    portfolio_implications(results)
    
    # Monte Carlo simulation
    print("\n" + "=" * 80)
    print("BLACK SWAN SCENARIO: High Political Instability + Economic Weakness")
    print("=" * 80)
    monte_carlo_simulation(bn, 
                          evidence={'Political_Instability': 'High', 
                                  'Economic_Weakness': 'High'},
                          n_sims=10000)
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    print("Key Takeaways from Rebonato-Denev Methodology:")
    print("-" * 80)
    print("1. Causal structure captures how crises propagate through markets")
    print("2. Forward-looking scenarios complement historical data")
    print("3. Expert judgment encoded in conditional probabilities")
    print("4. Portfolio decisions based on scenario analysis, not just correlations")
    print("5. Black swan events can be systematically incorporated into risk management")
    print()


if __name__ == "__main__":
    main()
