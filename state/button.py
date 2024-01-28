import pydivkit as dk
from pydivkit.core.fields import Expr
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    width = dk.DivMatchParentSize()
    height = dk.DivWrapContentSize()
    paddings = dk.DivEdgeInsets(left=24, top=16, right=16, bottom=16)
    margins = dk.DivEdgeInsets(left=24, right=24)
    border = dk.DivBorder(corner_radius=8)
    background = [dk.DivSolidBackground(color="#0E000000")]
    font_size = 14
    font_weight = dk.DivFontWeight.MEDIUM
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = "#000000"


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
                        text='A set of states',
                    ),
                    Subtitle(
                        text='States can be used to create interactive '
                             'elements, such as buttons or expandable '
                             'content.\n\nThe example shows a button that '
                             'changes its own text when clicked.',
                        margins=dk.DivEdgeInsets(bottom=12),
                    ),
                    dk.DivState(
                        id='sample',
                        states=[
                            dk.DivStateState(
                                state_id='first',
                                div=TextBlock(
                                    text='This is first state',
                                    actions=[
                                        dk.DivAction(
                                            log_id='switch_state1',
                                            url='div-action://set_state?'
                                                'state_id=0/sample/second',
                                        ),
                                    ],
                                ),
                            ),
                            dk.DivStateState(
                                state_id='second',
                                div=TextBlock(
                                    text='This is second state',
                                    actions=[
                                        dk.DivAction(
                                            log_id='switch_state1',
                                            url='div-action://set_state?'
                                                'state_id=0/sample/first',
                                        ),
                                    ],
                                ),
                            ),
                        ],
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
