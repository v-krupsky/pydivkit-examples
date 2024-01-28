import pydivkit as dk
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    font_size = 12
    line_height = 15
    height = dk.DivMatchParentSize()
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = "#000000"
    paddings = dk.DivEdgeInsets(top=16, bottom=16, left=8, right=8)
    background = [dk.DivSolidBackground(color="#0E000000")]


# Results in template 'title'
class Title(dk.DivText):
    __template_name__ = 'title'
    font_size = 20
    line_height = 24
    font_weight = dk.DivFontWeight.BOLD
    paddings = dk.DivEdgeInsets(left=24, right=24, bottom=16)


# Results in template 'subtitle'
class Subtitle(dk.DivText):
    __template_name__ = 'subtitle'
    font_size = 15
    line_height = 20
    paddings = dk.DivEdgeInsets(left=24, right=24)


# Compiles elements into a container
container = dk.DivContainer(
    orientation=dk.DivContainerOrientation.VERTICAL,
    margins=dk.DivEdgeInsets(top=24, bottom=24),
    height=dk.DivMatchParentSize(),
    items=[
        Title(
            text='Horizontal container',
            margins=dk.DivEdgeInsets(bottom=8)
        ),
        Subtitle(
            text='Similar to a vertical container, but the elements are '
                 'arranged horizontally.',
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        dk.DivContainer(
            orientation=dk.DivContainerOrientation.HORIZONTAL,
            items=[
                dk.DivContainer(
                    orientation=dk.DivContainerOrientation.HORIZONTAL,
                    height=dk.DivFixedSize(value=60),
                    items=[
                        TextBlock(
                            text='wrap_content',
                        ),
                        TextBlock(
                            text='Weight = 1',
                            width=dk.DivMatchParentSize(weight=1),
                            margins=dk.DivEdgeInsets(left=2),
                        ),
                        TextBlock(
                            text='Weight = 2',
                            width=dk.DivMatchParentSize(weight=2),
                            margins=dk.DivEdgeInsets(left=2),
                        ),
                        TextBlock(
                            text='wrap_content',
                            margins=dk.DivEdgeInsets(left=2),
                        ),
                    ]
                )
            ]
        )
    ]
)

# Prints the JSON representation of the container
print(
    json.dumps(
        dk.make_div(container),
        indent=4
    )
)
