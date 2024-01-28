import pydivkit as dk
from pydivkit.core.fields import Expr
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
                        text='Applying a property to part of text',
                    ),
                    Subtitle(
                        text='Text lets you insert an image in the specified '
                             'position or change the text properties in a '
                             'certain interval.\n\nIn the example, an image '
                             'of a star was inserted into the text at '
                             'position 71, the color of the characters of the '
                             'first word was changed, the distance between the '
                             'characters of the third word was increased, and '
                             'a word was underlined.',
                        margins=dk.DivEdgeInsets(bottom=12),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        items=[
                            Subtitle(
                                alignment_horizontal=dk.DivAlignmentHorizontal.
                                CENTER,
                                width=dk.DivMatchParentSize(),
                                margins=dk.DivEdgeInsets(left=0, right=0),
                                paddings=dk.DivEdgeInsets(left=4, right=4,
                                                          top=16, bottom=16),
                                background=[dk.DivSolidBackground(color=
                                                                   "#0E000000")],
                                max_lines=5,
                                text_alignment_vertical=dk.DivAlignmentVertical.
                                CENTER,
                                text_alignment_horizontal=dk.
                                DivAlignmentHorizontal.CENTER,
                                ranges=[
                                    dk.DivTextRange(
                                        start=0,
                                        end=5,
                                        font_weight=dk.DivFontWeight.BOLD,
                                        text_color='#3F28C3',
                                    ),
                                    dk.DivTextRange(
                                        start=12,
                                        end=17,
                                        underline='single',
                                        letter_spacing=5,
                                    ),
                                ],
                                images=[
                                    dk.DivTextImage(
                                        start=71,
                                        url='https://yastatic.net/s3/home/'
                                            'divkit/star.png',
                                    ),
                                ],
                                text='Lorem ipsum dolor sit amet, consectetur '
                                     'adipiscing elit, sed do eiusmodtempor '
                                     'incididunt ut labore et dolore magna '
                                     'aliqua. Ut enim ad minim veniam, quis '
                                     'nostrud exercitation ullamco laboris '
                                     'nisi ut aliquip ex ea commodo consequat. '
                                     'Duis aute irure dolor in reprehenderit '
                                     'in voluptate velit esse cillum dolore eu '
                                     'fugiat nulla pariatur.',
                            )
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
