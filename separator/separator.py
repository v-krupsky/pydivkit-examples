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
    states=[
        dk.DivDataState(
            state_id=0,
            div=dk.DivContainer(
                orientation=dk.DivContainerOrientation.VERTICAL,
                margins=dk.DivEdgeInsets(top=24, bottom=24),
                items=[
                    Title(
                        text='Separator.',
                    ),
                    Subtitle(
                        text='Can be vertical or horizontal. You can set the '
                             'color or make the separator transparent.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        paddings=dk.DivEdgeInsets(left=24, right=24),
                        items=[
                            EmptyBlock(
                                width=dk.DivMatchParentSize(),
                                height=dk.DivFixedSize(value=2),
                            ),
                            dk.DivSeparator(
                                delimiter_style=dk.DivSeparatorDelimiterStyle(
                                    color='#1e000000',
                                ),
                                paddings=dk.DivEdgeInsets(top=12, bottom=12),
                            ),
                            dk.DivContainer(
                                orientation=dk.DivContainerOrientation.HORIZONTAL,
                                items=[
                                    EmptyBlock(
                                        width=dk.DivMatchParentSize(weight=4),
                                    ),
                                    dk.DivSeparator(
                                        delimiter_style=dk.DivSeparatorDelimiterStyle(
                                            orientation=dk.DelimiterStyleOrientation.VERTICAL,
                                            color='#1e000000',
                                        ),
                                        height=dk.DivFixedSize(value=100),
                                    ),
                                    EmptyBlock(
                                        width=dk.DivMatchParentSize(weight=2),
                                    ),
                                ],
                            ),
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
