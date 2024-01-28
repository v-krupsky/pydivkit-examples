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


# Results in template 'animation_title'
class AnimationTitle(dk.DivText):
    __template_name__ = 'animation_title'
    font_weight = dk.DivFontWeight.BOLD
    font_size = 14
    paddings = dk.DivEdgeInsets(left=24, right=24, bottom=12, top=24)


# Results in template 'button'
class Button(dk.DivText):
    __template_name__ = 'button'
    paddings = dk.DivEdgeInsets(left=16, right=16, bottom=16, top=16)
    margins = dk.DivEdgeInsets(left=24, right=24)
    border = dk.DivBorder(corner_radius=8)
    background = [dk.DivSolidBackground(color='#0E000000')]
    font_size = 14
    font_weight = dk.DivFontWeight.MEDIUM
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_color = '#000000'


# Results in template 'in_out_transition_demo_block'
class InOutTransitionDemoBlock(dk.DivText):
    __template_name__ = 'in_out_transition_demo_block'
    height = dk.DivFixedSize(value=88)
    margins = dk.DivEdgeInsets(left=24, right=24, bottom=8)
    border = dk.DivBorder(corner_radius=16)
    background = [dk.DivSolidBackground(color='#3F28C3')]
    text_color = '#ffffff'
    font_size = 14
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER


# Prepare DivData object
data = dk.DivData(
    variables=[
        dk.StringVariable(
            name='change_state',
            value='none',
        ),
        dk.StringVariable(
            name='scale_state',
            value='visible'
        ),
        dk.StringVariable(
            name='slide_state',
            value='visible'
        ),
        dk.StringVariable(
            name='fade_state',
            value='visible'
        ),
        dk.StringVariable(
            name='set_state',
            value='visible'
        ),
    ],
    variable_triggers=[
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'scale' && scale_state == 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update scale_state',
                    url='div-action://set_variable?name=scale_state'
                        '&value=invisible'
                ),
            ]
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'scale' && scale_state != 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update scale_state',
                    url='div-action://set_variable?name=scale_state'
                        '&value=visible'
                ),
            ]
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'fade' && fade_state == 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update fade_state',
                    url='div-action://set_variable?name=fade_state'
                        '&value=invisible'
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'fade' && fade_state != 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update fade_state',
                    url='div-action://set_variable?name=fade_state'
                        '&value=visible'
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'slide' && slide_state == 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update slide_state',
                    url='div-action://set_variable?name=slide_state'
                        '&value=invisible'
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'slide' && slide_state != 'visible'}"
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    log_id='update slide_state',
                    url='div-action://set_variable?name=slide_state'
                        '&value=visible'
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'set' && set_state == 'visible'}",
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    # Should be set_state
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=set_state'
                        '&value=invisible'
                ),
            ],
        ),
        dk.DivTrigger(
            condition=Expr(
                v="@{change_state == 'set' && set_state == 'invisible'}",
            ),
            mode=dk.DivTriggerMode.ON_VARIABLE,
            actions=[
                dk.DivAction(
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=change_state&value=none'
                ),
                dk.DivAction(
                    # Should be set_state
                    log_id='update change_state flag',
                    url='div-action://set_variable?name=set_state&value=visible'
                ),
            ],
        ),
    ],
    log_id='sample_card',
    states=[
        dk.DivDataState(
            state_id=0,
            div=dk.DivContainer(
                orientation=dk.DivContainerOrientation.VERTICAL,
                margins=dk.DivEdgeInsets(top=24, bottom=24),
                items=[
                    Title(
                        text='Transition animations',
                    ),
                    Subtitle(
                        text='For each div, you can customize the transition '
                             'animation to be played when the div appears or '
                             'disappears.',
                    ),
                    AnimationTitle(
                        text='Scale',
                    ),
                    InOutTransitionDemoBlock(
                        id='scale_in_out',
                        text='Scale',
                        visibility=Expr(v="@{scale_state}"),
                        transition_out=dk.DivScaleTransition(
                            duration=1000,
                        ),
                        transition_in=dk.DivScaleTransition(
                            duration=1000,
                        ),
                    ),
                    Button(
                        alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                        text='Test Button',
                        actions=[
                            dk.DivAction(
                                log_id='set state',
                                url='div-action://set_variable'
                                    '?name=change_state&value=scale'
                            ),
                        ],
                    ),
                    AnimationTitle(
                        text='Slide',
                    ),
                    InOutTransitionDemoBlock(
                        id='slide_in_out',
                        text='Slide',
                        visibility=Expr(v="@{slide_state}"),
                        transition_out=dk.DivSlideTransition(
                            duration=1000,
                            edge=dk.DivSlideTransitionEdge.LEFT,
                        ),
                        transition_in=dk.DivSlideTransition(
                            duration=1000,
                            edge=dk.DivSlideTransitionEdge.RIGHT,
                        ),
                    ),
                    Button(
                        alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                        text='Test Button',
                        actions=[
                            dk.DivAction(
                                log_id='set state',
                                url='div-action://set_variable'
                                    '?name=change_state&value=slide'
                            ),
                        ],
                    ),
                    AnimationTitle(
                        text='Fade',
                    ),
                    InOutTransitionDemoBlock(
                        id='fade_in_out',
                        text='Fade',
                        visibility=Expr(v="@{fade_state}"),
                        transition_out=dk.DivFadeTransition(
                            duration=1000,
                        ),
                        transition_in=dk.DivFadeTransition(
                            duration=1000,
                        ),
                    ),
                    Button(
                        alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                        text='Test Button',
                        actions=[
                            dk.DivAction(
                                log_id='set state',
                                url='div-action://set_variable'
                                    '?name=change_state&value=fade'
                            ),
                        ],
                    ),
                    AnimationTitle(
                        text='Set',
                    ),
                    InOutTransitionDemoBlock(
                        id='set_in_out',
                        text='Set',
                        visibility=Expr(v="@{set_state}"),
                        transition_out=dk.DivAppearanceSetTransition(
                            items=[
                                dk.DivFadeTransition(
                                    duration=1000,
                                ),
                                dk.DivScaleTransition(
                                    duration=1000,
                                ),
                            ],
                        ),
                        transition_in=dk.DivAppearanceSetTransition(
                            items=[
                                dk.DivSlideTransition(
                                    duration=1000,
                                    edge=dk.DivSlideTransitionEdge.RIGHT,
                                ),
                                dk.DivFadeTransition(
                                    duration=1000,
                                ),
                            ],
                        ),
                    ),
                    Button(
                        alignment_horizontal=dk.DivAlignmentHorizontal.CENTER,
                        text='Test Button',
                        actions=[
                            dk.DivAction(
                                log_id='set state',
                                url='div-action://set_variable'
                                    '?name=change_state&value=set'
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
