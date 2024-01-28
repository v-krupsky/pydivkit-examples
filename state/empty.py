import pydivkit as dk
from pydivkit.core.fields import Expr
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'

    # Example in DivKit documentation:
    # "$text": "visible_text",
    # However, there is no variable 'visible_text' in the JSON in the example.
    # Also I could not figure out how to produce this JSON string,
    # using pydivkit.
    # Removing or leaving this line will produce the same result as in the
    # example.
    text = Expr('@{visible_text}')

    id = 'visible_id'
    width = dk.DivMatchParentSize()
    height = dk.DivFixedSize(value=88)
    border = dk.DivBorder(corner_radius=16)
    background = [dk.DivSolidBackground(color="#3F28C3")]
    margins = dk.DivEdgeInsets(left=24, right=24)
    text_color = "#ffffff"
    font_size = 14
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER


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
                        text='Empty state',
                    ),
                    Subtitle(
                        text='You can specify an empty state in the list of '
                             'possible states. In this case, when switching '
                             'to this state, the block will disappear.\n\nIn '
                             'the example, the button disappears when tapped.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivState(
                        id='sample',
                        states=[
                            dk.DivStateState(
                                state_id='visible',
                                div=TextBlock(
                                    text='Click to make this button invisible',
                                    actions=[
                                        dk.DivAction(
                                            log_id='switch_visible',
                                            url='div-action://set_state?'
                                                'state_id=0/sample/empty',
                                        ),
                                    ],
                                ),
                            ),
                            dk.DivStateState(
                                state_id='empty',
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
