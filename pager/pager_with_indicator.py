import pydivkit as dk
import json


# Results in template 'text_block'
class TextBlock(dk.DivText):
    __template_name__ = 'text_block'
    font_size = 14
    text_alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    alignment_horizontal = dk.DivContentAlignmentHorizontal.CENTER
    paddings = dk.DivEdgeInsets(top=4, bottom=4, left=8, right=8)
    width = dk.DivMatchParentSize()
    height = dk.DivMatchParentSize()
    background = [dk.DivSolidBackground(color='#f1f1f1')]
    border = dk.DivBorder(corner_radius=16)


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
                        text='Pager',
                    ),
                    Subtitle(
                        text='A pager displays a horizontal set of cards, '
                             'where the main card is fully visible and the '
                             'neighboring ones are partially '
                             'displayed.\n\nYou can use it with an indicator '
                             'to show which card is selected.\n\nAn indicator '
                             'is also a div and can be positioned '
                             'independently of a pager.\n\nThe example shows '
                             'a pager with ten cards and an indicator on top.',
                        margins=dk.DivEdgeInsets(bottom=24),
                    ),
                    dk.DivContainer(
                        items=[
                            dk.DivIndicator(
                                active_item_color='#000000',
                                active_item_size=1.5,
                                height=dk.DivFixedSize(value=10),
                                margins=dk.DivEdgeInsets(top=10, bottom=10),
                                # The sample from DivKit documentation contains
                                # an error in the space_between_centers
                                # definition and the instruction is being
                                # ignored during render. You can remove the
                                # line below to see that the indicator looks
                                # exactly the same.
                                # The correct definition is:
                                space_between_centers=dk.DivFixedSize(value=15),
                                inactive_item_color='#D0D1D9',
                                pager_id='pager_with_indicator',
                                shape=dk.DivRoundedRectangleShape(
                                    corner_radius=dk.DivFixedSize(value=2),
                                    item_height=dk.DivFixedSize(value=2),
                                    item_width=dk.DivFixedSize(value=10),
                                ),
                            ),
                            dk.DivPager(
                                id='pager_with_indicator',
                                item_spacing=dk.DivFixedSize(value=10),
                                height=dk.DivFixedSize(value=300),
                                items=[
                                    TextBlock(
                                        text='Item {}'.format(i),
                                    )
                                    for i in range(11)
                                ],
                                layout_mode=dk.DivNeighbourPageSize(
                                    neighbour_page_width=dk.DivFixedSize(
                                        value=16),
                                ),
                                paddings=dk.DivEdgeInsets(right=4, left=4),
                            ),
                        ]
                    )
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
