import pydivkit as dk
import json


# Results in template 'text_base'
class TextBlock(dk.DivText):
    __template_name__ = 'text_base'
    paddings = dk.DivEdgeInsets(top=8, bottom=8, left=8, right=8)
    background = [dk.DivSolidBackground(color="#0E000000")]
    font_size = 12
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = "#000000"


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
    items=[
        Title(
            text='Table',
        ),
        Subtitle(
            text='Elements are arranged in rows and columns.\n\nCells in rows '
                 'and columns can be merged: in the example, element 1 merges '
                 '2 cells vertically and element 4 merges 2 cells '
                 'horizontally. There are 2 columns total in the table.',
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        dk.DivGrid(
            width=dk.DivMatchParentSize(),
            height=dk.DivWrapContentSize(),
            alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
            column_count=2,
            items=[
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    height=dk.DivFixedSize(value=124),
                    margins=dk.DivEdgeInsets(right=4, bottom=4),
                    row_span=2,
                    text='1'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    height=dk.DivMatchParentSize(),
                    margins=dk.DivEdgeInsets(bottom=4),
                    text='2'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    height=dk.DivMatchParentSize(),
                    margins=dk.DivEdgeInsets(bottom=4),
                    text='3'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    column_span=2,
                    text='4'
                ),
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
