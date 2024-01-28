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
    width = dk.DivWrapContentSize()
    height = dk.DivWrapContentSize()
    margins = dk.DivEdgeInsets(top=8, left=24, right=24)
    paddings = dk.DivEdgeInsets(top=4, bottom=4, left=8, right=8)
    background = [dk.DivSolidBackground(color='#0E000000')]
    text_color = '#000000'
    font_size = 14

    # According to the text in the DivKit documentation, this instruction should
    # be present, but it is not present in the example JSON.
    # font_size_unit = dk.DivSizeUnit.SP

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
                        text='Size units',
                    ),
                    Subtitle(
                        text="dp (density-independent pixels) are units that "
                             "are used by default and do not depend on the "
                             "screen density. Converts to pt on IOS, "
                             "dp on Android, and px in the web "
                             "interface\n\nsp (scale-independent pixels) are "
                             "units that depend on the font size factor of a "
                             "mobile device. Only used on Android.\n\npx are "
                             "pixels. They don't scale to the screen density, "
                             "so an element whose size is defined in pixels "
                             "will look different on screens with different "
                             "densities. Not supported in the web interface.",
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        items=[
                            TextBlock(
                                height=dk.DivFixedSize(value=30),
                                text='Height in dp, text in sp',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(
                                    value=30,
                                    unit=dk.DivSizeUnit.SP,
                                ),
                                # This text assumes that font_size_unit is
                                # set to dk.DivSizeUnit.SP
                                text='Height and text in sp',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(
                                    value=30,
                                    unit=dk.DivSizeUnit.SP,
                                ),
                                font_size_unit=dk.DivSizeUnit.DP,
                                text='Height in sp, text in dp',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(
                                    value=30,
                                ),
                                font_size_unit=dk.DivSizeUnit.DP,
                                text='Height and text in dp',
                            ),
                            TextBlock(
                                height=dk.DivFixedSize(
                                    value=100,
                                    unit=dk.DivSizeUnit.PX,
                                ),
                                font_size=40,
                                font_size_unit=dk.DivSizeUnit.PX,
                                text='Height is 100 px, text is 40 px',
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
