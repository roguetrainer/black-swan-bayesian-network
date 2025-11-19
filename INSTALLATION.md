# Installation Guide

## Quick Setup (Recommended)

### Linux / macOS
```bash
# Navigate to the project directory
cd rebonato-denev-bayesian-networks

# Run the setup script
./setup.sh

# Follow the prompts
```

### Windows
```batch
# Navigate to the project directory
cd rebonato-denev-bayesian-networks

# Run the setup script
setup.bat

# Follow the prompts
```

---

## Manual Installation

### Prerequisites

- **Python 3.8 or higher** (3.9+ recommended)
- **pip** (Python package installer)
- **Virtual environment** (recommended)

### Step 1: Create Virtual Environment (Recommended)

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```batch
python -m venv venv
venv\Scripts\activate.bat
```

### Step 2: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 3: Install Requirements

Choose one of the following based on your needs:

#### Option A: Minimal Installation (Required packages only)
```bash
pip install -r requirements-minimal.txt
```

**Installs**:
- numpy (numerical computations)
- networkx (graph structures)
- matplotlib (visualization)

#### Option B: Full Installation (Recommended)
```bash
pip install -r requirements.txt
```

**Installs everything in minimal plus**:
- jupyter (interactive notebooks)
- pandas (data analysis)
- seaborn (advanced visualization)

#### Option C: Install Individual Packages
```bash
# Core requirements
pip install numpy>=1.20.0 networkx>=2.5.0 matplotlib>=3.3.0

# Optional: For Jupyter notebooks
pip install jupyter notebook ipython

# Optional: For data analysis
pip install pandas seaborn
```

### Step 4: Verify Installation

```python
# Run this Python code to verify
python -c "
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
print('✓ All core packages installed successfully!')
print(f'NumPy version: {np.__version__}')
print(f'NetworkX version: {nx.__version__}')
print(f'Matplotlib version: {plt.matplotlib.__version__}')
"
```

---

## Testing the Installation

### Quick Test

```bash
# Run the Eurozone model (should take ~10 seconds)
python rebonato_denev_eurozone_crisis.py
```

If you see output with scenario analysis and Monte Carlo results, the installation is successful!

### Interactive Test

```bash
# Launch Jupyter notebook
jupyter notebook rebonato_denev_tutorial.ipynb
```

Run the first few cells to verify everything works.

---

## Platform-Specific Instructions

### macOS

#### Using Homebrew (Recommended)
```bash
# Install Python if not already installed
brew install python@3.11

# Install the project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Potential Issues
- **"command not found: python3"**: Install Python via Homebrew
- **"No module named '_tkinter'"**: Install with `brew install python-tk@3.11`

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Install system dependencies for matplotlib
sudo apt install python3-tk

# Install the project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

#### Using Python from python.org (Recommended)
1. Download Python 3.11+ from https://www.python.org/downloads/
2. **Important**: Check "Add Python to PATH" during installation
3. Open Command Prompt or PowerShell
4. Run `setup.bat`

#### Potential Issues
- **"python is not recognized"**: Python not in PATH - reinstall and check the PATH option
- **"Microsoft Visual C++ is required"**: Install Microsoft C++ Build Tools

---

## Docker Installation (Alternative)

If you prefer containerized deployment:

```dockerfile
# Create a file named Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "rebonato_denev_eurozone_crisis.py"]
```

Build and run:
```bash
docker build -t rebonato-denev .
docker run rebonato-denev
```

---

## Conda Installation (Alternative)

If you use Anaconda/Miniconda:

```bash
# Create conda environment
conda create -n rebonato-denev python=3.11

# Activate environment
conda activate rebonato-denev

# Install packages
conda install numpy networkx matplotlib jupyter pandas seaborn

# Or use pip within conda
pip install -r requirements.txt
```

---

## Troubleshooting

### Common Issues

#### 1. "No module named 'numpy'"
**Solution**: Package not installed
```bash
pip install numpy
```

#### 2. "ImportError: cannot import name '_imaging' from 'PIL'"
**Solution**: Pillow issue with matplotlib
```bash
pip uninstall pillow
pip install pillow
```

#### 3. "RuntimeError: Python is not installed as a framework"
**Solution**: macOS matplotlib backend issue
```bash
# Create/edit ~/.matplotlib/matplotlibrc
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

#### 4. Virtual environment not activating
**Linux/macOS**:
```bash
source venv/bin/activate
```

**Windows (Command Prompt)**:
```batch
venv\Scripts\activate.bat
```

**Windows (PowerShell)**:
```powershell
venv\Scripts\Activate.ps1
# If blocked, run: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 5. "Permission denied" when running setup.sh
**Solution**: Make script executable
```bash
chmod +x setup.sh
```

#### 6. Matplotlib not displaying plots
**Solution**: 
- **Linux**: Install `python3-tk`
- **macOS**: Install via `brew install python-tk`
- **Windows**: Usually works by default

### Getting Help

If you encounter issues:

1. **Check Python version**: `python --version` (must be 3.8+)
2. **Check pip version**: `pip --version`
3. **Update pip**: `pip install --upgrade pip`
4. **Try minimal installation first**: `pip install -r requirements-minimal.txt`
5. **Check system dependencies**: Some packages need C compilers

---

## Upgrading

To upgrade to the latest versions:

```bash
# Upgrade all packages
pip install --upgrade -r requirements.txt

# Or upgrade individual packages
pip install --upgrade numpy networkx matplotlib
```

---

## Uninstallation

### Remove Virtual Environment
```bash
# Deactivate if active
deactivate

# Remove directory
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows
```

### Remove Packages
```bash
pip uninstall -r requirements.txt -y
```

---

## Performance Optimization

### For Large-Scale Analysis

If running large Monte Carlo simulations (>100,000 samples):

```bash
# Install optional performance packages
pip install numba  # JIT compilation for NumPy
pip install joblib  # Parallel processing
```

---

## Next Steps

After successful installation:

1. **Quick Start**: Read `QUICK_START.md`
2. **Run Demo**: Execute `python rebonato_denev_eurozone_crisis.py`
3. **Explore Tutorial**: Open `rebonato_denev_tutorial.ipynb`
4. **Review Analysis**: Read `TRUMP_TARIFFS_2025_ANALYSIS.md`

---

## System Requirements

### Minimum
- **CPU**: Any modern processor
- **RAM**: 2 GB
- **Disk**: 500 MB
- **OS**: Windows 10+, macOS 10.14+, Linux (any recent distro)

### Recommended
- **CPU**: 4+ cores
- **RAM**: 8 GB
- **Disk**: 1 GB
- **OS**: Latest stable version

### For Development
- **RAM**: 16 GB (for large-scale simulations)
- **CPU**: 8+ cores (for parallel processing)

---

## Security Notes

- Install from official PyPI sources only
- Keep Python and packages updated
- Use virtual environments to isolate dependencies
- Review `requirements.txt` before installation

---

## License Considerations

This implementation is for educational purposes. Dependencies have their own licenses:
- **NumPy**: BSD License
- **NetworkX**: BSD License
- **Matplotlib**: PSF-based License
- **Jupyter**: BSD License

All are permissive open-source licenses.

---

**Installation Status**: ✅ Ready for Python 3.8+  
**Last Updated**: November 2025  
**Tested Platforms**: Ubuntu 24.04, macOS 14, Windows 11
