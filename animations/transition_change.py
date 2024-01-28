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


# Results in template 'image_block'
class ImageBlock(dk.DivImage):
    __template_name__ = 'image_block'
    image_url = ('https://yastatic.net/s3/home/yandex-app/div_demo/containers'
                 '.png')
    width = dk.DivFixedSize(value=150)
    height = dk.DivFixedSize(value=150)
    margins = dk.DivEdgeInsets(left=16, right=16, bottom=16)


# Results in template 'button'
class Button(dk.DivText):
    __template_name__ = 'button'
    width = dk.DivMatchParentSize()
    height = dk.DivWrapContentSize()
    paddings = dk.DivEdgeInsets(left=16, top=16, right=16, bottom=16)
    margins = dk.DivEdgeInsets(left=24, right=24)
    border = dk.DivBorder(corner_radius=8)
    background = [dk.DivSolidBackground(color='#0E000000')]
    font_size = 14
    font_weight = dk.DivFontWeight.MEDIUM
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = '#000000'


# Prepare DivData object
data = dk.DivData(
    log_id='sample_card',
    variables=[
        dk.BooleanVariable(
            name='change_state',
            value=False,
        ),
        dk.BooleanVariable(
            name='state',
            value=False,
        ),
    ],
    variable_triggers=[
        dk.DivTrigger(
            condition=Expr(v='@{change_state && state}'),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=change_state'
                        '&value=false',
                ),
                dk.DivAction(
                    # Note typo in log_id, should be 'update state variable'
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=state&value=false',
                ),
                dk.DivAction(
                    log_id='change state',
                    url='div-action://set_state?state_id=0'
                        '/transition_change_demo_state/state1',
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(v='@{change_state && !state}'),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=change_state'
                        '&value=false',
                ),
                dk.DivAction(
                    log_id='update state variable',
                    url='div-action://set_variable?name=state&value=true',
                ),
                dk.DivAction(
                    log_id='change state',
                    url='div-action://set_state?state_id=0'
                        '/transition_change_demo_state/state2',
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
                        text='Move and resize animations',
                    ),
                    Subtitle(
                        # Actually the image moves to the lower-right corner
                        text='For each div, you can customize the transition '
                             'animation to be played when the div changes its '
                             'size or position.\n\nIn the example, the picture '
                             'is animated to increase in width and moves to '
                             'the upper-right corner when switching to '
                             'state 2.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivState(
                        width=dk.DivMatchParentSize(),
                        height=dk.DivFixedSize(value=250),
                        id='transition_change_demo_state',
                        states=[
                            dk.DivStateState(
                                state_id='state1',
                                div=ImageBlock(
                                    id='image',
                                    alignment_horizontal=dk.
                                    DivAlignmentHorizontal.CENTER,
                                    alignment_vertical=dk.DivAlignmentVertical.
                                    TOP,
                                    width=dk.DivMatchParentSize(),
                                    transition_change=dk.
                                    DivChangeBoundsTransition(
                                        duration=1000,
                                    ),
                                ),
                            ),
                            dk.DivStateState(
                                state_id='state2',
                                div=ImageBlock(
                                    id='image',
                                    alignment_horizontal=dk.
                                    DivAlignmentHorizontal.RIGHT,
                                    alignment_vertical=dk.DivAlignmentVertical.
                                    BOTTOM,
                                    transition_change=dk.
                                    DivChangeBoundsTransition(
                                        duration=1000,
                                    ),
                                ),
                            ),
                        ],
                    ),
                    Button(
                        alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                        text='Test Button',
                        actions=[
                            dk.DivAction(
                                log_id='set_state1',
                                url='div-action://set_variable?name='
                                    'change_state&value=true',
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
