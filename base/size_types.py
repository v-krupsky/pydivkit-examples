import pydivkit as dk
from pydivkit.core import Expr
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
    height = dk.DivWrapContentSize()
    margins = dk.DivEdgeInsets(top=8, left=24, right=24)
    paddings = dk.DivEdgeInsets(top=4, bottom=4, left=8, right=8)
    background = [dk.DivSolidBackground(color='#0E000000')]
    text_color = '#000000'
    font_size = 14
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
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
                        text='Sizing types',
                    ),
                    Subtitle(
                        text='match_parent: The size adjusts to the size of '
                             'the parent block\n\nwrap_content: The size '
                             'adjusts to the content\n\nfixed: The size is '
                             'fixed',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        items=[
                            TextBlock(
                                width=dk.DivWrapContentSize(),
                                text='This is wrap_content text',
                            ),
                            TextBlock(
                                width=dk.DivFixedSize(value=100),
                                text='This is fixed text that is 100dp wide',
                            ),
                            TextBlock(
                                width=dk.DivMatchParentSize(),
                                text='This is match_parent text',
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
