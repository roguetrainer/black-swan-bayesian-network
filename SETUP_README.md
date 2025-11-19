# Setup & Installation Files

This directory contains everything you need to get the Rebonato-Denev Bayesian Networks up and running.

---

## Quick Start

### Linux / macOS
```bash
./setup.sh
```

### Windows
```batch
setup.bat
```

That's it! The scripts will guide you through the installation.

---

## Files Overview

### 📋 Requirements Files

| File | Purpose | Use Case |
|------|---------|----------|
| **requirements.txt** | Full installation | Recommended for most users |
| **requirements-minimal.txt** | Core packages only | Minimal working environment |

### 🚀 Setup Scripts

| File | Platform | Description |
|------|----------|-------------|
| **setup.sh** | Linux/macOS | Interactive setup with virtual environment |
| **setup.bat** | Windows | Interactive setup for Windows systems |

### 🧪 Testing & Verification

| File | Purpose |
|------|---------|
| **test_installation.py** | Verify installation is working correctly |

### 📖 Documentation

| File | Content |
|------|---------|
| **INSTALLATION.md** | Comprehensive installation guide with troubleshooting |

---

## Installation Options

### Option 1: Automated Setup (Recommended)

**Linux/macOS**:
```bash
./setup.sh
```

**Windows**:
```batch
setup.bat
```

The script will:
- ✓ Check Python version (3.8+ required)
- ✓ Offer to create virtual environment
- ✓ Install dependencies
- ✓ Verify installation
- ✓ Run quick test

### Option 2: Manual Installation

1. **Create virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. **Install minimal requirements**:
   ```bash
   pip install -r requirements-minimal.txt
   ```

3. **OR install full requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**:
   ```bash
   python test_installation.py
   ```

### Option 3: Individual Package Installation

```bash
# Core requirements only
pip install numpy>=1.20.0 networkx>=2.5.0 matplotlib>=3.3.0

# Add Jupyter for interactive notebooks
pip install jupyter notebook

# Add data analysis tools
pip install pandas seaborn
```

---

## What Gets Installed?

### Minimal Installation (`requirements-minimal.txt`)

- **NumPy** (1.20.0+): Numerical computations and array operations
- **NetworkX** (2.5.0+): Graph structures for Bayesian networks
- **Matplotlib** (3.3.0+): Visualization and plotting

**Size**: ~50 MB  
**Time**: 1-2 minutes

### Full Installation (`requirements.txt`)

Everything in minimal, plus:

- **Jupyter** (1.0.0+): Interactive notebooks
- **IPython** (7.0.0+): Enhanced Python shell
- **Pandas** (1.3.0+): Data analysis and manipulation
- **Seaborn** (0.11.0+): Statistical visualization

**Size**: ~200 MB  
**Time**: 3-5 minutes

---

## Verifying Your Installation

### Method 1: Run Test Script
```bash
python test_installation.py
```

This will check:
- ✓ Python version (3.8+)
- ✓ Required packages
- ✓ Optional packages
- ✓ Basic functionality

### Method 2: Quick Manual Test
```bash
python -c "import numpy, networkx, matplotlib; print('✓ Installation successful!')"
```

### Method 3: Run a Model
```bash
python rebonato_denev_eurozone_crisis.py
```

If you see scenario analysis output, everything works!

---

## System Requirements

### Minimum
- **Python**: 3.8 or higher
- **Disk Space**: 500 MB
- **RAM**: 2 GB
- **OS**: Windows 10+, macOS 10.14+, Linux (any recent distro)

### Recommended
- **Python**: 3.9 or higher
- **Disk Space**: 1 GB
- **RAM**: 8 GB (for large simulations)
- **OS**: Latest stable version

---

## Troubleshooting

### Common Issues

**"Python not found"**
- Install Python from https://www.python.org/downloads/
- Make sure to add Python to PATH

**"Permission denied" (Linux/macOS)**
```bash
chmod +x setup.sh
```

**Virtual environment won't activate (Windows PowerShell)**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Package installation fails**
```bash
# Upgrade pip first
pip install --upgrade pip

# Try minimal installation
pip install -r requirements-minimal.txt
```

**Matplotlib won't display plots**
- **Linux**: `sudo apt install python3-tk`
- **macOS**: `brew install python-tk`

For more detailed troubleshooting, see [INSTALLATION.md](INSTALLATION.md).

---

## Platform-Specific Notes

### macOS
- Use Homebrew to install Python: `brew install python@3.11`
- May need to install python-tk: `brew install python-tk`

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk
```

### Windows
- Download Python from python.org
- **Important**: Check "Add Python to PATH" during installation

---

## Next Steps After Installation

1. **Verify installation**: Run `python test_installation.py`

2. **Quick demo**: 
   ```bash
   python rebonato_denev_eurozone_crisis.py
   ```

3. **Explore models**:
   - Eurozone Breakup: `rebonato_denev_eurozone_crisis.py`
   - Trump Tariffs 2025: `trump_tariffs_2025_blackswan.py`

4. **Interactive tutorial**:
   ```bash
   jupyter notebook rebonato_denev_tutorial.ipynb
   ```

5. **Read documentation**:
   - Quick Start: `QUICK_START.md`
   - Trump Tariffs Analysis: `TRUMP_TARIFFS_2025_ANALYSIS.md`
   - Complete Index: `MASTER_INDEX.md`

---

## Updating

To update to the latest package versions:

```bash
pip install --upgrade -r requirements.txt
```

---

## Uninstalling

### Remove Virtual Environment
```bash
deactivate           # If activated
rm -rf venv          # Linux/macOS
rmdir /s venv        # Windows
```

### Uninstall Packages
```bash
pip uninstall -r requirements.txt -y
```

---

## Getting Help

If you run into issues:

1. **Check** [INSTALLATION.md](INSTALLATION.md) for detailed troubleshooting
2. **Run** `python test_installation.py` to diagnose problems
3. **Verify** Python version: `python --version` (must be 3.8+)
4. **Try** minimal installation first: `pip install -r requirements-minimal.txt`

---

## Development Setup

For contributors or advanced users:

```bash
# Install full requirements
pip install -r requirements.txt

# Install development tools
pip install pytest black flake8 mypy

# Run tests
pytest

# Format code
black .
```

---

## File Checksums (Optional Verification)

For security-conscious users, you can verify file integrity:

```bash
# Linux/macOS
sha256sum requirements.txt requirements-minimal.txt

# Windows PowerShell
Get-FileHash requirements.txt, requirements-minimal.txt -Algorithm SHA256
```

---

## License

All setup scripts and requirements files are part of this educational project.
Dependencies have their own licenses (all permissive open-source).

---

**Setup Version**: 1.0  
**Last Updated**: November 2025  
**Compatible**: Python 3.8+  
**Tested**: Ubuntu 24.04, macOS 14, Windows 11
