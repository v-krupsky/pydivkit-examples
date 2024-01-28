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


# Results in template 'control_button'
class ControlButton(dk.DivImage):
    __template_name__ = 'control_button'
    scale = dk.DivImageScale.FIT
    aspect = dk.DivAspect(
        ratio=1,
    )
    width = dk.DivFixedSize(value=44)


# Prepare DivData object
data = dk.DivData(
    log_id='sample_card',
    variables=[
        dk.IntegerVariable(
            name='video_time',
            value=0,
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
                        text='Video',
                    ),
                    Subtitle(
                        text='A video player capable of playing a video '
                             'sequence from a file or a streaming video '
                             'received by URL. Depending on the parameters, '
                             'the video can start automatically, be looped or '
                             'run muted.\n\nIn this example, the slider '
                             'displays and changes the variable of the current '
                             'playback time. The rewind button sets the value '
                             'of the time variable to 0, and the play and '
                             'pause buttons call the corresponding actions.',
                        margins=dk.DivEdgeInsets(bottom=24),
                        ranges=[
                            dk.DivTextRange(
                                start=286,
                                end=292,
                                font_weight=dk.DivFontWeight.BOLD,
                            ),
                            dk.DivTextRange(
                                start=350,
                                end=354,
                                font_weight=dk.DivFontWeight.BOLD,
                            ),
                            dk.DivTextRange(
                                start=359,
                                end=364,
                                font_weight=dk.DivFontWeight.BOLD,
                            ),
                        ],
                    ),
                    dk.DivVideo(
                        id='bears_video',
                        video_sources=[
                            dk.DivVideoSource(
                                url='https://yastatic.net/s3/home/divkit/'
                                    'bears.mp4',
                                mime_type='video/mp4',
                            ),
                        ],
                        preload_required=True,
                        repeatable=False,
                        autostart=False,
                        muted=True,
                        elapsed_time_variable='video_time',
                        height=dk.DivFixedSize(value=320),
                        background=[dk.DivSolidBackground(color='#000000')],
                    ),
                    Subtitle(
                        width=dk.DivMatchParentSize(),
                        text_alignment_horizontal=dk.DivAlignmentHorizontal
                        .CENTER,
                        text='Time elapsed: @{video_time}ms',
                    ),
                    dk.DivSlider(
                        width=dk.DivMatchParentSize(),
                        margins=dk.DivEdgeInsets(top=16, left=12, right=12),
                        max_value=30000,
                        min_value=0,
                        thumb_value_variable='video_time',
                        thumb_style=dk.DivShapeDrawable(
                            color='#FFCC00',
                            stroke=dk.DivStroke(
                                color='#ffffff',
                                width=3,
                            ),
                            shape=dk.DivRoundedRectangleShape(
                                item_height=dk.DivFixedSize(value=32),
                                item_width=dk.DivFixedSize(value=32),
                                corner_radius=dk.DivFixedSize(value=16),
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
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.HORIZONTAL,
                        width=dk.DivMatchParentSize(),
                        height=dk.DivWrapContentSize(),
                        content_alignment_horizontal=dk.
                        DivContentAlignmentHorizontal.CENTER,
                        items=[
                            ControlButton(
                                image_url='https://yastatic.net/s3/home/divkit'
                                          '/rewind_button.png',
                                margins=dk.DivEdgeInsets(right=20),
                                actions=[
                                    dk.DivAction(
                                        log_id='rewind',
                                        url='div-action://set_variable?'
                                            'name=video_time&value=0',
                                    ),
                                ],
                            ),
                            ControlButton(
                                image_url='https://yastatic.net/s3/home/divkit'
                                          '/play_button.png',
                                margins=dk.DivEdgeInsets(right=15),
                                paddings=dk.DivEdgeInsets(top=3, bottom=3),
                                actions=[
                                    dk.DivAction(
                                        log_id='play',
                                        url='div-action://video?id=bears_video'
                                            '&action=start'
                                    ),
                                ],
                            ),
                            ControlButton(
                                image_url='https://yastatic.net/s3/home/divkit'
                                          '/pause_button.png',
                                paddings=dk.DivEdgeInsets(top=3, bottom=3),
                                actions=[
                                    dk.DivAction(
                                        log_id='pause',
                                        url='div-action://video?id=bears_video'
                                            '&action=pause'
                                    ),
                                ],
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
