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


# Results in template 'button'
class Button(dk.DivText):
    __template_name__ = 'button'
    background_color: str = dk.Field()
    height = dk.DivFixedSize(value=48)
    margins = dk.DivEdgeInsets(left=16, right=16, bottom=16)
    border = dk.DivBorder(corner_radius=16)
    background = [dk.DivSolidBackground(color=dk.Ref(background_color))]
    font_size = 14
    font_weight = dk.DivFontWeight.MEDIUM
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
                        text='Tap animations',
                    ),
                    Subtitle(
                        text='If a div has at least one tap action specified, '
                             'you can set a tap animation.\n\nFade, scale, '
                             'and a combination of fade and scale animations '
                             'are supported.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    Button(
                        background_color='#00B341',
                        text='Fade',
                        text_color='#000000',
                        actions=[
                            dk.DivAction(
                                log_id='fade_button_press',
                                url='div-action://animation/fade',
                            ),
                        ],
                        action_animation=dk.DivAnimation(
                            name=dk.DivAnimationName.FADE,
                            start_value=1,
                            end_value=0.4,
                            duration=500,
                            interpolator=dk.DivAnimationInterpolator.
                            EASE_IN_OUT,
                        ),
                    ),
                    Button(
                        background_color='#0077FF',
                        text_color='#ffffff',
                        text='Scale',
                        actions=[
                            dk.DivAction(
                                log_id='scale_button_press',
                                url='div-action://animation/scale',
                            ),
                        ],
                        action_animation=dk.DivAnimation(
                            name=dk.DivAnimationName.SCALE,
                            start_value=1,
                            end_value=0.4,
                            duration=500,
                            interpolator=dk.DivAnimationInterpolator.
                            EASE_IN_OUT,
                        ),
                    ),
                    Button(
                        background_color='#FFCC00',
                        text='Set',
                        text_color='#000000',
                        actions=[
                            dk.DivAction(
                                log_id='set_button_press',
                                url='div-action://animation/set',
                            ),
                        ],
                        action_animation=dk.DivAnimation(
                            name=dk.DivAnimationName.SET,
                            items=[
                                dk.DivAnimation(
                                    name=dk.DivAnimationName.FADE,
                                    start_value=1,
                                    end_value=0.2,
                                    duration=300,
                                    interpolator=dk.DivAnimationInterpolator.
                                    EASE_IN_OUT,
                                ),
                                dk.DivAnimation(
                                    name=dk.DivAnimationName.SCALE,
                                    start_value=1,
                                    end_value=0.5,
                                    duration=500,
                                    interpolator=dk.DivAnimationInterpolator.
                                    EASE_IN_OUT,
                                ),
                            ],
                        ),
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
