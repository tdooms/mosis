from CBD.lib.std import IntegratorBlock, DerivatorBlock
from BlockToLatex import block_to_latex

# derivator block latex
print("\033[43;30mDerivator block\033[0m")
block_to_latex(DerivatorBlock("derivator"))

# integrator block latex
print("\033[43;30mIntegrator block\033[0m")
block_to_latex(IntegratorBlock("integrator"))
