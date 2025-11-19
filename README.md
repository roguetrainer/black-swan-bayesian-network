# Rebonato-Denev Bayesian Network for Black Swan Events

## Overview

This implementation demonstrates the Bayesian network methodology from **"Portfolio Management under Stress: A Bayesian-Net Approach to Coherent Asset Allocation"** by Riccardo Rebonato and Alexander Denev (Cambridge University Press, 2014).

The examples focuses on modelling  **black swan events**: 
* the potential breakup of the Eurozone, and its cascading effects on financial markets ~2010-2012
* Trump's tariffs affecting global trade in 2025

![Black Swan](blackswan.png)


### Taleb's Black Swan

The term **Black Swan** in the context of financial risk and broader impact was popularized by writer, statistician, and former options trader **Nassim Nicholas Taleb**.

He extensively discussed the concept in his 2007 book, *The Black Swan: The Impact of the Highly Improbable*.

#### 🦢 What a Black Swan Event Means

According to Taleb, a Black Swan event is an event with three principal attributes:

🦤  **Rarity (The Outlier):** It is an **outlier** because it lies outside the realm of regular expectations, as nothing in the past definitively points to its possibility.
💣  **Extreme Impact:** It carries an **extreme impact** when it occurs, causing widespread and severe consequences across markets, economies, or societies.
🔮  **Retrospective Predictability:** In spite of its outlier status, human nature leads people to invent explanations for it **after the fact**, making it appear predictable in hindsight (known as *hindsight bias*).

In finance, these events are particularly dangerous because standard risk models often fail to account for them, leading to massive, unpredictable losses. Examples often cited include the **2008 Global Financial Crisis** and the **COVID-19 pandemic**.

If you'd like to know more about Taleb's other concepts, 🕵️‍♀️ search for **Antifragility**.

## Key Innovation: Causal Modeling for Stress Testing

Unlike traditional portfolio management approaches that rely on historical correlations, Rebonato and Denev advocate for:

1. **Causal Structure**: Explicitly modeling how crises propagate through markets
2. **Forward-Looking Scenarios**: Incorporating extreme events that may not be present in historical data
3. **Expert Judgment**: Encoding subjective probabilities based on domain knowledge
4. **Scenario Analysis**: Portfolio optimization under stress conditions, not just "normal times"

## The Eurozone Crisis Network

### Network Structure

The Bayesian network models the following causal relationships:

```
Political_Instability ──┐
                        ├──> Eurozone_Breakup ──> Credit_Spreads ──> Corporate_Bonds
Economic_Weakness ─────┘                     │                   │
                                             │                   └──> Equities
                                             │                         ↑
                                             └──> Flight_to_Quality ───┤
                                                         │              │
                                                         └──> Government_Bonds
```

### Variables and States

| Variable | States | Description |
|----------|--------|-------------|
| Political_Instability | Low, High | Political tensions within Eurozone |
| Economic_Weakness | Low, High | Economic indicators (GDP, unemployment) |
| Eurozone_Breakup | No, Yes | **The Black Swan Event** |
| Credit_Spreads | Normal, Widening | Corporate credit spreads |
| Flight_to_Quality | No, Yes | Flight to safe-haven assets |
| Corporate_Bonds | Stable, Falling | Corporate bond performance |
| Government_Bonds | Stable, Rally | Government bond performance |
| Equities | Stable, Falling | Equity market performance |

## Implementation

### Framework Used

The implementation uses a custom Bayesian network framework built with:
- **NumPy**: For numerical computations
- **NetworkX**: For graph structure
- **Matplotlib**: For visualization

This avoids heavyweight dependencies like PyTorch while maintaining full functionality.

### Key Components

1. **BayesianNetwork Class**: Core implementation with:
   - Conditional Probability Tables (CPDs)
   - Variable elimination for inference
   - Forward sampling for Monte Carlo simulation

2. **Conditional Probability Distributions**: Expert-elicited probabilities reflecting:
   - Base rates for political and economic conditions
   - Conditional probabilities linking causes to effects
   - Severity of market reactions under stress

## Example Results

### Scenario Analysis

#### Scenario 1: Normal Times
- Political Instability: Low
- Economic Weakness: Low
- → Eurozone Breakup probability: **6.7%**
- → Equity decline probability: **22.3%**

#### Scenario 2: Black Swan (High Political + Economic Crisis)
- Political Instability: High
- Economic Weakness: High
- → Eurozone Breakup probability: **76.1%**
- → Equity decline probability: **62.0%**

