from CBD.lib.std import BaseBlock
import CBD.converters.latexify as latexify


def block_to_latex(block: BaseBlock):
    latexobject = latexify.CBD2Latex(block, show_steps=True)
    print(latexobject.render())
