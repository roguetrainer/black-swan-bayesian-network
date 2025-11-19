#!/usr/bin/env python3
"""
Installation Verification Test
==============================
Quick test to verify all dependencies are properly installed.
"""

import sys
import importlib
from typing import List, Tuple

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'


def print_banner():
    """Print test banner."""
    print("\n" + "=" * 70)
    print(f"{BOLD}Rebonato-Denev Bayesian Networks - Installation Test{RESET}")
    print("=" * 70 + "\n")


def check_python_version() -> Tuple[bool, str]:
    """Check Python version."""
    major, minor = sys.version_info[:2]
    version_str = f"{major}.{minor}.{sys.version_info.micro}"
    
    if major >= 3 and minor >= 8:
        return True, f"Python {version_str}"
    else:
        return False, f"Python {version_str} (3.8+ required)"


def check_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
    """Check if a package is installed and get version."""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        
        # Try to get version
        version = "unknown"
        for attr in ['__version__', 'VERSION', 'version']:
            if hasattr(module, attr):
                version = getattr(module, attr)
                if callable(version):
                    version = version()
                break
        
        return True, f"{package_name} {version}"
    except ImportError:
        return False, f"{package_name} (not installed)"


def run_functionality_test() -> Tuple[bool, str]:
    """Run a quick functionality test."""
    try:
        import numpy as np
        import networkx as nx
        import matplotlib.pyplot as plt
        
        # Test NumPy
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.mean() == 3.0, "NumPy calculation failed"
        
        # Test NetworkX
        G = nx.DiGraph()
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        assert nx.has_path(G, 1, 3), "NetworkX path finding failed"
        
        # Test Matplotlib (backend check)
        fig, ax = plt.subplots(figsize=(1, 1))
        plt.close(fig)
        
        return True, "All functionality tests passed"
    except Exception as e:
        return False, f"Functionality test failed: {str(e)}"


def main():
    """Run all tests."""
    print_banner()
    
    # Track results
    all_passed = True
    required_failed = []
    optional_failed = []
    
    # Check Python version
    print(f"{BLUE}Checking Python version...{RESET}")
    passed, message = check_python_version()
    if passed:
        print(f"  {GREEN}✓{RESET} {message}")
    else:
        print(f"  {RED}✗{RESET} {message}")
        all_passed = False
        required_failed.append("Python 3.8+")
    print()
    
    # Check required packages
    print(f"{BLUE}Checking required packages...{RESET}")
    required_packages = [
        ('numpy', 'numpy'),
        ('networkx', 'networkx'),
        ('matplotlib', 'matplotlib'),
    ]
    
    for package_name, import_name in required_packages:
        passed, message = check_package(package_name, import_name)
        if passed:
            print(f"  {GREEN}✓{RESET} {message}")
        else:
            print(f"  {RED}✗{RESET} {message}")
            all_passed = False
            required_failed.append(package_name)
    print()
    
    # Check optional packages
    print(f"{BLUE}Checking optional packages...{RESET}")
    optional_packages = [
        ('jupyter', 'jupyter'),
        ('pandas', 'pandas'),
        ('seaborn', 'seaborn'),
    ]
    
    for package_name, import_name in optional_packages:
        passed, message = check_package(package_name, import_name)
        if passed:
            print(f"  {GREEN}✓{RESET} {message}")
        else:
            print(f"  {YELLOW}○{RESET} {message} (optional)")
            optional_failed.append(package_name)
    print()
    
    # Run functionality test
    if not required_failed:
        print(f"{BLUE}Running functionality tests...{RESET}")
        passed, message = run_functionality_test()
        if passed:
            print(f"  {GREEN}✓{RESET} {message}")
        else:
            print(f"  {RED}✗{RESET} {message}")
            all_passed = False
        print()
    
    # Print summary
    print("=" * 70)
    if all_passed and not required_failed:
        print(f"{GREEN}{BOLD}✓ ALL TESTS PASSED{RESET}")
        print()
        print("Your environment is ready to run the Bayesian network models!")
        print()
        print("Next steps:")
        print(f"  1. Run Eurozone model: {BLUE}python rebonato_denev_eurozone_crisis.py{RESET}")
        print(f"  2. Run Trump Tariffs model: {BLUE}python trump_tariffs_2025_blackswan.py{RESET}")
        print(f"  3. Open tutorial: {BLUE}jupyter notebook rebonato_denev_tutorial.ipynb{RESET}")
    else:
        print(f"{RED}{BOLD}✗ INSTALLATION INCOMPLETE{RESET}")
        print()
        if required_failed:
            print(f"{RED}Required packages missing:{RESET}")
            for package in required_failed:
                print(f"  • {package}")
            print()
            print("Install required packages:")
            print(f"  {BLUE}pip install -r requirements-minimal.txt{RESET}")
        
        if optional_failed:
            print()
            print(f"{YELLOW}Optional packages missing:{RESET}")
            for package in optional_failed:
                print(f"  • {package}")
            print()
            print("Install optional packages:")
            print(f"  {BLUE}pip install -r requirements.txt{RESET}")
    
    print("=" * 70)
    print()
    
    # Return exit code
    return 0 if all_passed and not required_failed else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
