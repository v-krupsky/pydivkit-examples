import pydivkit as dk
import json


# Results in template 'empty_block'
class EmptyBlock(dk.DivText):
    __template_name__ = 'empty_block'
    text = '   '
    width = dk.DivFixedSize(value=100)
    height = dk.DivFixedSize(value=100)


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
    variables=[
        dk.StringVariable(
            name='value_variable',
            value='',
        ),
    ],
    states=[
        dk.DivDataState(
            state_id=0,
            div=dk.DivContainer(
                orientation=dk.DivContainerOrientation.VERTICAL,
                margins=dk.DivEdgeInsets(top=24, bottom=24),
                items=[
                    Title(
                        text='Select',
                    ),
                    Subtitle(
                        text='Allows you to select an option from a '
                             'predefined list.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    Subtitle(
                        text='Options may have different values for user and '
                             'application.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        paddings=dk.DivEdgeInsets(left=24, right=24),
                        items=[
                            dk.DivSelect(
                                width=dk.DivMatchParentSize(),
                                height=dk.DivWrapContentSize(),
                                paddings=dk.DivEdgeInsets(
                                    left=16, top=10, right=16, bottom=10
                                ),
                                alpha=1,
                                alignment_horizontal=dk.DivAlignmentHorizontal.
                                CENTER,
                                alignment_vertical=dk.DivAlignmentVertical.
                                CENTER,
                                background=[
                                    dk.DivSolidBackground(
                                        color='#0e000000'
                                    )
                                ],
                                border=dk.DivBorder(corner_radius=8),
                                font_size=16,
                                font_weight=dk.DivFontWeight.MEDIUM,
                                text_color='#000000',
                                value_variable='value_variable',
                                hint_text='Select option',
                                hint_color='#888888',
                                line_height=22,
                                options=[
                                    dk.DivSelectOption(
                                        value='value_for_option_{}'.format(i),
                                        text='Option {}'.format(i),
                                    ) for i in range(1,4)
                                ],
                            ),
                            dk.DivText(
                                text=' ',
                                height=dk.DivFixedSize(value=16),
                            ),
                            dk.DivText(
                                width=dk.DivMatchParentSize(),
                                height=dk.DivWrapContentSize(),
                                font_size=16,
                                text_color='#000000',
                                text='Value: @{value_variable}',
                            )
                        ]
                    )
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