#### Scenario 3: Given Eurozone Breakup
- Eurozone Breakup: Yes (observed)
- → Credit Spreads Widening: **78.6%**
- → Flight to Quality: **88.0%**
- → Corporate Bonds Falling: **73.8%**
- → Government Bonds Rally: **73.3%**
- → Equities Falling: **75.7%**

#### Scenario 4: Market Stress Signals
- Credit Spreads: Widening
- Flight to Quality: Yes
- → Inferred Eurozone Breakup probability: **95.7%**
- → Equity decline probability: **90.0%**

### Monte Carlo Results

Under the black swan scenario (High Political Instability + High Economic Weakness), 10,000 simulations show:

- **Eurozone Breakup occurs**: 70.5% of scenarios
- When breakup occurs:
  - Corporate Bonds fall: 76.7%
  - Government Bonds rally: 71.9%
  - Equities fall: 77.3%

## Why This Matters: The Black Swan Connection

### Traditional vs. Rebonato-Denev Approach

**Traditional Approach (Correlation-Based)**:
- Uses historical correlations
- Assumes stable relationships
- Fails during regime changes
- Cannot model unprecedented events

**Rebonato-Denev Approach (Causal Bayesian)**:
- Models causal mechanisms
- Incorporates expert judgment about novel scenarios
- Explicitly represents extreme events
- Updates beliefs as new information arrives

### Black Swan Events

Nassim Taleb defined "black swan" events as:
1. **Rare**: Outside the realm of regular expectations
2. **High Impact**: Extreme consequences
3. **Retrospectively Predictable**: After the fact, we rationalize them

The Eurozone breakup scenario exemplifies this:
- **Rare**: No precedent in modern financial markets (unlike previous currency union dissolutions)
- **High Impact**: Would affect ~20% of global GDP and €20 trillion in contracts
- **Causal Structure**: We can reason about how it would unfold, even without historical data

### Practical Applications

1. **Stress Testing**: Banks and asset managers can model scenarios beyond historical experience
2. **Portfolio Construction**: Allocate assets based on causal understanding, not just correlations
3. **Risk Management**: Quantify tail risks that don't appear in VaR models
4. **Regulatory Compliance**: Meet stress testing requirements with forward-looking scenarios

## Key Insights from the Methodology

1. **Causality > Correlation**: Understanding causal mechanisms helps predict regime changes

2. **Expert Judgment is Necessary**: For unprecedented events, quantitative models need qualitative input

3. **Scenario Diversity**: Multiple scenarios (normal, stress, extreme) provide robust portfolios

4. **Ambiguity Aversion**: Uncertainty about probabilities themselves should affect portfolio choice

5. **Dynamic Updates**: Bayesian inference allows updating beliefs as new evidence arrives

## Running the Code

```bash
python rebonato_denev_eurozone_crisis.py
```

The script will:
1. Build the Bayesian network
2. Visualize the causal structure
3. Analyze four stress scenarios
4. Show portfolio implications
5. Run Monte Carlo simulations

## Further Reading

### Primary Source
- Rebonato, R., & Denev, A. (2014). *Portfolio Management under Stress: A Bayesian-Net Approach to Coherent Asset Allocation*. Cambridge University Press.

### Related Papers
- Rebonato, R. (2012). "A Bayesian Approach to Stress Testing and Scenario Analysis." *Journal of Investment Management*, 10(4), 19-53.

### Bayesian Networks in Finance
- Pearl, J. (2009). *Causality: Models, Reasoning and Inference*. Cambridge University Press.
- Koller, D., & Friedman, N. (2009). *Probabilistic Graphical Models: Principles and Techniques*. MIT Press.

### Black Swan Theory
- Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House.

## Extensions

Possible extensions to this implementation:

1. **More Asset Classes**: Add commodities, real estate, cryptocurrencies
2. **Quantitative Returns**: Map states to actual return distributions
3. **Multi-Period Dynamics**: Model time evolution of crises
4. **Learning from Data**: Estimate CPDs from historical data where available
5. **Portfolio Optimization**: Implement utility maximization under scenarios
6. **Ambiguity Aversion**: Model uncertainty about probabilities (Ellsberg paradox)

## Author Notes

This implementation is educational and demonstrates the core concepts. For production use:
- Consider using established libraries like `pgmpy` or `PyMC`
- Validate CPDs with domain experts
- Incorporate real market data
- Add sensitivity analysis
- Consider computational efficiency for large networks

## License

This code is provided for educational purposes. The methodology is described in detail in Rebonato & Denev's book, which should be consulted for rigorous application.
