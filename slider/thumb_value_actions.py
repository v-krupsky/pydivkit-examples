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
    variables=[
        dk.NumberVariable(
            name='text_alpha',
            value=0.5,
        ),
        dk.IntegerVariable(
            name='my_thumb_value',
            value=0,
        ),
    ],
    variable_triggers=[
        dk.DivTrigger(
            # Note the import statement!
            condition=Expr(v='@{my_thumb_value >= 0}'),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='change_text_alpha',
                    url='div-action://set_variable?name=text_alpha&value=@{'
                        'my_thumb_value}'
                ),
            ],
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
                        text='Actions when changing the slider value.',
                    ),
                    Subtitle(
                        text="The slider lets you track changes in the "
                             "selected value.\n\nIn the example, the slider "
                             "is used to set text transparency: a number in "
                             "the range from 0 to 1 is selected and when the "
                             "value changes, the 'alpha' field of the text is "
                             "updated.",
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        items=[
                            dk.DivImage(
                                image_url='https://yastatic.net/s3/home/divkit/oldbg.png',
                                width=dk.DivMatchParentSize(),
                                alpha=Expr(v='@{div(text_alpha, 255.0)}'),
                            ),
                            dk.DivSlider(
                                width=dk.DivMatchParentSize(),
                                paddings=dk.DivEdgeInsets(top=16, left=12,
                                                          right=12),
                                max_value=255,
                                min_value=0,
                                thumb_value_variable='my_thumb_value',
                                thumb_style=dk.DivShapeDrawable(
                                    color='#FFCC00',
                                    stroke=dk.DivStroke(
                                        color='#ffffff',
                                        width=3,
                                    ),
                                    shape=dk.DivRoundedRectangleShape(
                                        item_height=dk.DivFixedSize(value=32),
                                        item_width=dk.DivFixedSize(value=32),
                                        corner_radius=dk.DivFixedSize(value=100),
                                    ),
                                ),
                                track_active_style=dk.DivShapeDrawable(
                                    color='#FFCC00',
                                    shape=dk.DivRoundedRectangleShape(
                                        item_height=dk.DivFixedSize(value=6),
                                    ),
                                ),
                                track_inactive_style=dk.DivShapeDrawable(
                                    color='#20000000',
                                    shape=dk.DivRoundedRectangleShape(
                                        item_height=dk.DivFixedSize(value=6),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=16),
                        text='Slider with one pointer',
                        text_alignment_horizontal=dk.DivAlignmentHorizontal
                        .CENTER,
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
