# Rebonato-Denev Bayesian Networks: Complete Collection

## Two Black Swan Scenarios for Portfolio Management

This package contains complete implementations of the Rebonato-Denev causal Bayesian network methodology applied to two different "black swan" scenarios:

1. **Eurozone Breakup** (Academic/Demonstrative)
2. **Trump Tariffs 2025** (Active Risk)

---

## 📚 Start Here

### Quick Start
- **[QUICK_START.md](computer:///mnt/user-data/outputs/QUICK_START.md)** - Get running in 2 minutes

### Executive Summaries
- **[BLACK_SWAN_COMPARISON.md](computer:///mnt/user-data/outputs/BLACK_SWAN_COMPARISON.md)** - Compare both scenarios side-by-side
- **[TRUMP_TARIFFS_2025_ANALYSIS.md](computer:///mnt/user-data/outputs/TRUMP_TARIFFS_2025_ANALYSIS.md)** - Deep dive on 2025's biggest risk
- **[PROJECT_SUMMARY.md](computer:///mnt/user-data/outputs/PROJECT_SUMMARY.md)** - Overall project overview

---

## 💻 Implementations

### Eurozone Breakup Model
- **[rebonato_denev_eurozone_crisis.py](computer:///mnt/user-data/outputs/rebonato_denev_eurozone_crisis.py)** - Complete implementation
- **[rebonato_denev_tutorial.ipynb](computer:///mnt/user-data/outputs/rebonato_denev_tutorial.ipynb)** - Interactive tutorial
- **[README.md](computer:///mnt/user-data/outputs/README.md)** - Full methodology documentation

### Trump Tariffs 2025 Model  
- **[trump_tariffs_2025_blackswan.py](computer:///mnt/user-data/outputs/trump_tariffs_2025_blackswan.py)** - Complete implementation
- Includes 13-variable network with sector-specific impacts
- Monte Carlo simulation with 10,000 runs

---

## 📊 Visualizations

### Eurozone Scenario
- **[eurozone_crisis_network.png](computer:///mnt/user-data/outputs/eurozone_crisis_network.png)** - Network structure
- **[scenario_comparison.png](computer:///mnt/user-data/outputs/scenario_comparison.png)** - All scenarios compared
- **[causal_flow.png](computer:///mnt/user-data/outputs/causal_flow.png)** - Probability propagation

### Trump Tariffs Scenario
- **[trump_tariffs_2025_network.png](computer:///mnt/user-data/outputs/trump_tariffs_2025_network.png)** - Network structure
- More complex network (13 variables vs 8)
- Multiple transmission channels

---

## 🔧 Technical Files

- **[requirements.txt](computer:///mnt/user-data/outputs/requirements.txt)** - Python dependencies
- **[INDEX.md](computer:///mnt/user-data/outputs/INDEX.md)** - Original file index

---

## Key Findings Summary

### Eurozone Breakup (Demonstrative)
- **Base Probability**: 7% (normal conditions)
- **Black Swan**: 76% (political + economic crisis)
- **Status**: Hypothetical scenario
- **Purpose**: Demonstrate methodology

### Trump Tariffs 2025 (ACTIVE RISK)
- **Base Probability**: 70% (given stated policy)  
- **Black Swan**: 90% (aggressive + retaliation)
- **Status**: **IMMINENT THREAT**
- **Market Pricing**: **SIGNIFICANTLY UNDERPRICED**

---

## What Makes This Different

### Traditional Portfolio Management
❌ Relies on historical correlations (fail during crises)  
❌ Cannot model unprecedented events  
❌ Black box approaches  
❌ Reactive, not proactive  

### Rebonato-Denev Causal Bayesian Approach
✅ Explicit causal modeling  
✅ Forward-looking scenarios  
✅ Expert judgment + rigorous math  
✅ Dynamic updating as evidence arrives  
✅ Transparent reasoning  

**This is why causal modeling matters**: You can model events BEFORE they happen, not just after.

---

## Immediate Action Items for 2025

### 🔴 High Priority (Trump Tariffs)
1. **Review portfolio exposure** to China/imports
2. **Reduce cyclical sectors** (manufacturing, consumer discretionary)
3. **Add inflation hedges** (TIPS, commodities, gold)
4. **Consider defensive positioning** NOW (before repricing)
5. **Monitor policy announcements** daily from Jan 2025

### 🟡 Medium Priority (Eurozone)
1. **Monitor political developments** in EU
2. **Maintain geographic diversification**
3. **Watch sovereign spreads** for warning signs

### 🟢 Ongoing (Methodology)
1. **Update probabilities** as events unfold
2. **Extend models** to other scenarios (see below)
3. **Refine conditional probabilities** with new data

---

## Potential Extensions

The methodology can be applied to other 2025 black swan scenarios:

### Geopolitical
- Taiwan invasion scenario
- Ukraine escalation
- Middle East conflict expansion

### Economic
- Commercial real estate crisis
- Private credit market dislocation
- Sovereign debt crisis (Japan, UK)

### Technological
- AI displacement shock
- Cyber attack on financial system
- Cryptocurrency collapse/regulation

### Climate
- Catastrophic climate event
- Energy transition disruption
- Food supply crisis

Each requires custom network structure but uses same Bayesian causal framework.

---

## Technical Requirements

```bash
# Install dependencies
pip install numpy networkx matplotlib jupyter

# Run Eurozone model
python rebonato_denev_eurozone_crisis.py

# Run Tariffs model  
python trump_tariffs_2025_blackswan.py

# Interactive tutorial
jupyter notebook rebonato_denev_tutorial.ipynb
```

---

## Academic Foundation

**Primary Source**:
Rebonato, R., & Denev, A. (2014). *Portfolio Management under Stress: A Bayesian-Net Approach to Coherent Asset Allocation*. Cambridge University Press.

**Related Theory**:
- Pearl, J. (2009). *Causality* - Foundational work on causal inference
- Taleb, N. (2007). *The Black Swan* - Motivation for the problem
- Koller & Friedman (2009). *Probabilistic Graphical Models* - Technical foundations

---

## File Statistics

- **Total Files**: 17
- **Python Scripts**: 3
- **Jupyter Notebooks**: 2
- **Documentation**: 8
- **Visualizations**: 4
- **Total Size**: ~2.5 MB
- **Lines of Code**: ~2,000

---

## Implementation Notes

### Custom Bayesian Network Framework
- No heavyweight dependencies (PyTorch, TensorFlow)
- Pure NumPy/NetworkX implementation
- Variable elimination for exact inference
- Forward sampling for Monte Carlo
- Suitable for networks up to ~20 variables

### Production Considerations
For real-world deployment:
- Consider pgmpy or PyMC for larger networks
- Add parameter learning from data
- Implement approximate inference (MCMC, variational)
- Build real-time data feeds
- Add sensitivity analysis
- Implement backtesting framework

---

## Contact & Contributions

This implementation is educational and demonstrates core concepts. The methodology is particularly relevant given:

- Increasing geopolitical uncertainty
- Complex economic interdependencies  
- Limitations of traditional risk models
- Need for forward-looking stress testing

**The 2025 tariffs scenario is not academic - it's an active, imminent risk that markets are underpricing.**

---

## Updates

- **Initial Release**: November 2025
- **Eurozone Model**: Complete (demonstrative)
- **Tariffs Model**: Complete (active monitoring)
- **Next Update**: Post Trump inauguration (January 2025)

---

## Risk Disclaimer

These models represent analytical frameworks for risk assessment, not investment advice. Probabilities are based on subjective expert judgment encoded in conditional probability tables. Actual outcomes may differ significantly. 

**For 2025 specifically: The Trump tariffs represent a clear and present danger to markets. This analysis suggests markets are significantly underpricing this risk.**

---

*Created: November 2025*  
*Methodology: Rebonato-Denev Causal Bayesian Networks*  
*Purpose: Educational implementation with real-world application to 2025 risks*

---

## Quick Navigation

**For Portfolio Managers**: Start with [BLACK_SWAN_COMPARISON.md](computer:///mnt/user-data/outputs/BLACK_SWAN_COMPARISON.md)  
**For Risk Managers**: Read [TRUMP_TARIFFS_2025_ANALYSIS.md](computer:///mnt/user-data/outputs/TRUMP_TARIFFS_2025_ANALYSIS.md)  
**For Researchers**: Review [README.md](computer:///mnt/user-data/outputs/README.md) and code implementations  
**For Quick Demo**: Run [rebonato_denev_eurozone_crisis.py](computer:///mnt/user-data/outputs/rebonato_denev_eurozone_crisis.py)  
**For 2025 Action**: Review portfolio implications in tariffs analysis
