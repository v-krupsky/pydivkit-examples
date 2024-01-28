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
    font_size = 15
    text_color = '#000000'
    paddings = dk.DivEdgeInsets(left=24, right=24, top=4, bottom=4)


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
                        text='Text properties',
                    ),
                    Subtitle(
                        text='All possible properties that can be applied to '
                             'text',
                        margins=dk.DivEdgeInsets(bottom=12),
                    ),
                    dk.DivContainer(
                        paddings=dk.DivEdgeInsets(top=12, bottom=12),
                        background=[dk.DivSolidBackground(color='#0E000000')],
                        items=[
                            TextBlock(
                                text='Change the text size',
                                font_size=22,
                            ),
                            TextBlock(
                                text='Change the font style',
                                font_weight=dk.DivFontWeight.BOLD,
                            ),
                            TextBlock(
                                text='Underline text',
                                underline='single',
                            ),
                            TextBlock(
                                text='Cross out text (strikethrough)',
                                strike='single',
                            ),
                            TextBlock(
                                text='Change the space between characters',
                                letter_spacing=3,
                            ),
                            TextBlock(
                                text='Change the text color',
                                text_color='#3F28C3',
                            ),
                            TextBlock(
                                text='Change the alignment',
                                text_alignment_horizontal=dk.
                                DivAlignmentHorizontal.RIGHT,
                            ),
                            TextBlock(
                                text='Change the height of a line',
                                line_height=52,
                            ),
                            TextBlock(
                                text='Set the maximum number of lines in the '
                                     'text. Set the maximum number of lines '
                                     'in the text. Set the maximum number of '
                                     'lines in the text. Set the maximum '
                                     'number of lines in the text. Set the '
                                     'maximum number of lines in the text. '
                                     'Set the maximum number of lines in the '
                                     'text. Set the maximum number of lines in '
                                     'the text. Set the maximum number of '
                                     'lines in the text.',
                                max_lines=2,
                            ),
                            TextBlock(
                                text='You can highlight and copy this text',
                                selectable=True,
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
