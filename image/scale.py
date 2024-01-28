import pydivkit as dk
import json


# Results in template 'title'
class Title(dk.DivText):
    __template_name__ = 'title'
    font_size = 20
    line_height = 24
    font_weight = dk.DivFontWeight.BOLD
    paddings = dk.DivEdgeInsets(left=24, right=24, bottom=24)


# Results in template 'subtitle'
class Subtitle(dk.DivText):
    __template_name__ = 'subtitle'
    font_size = 15
    line_height = 20
    paddings = dk.DivEdgeInsets(left=24, right=24, top=26)


# Results in template 'image_block'
class ImageBlock(Subtitle):  # Subtitle is used as a base class!
    __template_name__ = 'image_block'
    paddings = dk.DivEdgeInsets(left=0, right=0, top=0)
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentVertical.CENTER
    alignment_vertical = dk.DivContentAlignmentVertical.CENTER
    alignment_horizontal = dk.DivContentAlignmentHorizontal.CENTER
    text = 'Image Area'
    background = [dk.DivSolidBackground(color='#F9F9F9')]
    height = dk.DivMatchParentSize()
    width = dk.DivMatchParentSize()


# Results in template 'image_container'
class ImageContainer(dk.DivContainer):
    __template_name__ = 'image_container'
    height = dk.DivFixedSize(value=212)
    width = dk.DivFixedSize(value=180)
    background = [dk.DivImageBackground(
        image_url='https://yastatic.net/s3/home/divkit/pattern.png',
        scale=dk.DivImageScale.FILL
    )]


# Results in template 'scale_type_title'
class ScaleTypeTitle(Title):  # Title is used as a base class!
    __template_name__ = 'scale_type_title'
    font_size = 10
    line_height = 16
    paddings = dk.DivEdgeInsets(left=0, right=0, bottom=0)
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentVertical.CENTER
    alignment_vertical = dk.DivContentAlignmentVertical.CENTER
    alignment_horizontal = dk.DivContentAlignmentHorizontal.CENTER


# Compiles elements into a container
container = dk.DivContainer(
    orientation=dk.DivContainerOrientation.VERTICAL,
    content_alignment_horizontal=dk.DivContentAlignmentHorizontal.CENTER,
    margins=dk.DivEdgeInsets(top=24, bottom=24),
    items=[
        Title(
            text='Image scale',
        ),
        ImageContainer(
            items=[
                ImageBlock(
                    margins=dk.DivEdgeInsets(top=24, left=8, right=8, bottom=6),
                ),
                ScaleTypeTitle(
                    text='CROP AREA',
                    margins=dk.DivEdgeInsets(top=0, bottom=2)
                )
            ]
        ),
        Subtitle(
            text="fill: Fills all available space. If something doesn't fit, "
                 "it's cropped.",
            margins=dk.DivEdgeInsets(bottom=24)
        ),
        ImageContainer(
            orientation=dk.DivContainerOrientation.OVERLAP,
            items=[
                ImageBlock(
                    margins=dk.DivEdgeInsets(
                        left=40,
                        right=40,
                        start=40,  # Note: start and end are used instead of
                        end=40,    # top and bottom
                    ),
                    width=dk.DivFixedSize(value=100),
                ),
                ScaleTypeTitle(
                    text='WRAPPER AREA',
                    font_size=8,
                    line_height=12,
                    margins=dk.DivEdgeInsets(left=140)
                )
            ]
        ),
        Subtitle(
            text='fit: Fits into the boundaries. Any remaining space will be '
                 'empty.',
            margins=dk.DivEdgeInsets(bottom=38)
        ),
        ImageContainer(
            width=dk.DivFixedSize(value=165),
            height=dk.DivFixedSize(value=110),
            items=[ImageBlock()]
        ),
        Subtitle(
            text='fixed: Fixed image sizes and proportions.',
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
