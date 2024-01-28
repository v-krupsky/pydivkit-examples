import pydivkit as dk
import json


# Results in template 'image_block'
class ImageBlock(dk.DivImage):
    __template_name__ = 'image_block'
    height = dk.DivFixedSize(value=184)
    width = dk.DivMatchParentSize()
    margins = dk.DivEdgeInsets(left=24, right=24, bottom=8)


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
            text='Placeholder images, stubs',
        ),
        Subtitle(
            text='By default, a gray stub is used before an image loads ('
                 'first picture).\n\nYou can also set a solid colored stub ('
                 'second picture) or insert a base64-encoded image (third '
                 'picture).\n',
            margins=dk.DivEdgeInsets(bottom=32)
        ),
        dk.DivContainer(
            orientation=dk.DivContainerOrientation.VERTICAL,
            content_alignment_horizontal=dk.DivContentAlignmentHorizontal
            .CENTER,
            items=[
                ImageBlock(image_url='empty://'),
                ImageBlock(
                    placeholder_color='#8533FF',
                    image_url='empty://',
                ),
                ImageBlock(
                    preview='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/wAALCAASACABAREA/8QAFwABAAMAAAAAAAAAAAAAAAAABQMEB//EACcQAAEDAwMBCQAAAAAAAAAAAAEAAgMEBiEREzFRBRIWIjJhcYGR/9oACAEBAAA/ANprbho426tc36Q1ZeEIicA8IuO8YWTZkb+pbxvSbIG43jqsAmvKskYQHnjqjZbnrCHd6RG1dx1L/RJke6qG5u0AMyO0UdKTnKirT5D8IyiJMztcq1OBsHA4X//Z',
                    image_url='empty://',
                )
            ],
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
