# Quick Start Guide
## Rebonato-Denev Bayesian Networks for Black Swan Events

---

## What You Have

A complete implementation of Riccardo Rebonato and Alexander Denev's Bayesian network methodology for modeling "black swan" financial events - specifically, the Eurozone breakup scenario.

---

## Files at a Glance

| File | Purpose | Size |
|------|---------|------|
| `rebonato_denev_eurozone_crisis.py` | Main implementation | 22 KB |
| `rebonato_denev_tutorial.ipynb` | Interactive notebook | 11 KB |
| `README.md` | Comprehensive documentation | 8 KB |
| `PROJECT_SUMMARY.md` | Executive summary | 8 KB |
| `eurozone_crisis_network.png` | Network structure | 334 KB |
| `scenario_comparison.png` | Results visualization | 383 KB |
| `causal_flow.png` | Probability flow diagram | 303 KB |
| `requirements.txt` | Dependencies | <1 KB |

---

## Run It Now (3 Options)

### Option 1: Quick Demo (2 minutes)
```bash
python rebonato_denev_eurozone_crisis.py
```
This runs the complete analysis and shows:
- 4 stress scenarios
- Portfolio implications
- Monte Carlo simulation results

### Option 2: Interactive Exploration (10 minutes)
```bash
jupyter notebook rebonato_denev_tutorial.ipynb
```
Step-by-step tutorial with:
- Custom scenario analysis
- Interactive visualizations
- Portfolio allocation examples

### Option 3: Just See the Pictures
Open these files:
- `eurozone_crisis_network.png` - The causal structure
- `scenario_comparison.png` - All results in one view
- `causal_flow.png` - How probabilities propagate

---

## Key Insights (TL;DR)

### The Problem with Traditional Approaches
❌ Historical correlations break down during crises  
❌ Can't model events that haven't happened  
❌ No understanding of causality  

### The Rebonato-Denev Solution
✅ Explicit causal modeling  
✅ Forward-looking scenarios  
✅ Expert judgment + data  
✅ Bayesian updating  

### What the Model Shows

**Normal Times** → 7% breakup risk, 22% equity decline  
**Black Swan** (High politics + econ crisis) → 76% breakup risk, 62% equity decline  
**If Breakup Occurs** → 88% flight to quality, 76% equity decline  
**Market Signals** (Spreads widening + flight) → 96% inferred breakup risk

### Portfolio Implications

| Scenario | Recommendation |
|----------|----------------|
| Normal | 60% equities, 30% corp bonds, 10% gov bonds |
| Elevated Risk | 40% equities, 20% corp bonds, 40% gov bonds |
| High Stress | 20% equities, 10% corp bonds, 70% gov bonds |

---

## The "Black Swan" Connection

### What Makes It a Black Swan?

1. **Rare**: Eurozone breakup unprecedented in modern finance
2. **High Impact**: Affects ~20% of global GDP, €20 trillion contracts
3. **Retrospectively Predictable**: We can reason about causality

### Why This Matters

Traditional models say: *"It hasn't happened, so we can't model it"*

Rebonato-Denev says: *"We understand the causal mechanisms, so we CAN model it"*

This is the difference between **correlation** and **causation**.

---

## Understanding the Network

### The Causal Chain

```
ROOT CAUSES
  Political_Instability (EU tensions)
  Economic_Weakness (GDP, unemployment)
        ↓
CRISIS EVENT  
  Eurozone_Breakup (THE BLACK SWAN)
        ↓
MARKET MECHANISMS
  Credit_Spreads (widen during stress)
  Flight_to_Quality (rush to safety)
        ↓
ASSET IMPACTS
  Corporate_Bonds (credit sensitive)
  Government_Bonds (safe haven)
  Equities (most vulnerable)
```

### Why This Structure?

- **Political_Instability** → Increases breakup risk (sovereignty concerns)
- **Economic_Weakness** → Increases breakup risk (costs of membership)
- **Eurozone_Breakup** → Causes market disruption
- **Credit_Spreads** → Corporate bonds become risky
- **Flight_to_Quality** → Investors seek safety
- **Asset Classes** → React based on their characteristics

---

## Practical Usage

### For Portfolio Managers

1. **Monitor leading indicators** (politics, economics)
2. **Calculate scenario probabilities** using the network
3. **Adjust allocations** dynamically
4. **Stress test** portfolios under extreme scenarios

### For Risk Managers

1. **Model tail risks** beyond VaR
2. **Early warning system** via probability updates
3. **Scenario planning** for crisis response
4. **Regulatory compliance** (Basel III stress tests)

### For Researchers

1. **Extend to other black swans** (pandemic, cyber attack)
2. **Add more variables** (central bank policy, contagion)
3. **Learn from data** (estimate probabilities empirically)
4. **Integrate with ML** (hybrid models)

---

## Next Steps

### Immediate
1. Run the demo script
2. Look at the visualizations  
3. Read the README for details

### Short-term
1. Modify probabilities to reflect your views
2. Add new variables to the network
3. Try different scenarios
4. Compare with your current portfolio

### Long-term
1. Apply to other crisis scenarios
2. Integrate with real market data
3. Build production-grade system
4. Validate with historical crises

---

## Common Questions

**Q: Why not just use correlations?**  
A: Correlations break down during crises. Causal relationships are more stable.

**Q: Aren't the probabilities subjective?**  
A: Yes, that's the point. Expert judgment is necessary for unprecedented events. But the logic is rigorous.

**Q: Can this predict the future?**  
A: No model predicts the future. But it helps you reason systematically about possibilities.

**Q: What about other black swans?**  
A: The methodology applies to any scenario you can model causally (pandemic, climate, cyber).

**Q: Is this better than traditional VaR?**  
A: It's complementary. VaR handles normal times. This handles tail events.

---

## Resources

### Essential Reading
- Rebonato & Denev (2014) - The original book
- Pearl (2009) "Causality" - The foundations
- Taleb (2007) "The Black Swan" - The problem this solves

### Technical Background
- Bayesian networks: Pearl, Koller & Friedman
- Portfolio theory: Markowitz, Black-Litterman
- Stress testing: Basel Committee guidelines

### Code Examples
All in this package - it's complete and self-contained!

---

## Support

This is an educational implementation. For production use:
- Consult the original book for full methodology
- Validate probabilities with domain experts
- Consider established libraries (pgmpy, PyMC)
- Add comprehensive testing
- Integrate real market data

---

## Final Thought

> "The core of the problem is that past data is not necessarily indicative of future performance, especially during periods of stress."  
> — Riccardo Rebonato

This implementation shows how to move beyond that limitation by modeling causality, not just correlation.

**Enjoy exploring!**
