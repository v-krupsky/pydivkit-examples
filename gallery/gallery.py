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
    paddings = dk.DivEdgeInsets(top=4, bottom=4, left=8, right=8)
    width = dk.DivFixedSize(value=80)
    height = dk.DivFixedSize(value=104)
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
        Title(
            text='Gallery',
        ),
        Subtitle(
            text='Displays elements with any content, not just images. It '
                 'lets you set the distance between adjacent elements.',
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        dk.DivGallery(
            height=dk.DivFixedSize(value=104),
            paddings=dk.DivEdgeInsets(left=16, right=16),
            item_spacing=16,
            items=[
                TextBlock(text='Item 0'),
                TextBlock(text='Item 1'),
                TextBlock(text='Item 2'),
                TextBlock(text='Item 3'),
                TextBlock(text='Item 4'),
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
