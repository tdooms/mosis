from CBD.lib.std import IntegratorBlock, DerivatorBlock
from BlockToLatex import block_to_latex

# derivator block latex
print("Derivator block")
block_to_latex(DerivatorBlock("derivator"))

# integrator block latex
print("Integrator block")
block_to_latex(IntegratorBlock("integrator"))
