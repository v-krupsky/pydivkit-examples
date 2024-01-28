import pydivkit as dk
import json


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


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    text_color = '#ffffff'
    height = dk.DivFixedSize(value=184)
    paddings = dk.DivEdgeInsets(left=16, right=16, bottom=16)
    margins = dk.DivEdgeInsets(left=24, right=24, bottom=16)
    text_alignment_vertical = dk.DivAlignmentVertical.BOTTOM
    font_size = 15
    line_height = 20


# Prepare DivData object
data = dk.DivData(
    log_id='sample_card',
    states=[
        dk.DivDataState(
            state_id=0,
            div=dk.DivContainer(
                orientation=dk.DivContainerOrientation.VERTICAL,
                margins=dk.DivEdgeInsets(top=24, bottom=24),
                items=[
                    Title(
                        text='Background',
                    ),
                    Subtitle(
                        text='It can be a solid color, gradient, or an image. '
                             'You can also overlay multiple backgrounds on '
                             'top of each other.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        items=[
                            TextBlock(
                                height=dk.DivFixedSize(value=150),
                                background=[
                                    dk.DivSolidBackground(
                                        color='#C4C4C4',
                                        # DivKit example provides
                                        # "angle": 270 at this point, but
                                        # dk.SolidBackground does not support
                                        # angle. Removing the instruction in
                                        # the DivKit example does not seem to
                                        # affect the result.
                                    ),
                                ],
                                text_alignment_vertical=dk.DivAlignmentVertical.
                                BOTTOM,
                                text='Solid background',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(value=150),
                                background=[
                                    dk.DivLinearGradient(
                                        colors=[
                                            '#0fff',
                                            '#000',
                                        ],
                                        angle=270,
                                    ),
                                ],
                                text_alignment_vertical=dk.DivAlignmentVertical.
                                BOTTOM,
                                text='Gradient',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(value=150),
                                background=[
                                    dk.DivImageBackground(
                                        image_url='https://yastatic.net/s3'
                                                  '/home/yandex-app/div_demo'
                                                  '/containers.png',
                                    ),
                                ],
                                text_alignment_vertical=dk.DivAlignmentVertical.
                                BOTTOM,
                                text='Image',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(value=150),
                                background=[
                                    dk.DivImageBackground(
                                        image_url='https://yastatic.net/s3'
                                                  '/home/yandex-app/div_demo'
                                                  '/containers.png',
                                    ),
                                    dk.DivLinearGradient(
                                        colors=[
                                            '#0fff',
                                            '#000',
                                        ],
                                        angle=270,
                                    ),
                                ],
                                text_alignment_vertical=dk.DivAlignmentVertical.
                                BOTTOM,
                                text='Gradient and image',
                            ),
                        ],
                    ),
                ]
            ),
        )
    ],
)


# Prepare the dictionary
dct = {
    'templates': {
        tpl.template_name: tpl.template()
        for tpl in data.related_templates()
    },
    'card': data.dict()
}
print(json.dumps(dct, indent=4))
