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
    id = 'visible_id'
    width = dk.DivMatchParentSize()
    height = dk.DivFixedSize(value=88)
    border = dk.DivBorder(corner_radius=16)
    margins = dk.DivEdgeInsets(top=8, left=24, right=24)
    background = [dk.DivSolidBackground(color='#0E000000')]
    text_color = '#000000'
    font_size = 14
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER


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
                        text='Border',
                    ),
                    Subtitle(
                        text='Using a border, you can set the corner radius ('
                             'round corners), outline, and shadows.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        items=[
                            TextBlock(
                                text='Shadow',
                                border=dk.DivBorder(has_shadow=True),
                            ),
                            TextBlock(
                                text='Corner radius 16dp',
                                border=dk.DivBorder(corner_radius=16),
                            ),
                            TextBlock(
                                text='Stroke 8dp',
                                border=dk.DivBorder(
                                    stroke=dk.DivStroke(
                                        color='#3F28C3',
                                        width=8,
                                    ),
                                ),
                            ),
                            TextBlock(
                                text='Set',
                                border=dk.DivBorder(
                                    stroke=dk.DivStroke(
                                        color='#3F28C3',
                                        width=8,
                                    ),
                                    corner_radius=16,
                                    has_shadow=True,
                                ),
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
