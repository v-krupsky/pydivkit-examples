import pydivkit as dk
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    font_size = 12
    line_height = 15
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = "#000000"
    width = dk.DivFixedSize(value=80)
    paddings = dk.DivEdgeInsets(top=13, bottom=13, left=8, right=8)
    background = [dk.DivSolidBackground(color="#0E000000")]
    border = dk.DivBorder(corner_radius=16)


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
        Title(text='Alignment inside a container'),
        Subtitle(text='There are 2 containers here: vertical and '
                      'horizontal. For horizontal alignment (in the '
                      'first container), alignment_horizontal is '
                      'used, and for vertical alignment (in the '
                      'second container), alignment_vertical is used.'),
        dk.DivContainer(
            orientation=dk.DivContainerOrientation.VERTICAL,
            margins=dk.DivEdgeInsets(top=24, bottom=24),
            items=[
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.LEFT,
                    text='left',
                ),
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                    text='center',
                ),
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.RIGHT,
                    text='right',
                ),
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.LEFT,
                    text='left',
                ),
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                    text='center',
                ),
                TextBlock(
                    alignment_horizontal=dk.DivAlignmentHorizontal.RIGHT,
                    text='right',
                ),
                # Yes, containers are nested
                dk.DivContainer(
                    orientation=dk.DivContainerOrientation.HORIZONTAL,
                    height=dk.DivFixedSize(value=100),
                    items=[
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.TOP,
                            text='top',
                        ),
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.CENTER,
                            text='center',
                        ),
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.BOTTOM,
                            text='bottom',
                        ),
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.TOP,
                            text='top',
                        ),
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.CENTER,
                            text='center',
                        ),
                        TextBlock(
                            alignment_vertical=dk.DivAlignmentVertical.BOTTOM,
                            text='bottom',
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
