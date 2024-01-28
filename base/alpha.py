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
    states=[
        dk.DivDataState(
            state_id=0,
            div=dk.DivContainer(
                orientation=dk.DivContainerOrientation.VERTICAL,
                margins=dk.DivEdgeInsets(top=24, bottom=24),
                items=[
                    Title(
                        text='Transparency',
                    ),
                    Subtitle(
                        text='You can set the transparency for any div: from '
                             '0 to 1',
                        margins=dk.DivEdgeInsets(bottom=12),
                    ),
                    dk.DivContainer(
                        orientation=dk.DivContainerOrientation.VERTICAL,
                        margins=dk.DivEdgeInsets(bottom=12),
                        items=[
                            dk.DivImage(
                                height=dk.DivFixedSize(value=200),
                                image_url='https://yastatic.net/s3/home'
                                          '/yandex-app/div_demo/containers.png',
                            ),
                            dk.DivImage(
                                height=dk.DivFixedSize(value=200),
                                alpha=0.5,
                                image_url='https://yastatic.net/s3/home'
                                          '/yandex-app/div_demo/containers.png',
                            ),
                        ],
                    ),
                    Subtitle(
                        text='The transparency of the first image is 1 and '
                             'the second is 0.5.',
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
