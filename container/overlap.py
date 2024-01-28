import pydivkit as dk
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    font_size = 12
    line_height = 15
    font_weight = dk.DivFontWeight.MEDIUM
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = "#ffffff"
    width = dk.DivWrapContentSize()
    paddings = dk.DivEdgeInsets(top=8, bottom=8, left=8, right=8)
    background = [dk.DivSolidBackground(color="#48000000")]


# Results in template 'image_block'
class ImageBlock(dk.DivImage):
    __template_name__ = 'image_block'
    image_url = 'https://yastatic.net/s3/home/yandex-app/div_demo/containers.png'
    scale = dk.DivImageScale.FILL
    height = dk.DivMatchParentSize()


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
        Title(text='Overlay container'),
        Subtitle(
            text='The elements are layered on top of each other in the order '
                 'of their position in the items array.',
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        dk.DivContainer(
            orientation=dk.DivContainerOrientation.OVERLAP,
            height=dk.DivFixedSize(value=150),
            items=[
                ImageBlock(),
                TextBlock(
                    text='Upper-left corner',
                    alignment_horizontal=dk.DivAlignmentHorizontal.LEFT,
                ),
                TextBlock(
                    text='Text on top',
                    margins=dk.DivEdgeInsets(left=16, top=16),
                    paddings=dk.DivEdgeInsets(
                        top=16,
                        bottom=16,
                        left=16,
                        right=16
                    ),
                    alignment_horizontal=dk.DivAlignmentHorizontal.LEFT,
                ),
                TextBlock(
                    text='Upper-right corner',
                    alignment_horizontal=dk.DivAlignmentHorizontal.RIGHT,
                ),
                TextBlock(
                    text='Lower-right corner',
                    alignment_vertical=dk.DivAlignmentVertical.BOTTOM,
                    alignment_horizontal=dk.DivAlignmentHorizontal.RIGHT,
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
