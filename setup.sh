#!/bin/bash
# Setup script for Rebonato-Denev Bayesian Networks
# ==================================================
# This script sets up the Python environment and dependencies

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Banner
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Rebonato-Denev Bayesian Networks Setup                   ║"
echo "║  Black Swan Event Modeling for Portfolio Management       ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
print_info "Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    print_error "Python not found! Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
print_success "Found Python $PYTHON_VERSION"

# Check if Python version is 3.8+
PYTHON_MAJOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info[0])')
PYTHON_MINOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info[1])')

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    print_error "Python 3.8 or higher is required. Found Python $PYTHON_VERSION"
    exit 1
fi

# Ask user for installation type
echo ""
print_info "Select installation type:"
echo "  1) Minimal (required packages only)"
echo "  2) Full (includes Jupyter, visualization tools)"
echo "  3) Development (full + dev tools)"
echo ""
read -p "Enter choice [1-3]: " INSTALL_TYPE

case $INSTALL_TYPE in
    1)
        REQUIREMENTS_FILE="requirements-minimal.txt"
        print_info "Installing minimal requirements..."
        ;;
    2)
        REQUIREMENTS_FILE="requirements.txt"
        print_info "Installing full requirements..."
        ;;
    3)
        REQUIREMENTS_FILE="requirements.txt"
        print_info "Installing full requirements with dev tools..."
        DEV_INSTALL=true
        ;;
    *)
        print_warning "Invalid choice. Using minimal installation."
        REQUIREMENTS_FILE="requirements-minimal.txt"
        ;;
esac

# Ask about virtual environment
echo ""
read -p "Create virtual environment? [y/N]: " CREATE_VENV

if [[ $CREATE_VENV =~ ^[Yy]$ ]]; then
    print_info "Creating virtual environment..."
    
    # Check if venv exists
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists."
        read -p "Remove and recreate? [y/N]: " RECREATE_VENV
        if [[ $RECREATE_VENV =~ ^[Yy]$ ]]; then
            rm -rf venv
            $PYTHON_CMD -m venv venv
            print_success "Virtual environment recreated"
        fi
    else
        $PYTHON_CMD -m venv venv
        print_success "Virtual environment created"
    fi
    
    # Activate virtual environment
    print_info "Activating virtual environment..."
    source venv/bin/activate
    print_success "Virtual environment activated"
    
    # Upgrade pip
    print_info "Upgrading pip..."
    $PIP_CMD install --upgrade pip > /dev/null 2>&1
    print_success "pip upgraded"
fi

# Install requirements
echo ""
print_info "Installing Python packages from $REQUIREMENTS_FILE..."

if [ -f "$REQUIREMENTS_FILE" ]; then
    $PIP_CMD install -r $REQUIREMENTS_FILE
    print_success "Python packages installed successfully"
else
    print_error "Requirements file not found: $REQUIREMENTS_FILE"
    exit 1
fi

# Install development tools if requested
if [ "$DEV_INSTALL" = true ]; then
    print_info "Installing development tools..."
    $PIP_CMD install pytest black flake8 mypy > /dev/null 2>&1
    print_success "Development tools installed"
fi

# Verify installation
echo ""
print_info "Verifying installation..."

VERIFICATION_FAILED=false

# Check numpy
if $PYTHON_CMD -c "import numpy" 2>/dev/null; then
    NUMPY_VERSION=$($PYTHON_CMD -c "import numpy; print(numpy.__version__)")
    print_success "NumPy $NUMPY_VERSION installed"
else
    print_error "NumPy installation failed"
    VERIFICATION_FAILED=true
fi

# Check networkx
if $PYTHON_CMD -c "import networkx" 2>/dev/null; then
    NX_VERSION=$($PYTHON_CMD -c "import networkx; print(networkx.__version__)")
    print_success "NetworkX $NX_VERSION installed"
else
    print_error "NetworkX installation failed"
    VERIFICATION_FAILED=true
fi

# Check matplotlib
if $PYTHON_CMD -c "import matplotlib" 2>/dev/null; then
    MPL_VERSION=$($PYTHON_CMD -c "import matplotlib; print(matplotlib.__version__)")
    print_success "Matplotlib $MPL_VERSION installed"
else
    print_error "Matplotlib installation failed"
    VERIFICATION_FAILED=true
fi

if [ "$VERIFICATION_FAILED" = true ]; then
    print_error "Installation verification failed. Please check error messages above."
    exit 1
fi

# Run quick test
echo ""
print_info "Running quick test..."

$PYTHON_CMD -c "
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Quick test
arr = np.array([1, 2, 3])
G = nx.Graph()
G.add_edge(1, 2)
print('✓ All imports successful')
" 2>/dev/null

if [ $? -eq 0 ]; then
    print_success "Quick test passed"
else
    print_error "Quick test failed"
    exit 1
fi

# Display summary
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  SETUP COMPLETE!                                           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
print_success "Environment is ready to use"
echo ""
echo "Next steps:"
echo ""
echo "1. Run the Eurozone model:"
echo "   ${GREEN}$PYTHON_CMD rebonato_denev_eurozone_crisis.py${NC}"
echo ""
echo "2. Run the Trump Tariffs 2025 model:"
echo "   ${GREEN}$PYTHON_CMD trump_tariffs_2025_blackswan.py${NC}"
echo ""
echo "3. Open the interactive tutorial:"
echo "   ${GREEN}jupyter notebook rebonato_denev_tutorial.ipynb${NC}"
echo ""

if [[ $CREATE_VENV =~ ^[Yy]$ ]]; then
    echo "Note: Virtual environment is activated. To deactivate, run:"
    echo "   ${YELLOW}deactivate${NC}"
    echo ""
fi

echo "Documentation:"
echo "  • Quick Start: ${BLUE}QUICK_START.md${NC}"
echo "  • Trump Tariffs Analysis: ${BLUE}TRUMP_TARIFFS_2025_ANALYSIS.md${NC}"
echo "  • Complete Index: ${BLUE}MASTER_INDEX.md${NC}"
echo ""

print_success "Happy modeling! 🎯"
echo ""
