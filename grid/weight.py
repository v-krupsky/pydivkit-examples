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
            text='The weight of a table element.',
        ),
        Subtitle(
            text='The weight of an element determines how much space it '
                 'occupies inside the table. It can be applied to both width '
                 'and height.\n\nIn the example, elements 2 and 3 have a '
                 'width weight of 2.\n',
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        dk.DivGrid(
            # For below, the DivKit example is:
            # "width": {
            #    "type": "match_parent",
            #    "value": 240
            # },
            # but it does not make much sense as "value" is not supported by
            # "match_parent" type. This code provides render, identical to
            # the DivKit example.
            width=dk.DivMatchParentSize(),
            height=dk.DivFixedSize(value=160),
            column_count=3,
            items=[
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    height=dk.DivMatchParentSize(weight=1),
                    margins=dk.DivEdgeInsets(right=8, bottom=8),
                    text='1'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=2),
                    height=dk.DivMatchParentSize(weight=1),
                    margins=dk.DivEdgeInsets(bottom=8),
                    column_span=2,
                    text='2'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=2),
                    height=dk.DivMatchParentSize(weight=1),
                    margins=dk.DivEdgeInsets(right=8),
                    column_span=2,
                    text='3'
                ),
                TextBlock(
                    width=dk.DivMatchParentSize(weight=1),
                    height=dk.DivMatchParentSize(weight=1),
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
