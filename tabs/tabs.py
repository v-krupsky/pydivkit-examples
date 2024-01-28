import pydivkit as dk
from pydivkit.core.fields import Expr
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    font_size = 28
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    width = dk.DivMatchParentSize()
    height = dk.DivFixedSize(value=184)
    background = [dk.DivSolidBackground(color="#0E000000")]
    border = dk.DivBorder(corner_radius=16)


# Results in template 'tab_container'
class TabContainer(dk.DivContainer):
    __template_name__ = 'tab_container'
    paddings = dk.DivEdgeInsets(left=16, right=16)


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
                        text='Tabs',
                    ),
                    Subtitle(
                        text='A set of tabs and a row with labels.\n\nOnly '
                             'one tab is visible at a time, the rest can be '
                             'switched by tapping the label of the respective '
                             'tab.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivTabs(
                        height=dk.DivWrapContentSize(),
                        tab_title_style=dk.DivTabsTabTitleStyle(
                            animation_type=dk.TabTitleStyleAnimationType.SLIDE,
                        ),
                        items=[
                            dk.DivTabsItem(
                                title='wrap_content',
                                div=TabContainer(
                                    items=[
                                        TextBlock(
                                            text='Item {}'.format(i),
                                            width=dk.DivMatchParentSize(),
                                        ),
                                    ],
                                ),
                            ) for i in range(4) # DivKit sample has 2 'Item 3's
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
