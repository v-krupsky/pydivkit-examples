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


# Prepare DivData object
data = dk.DivData(
    log_id='sample_card',
    variables=[
        dk.IntegerVariable(
            name='first_thumb_value',
            value=6,
        ),
        dk.IntegerVariable(
            name='second_thumb_value',
            value=3,
        ),
        dk.IntegerVariable(
            name='second_thumb_secondary_value',
            value=8,
        ),
        dk.IntegerVariable(
            name='third_thumb_value',
            value=6,
        ),
        dk.IntegerVariable(
            name='fourth_thumb_value',
            value=6,
        ),
        dk.IntegerVariable(
            name='fifth_thumb_value',
            value=6,
        ),
        dk.IntegerVariable(
            name='sixth_thumb_value',
            value=6,
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
                        text='Slider.',
                    ),
                    Subtitle(
                        text='A scale where you can select values from a '
                             'range. It can have one or two pointers.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    Subtitle(
                        text='Slider with one pointer',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        paddings=dk.DivEdgeInsets(left=8, right=8),
                        max_value=10,
                        min_value=1,
                        thumb_value_variable='first_thumb_value',
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
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=24),
                        text='Slider with two pointers',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        max_value=10,
                        min_value=1,
                        thumb_value_variable='second_thumb_value',
                        thumb_secondary_value_variable='second_thumb_secondary_value',
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
                        paddings=dk.DivEdgeInsets(left=8, right=8),
                        thumb_secondary_style=dk.DivShapeDrawable(
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
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=24),
                        text='Slider with ticks',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        max_value=10,
                        min_value=1,
                        paddings=dk.DivEdgeInsets(left=12, right=12),
                        thumb_value_variable='third_thumb_value',
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
                        tick_mark_active_style=dk.DivShapeDrawable(
                            color='#FFCC00',
                            stroke=dk.DivStroke(
                                color='#ffffff',
                                width=2,
                            ),
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=8),
                                item_width=dk.DivFixedSize(value=8),
                                corner_radius=dk.DivFixedSize(value=5),
                            ),
                        ),
                        tick_mark_inactive_style=dk.DivShapeDrawable(
                            color='#20000000',
                            stroke=dk.DivStroke(
                                color='#ffffff',
                                width=2,
                            ),
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=8),
                                item_width=dk.DivFixedSize(value=8),
                                corner_radius=dk.DivFixedSize(value=5),
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
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=24),
                        text='Slider with a modified style for the active '
                             'scale',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        max_value=10,
                        min_value=1,
                        paddings=dk.DivEdgeInsets(left=10, right=10),
                        thumb_value_variable='fourth_thumb_value',
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
                            color='#3F28C3',
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=10),
                                corner_radius=dk.DivFixedSize(value=2),
                            ),
                        ),
                        track_inactive_style=dk.DivShapeDrawable(
                            color='#20000000',
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=6),
                            ),
                        ),
                    ),
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=24),
                        text='Slider with a modified pointer style',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        margins=dk.DivEdgeInsets(top=16, left=20, right=20),
                        max_value=10,
                        min_value=1,
                        thumb_value_variable='fifth_thumb_value',
                        thumb_style=dk.DivShapeDrawable(
                            color='#FFCC00',
                            stroke=dk.DivStroke(
                                color='#ffffff',
                                width=3,
                            ),
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=32),
                                item_width=dk.DivFixedSize(value=12),
                                corner_radius=dk.DivFixedSize(value=12),
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
                    Subtitle(
                        margins=dk.DivEdgeInsets(top=24),
                        text='Slider with a selected value on the pointer',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        margins=dk.DivEdgeInsets(top=16, left=10, right=10),
                        max_value=10,
                        min_value=1,
                        thumb_value_variable='sixth_thumb_value',
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
                        thumb_text_style=dk.DivSliderTextStyle(
                            font_size=12,
                            font_weight=dk.DivFontWeight.BOLD,
                            text_color='#ffffff',
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
