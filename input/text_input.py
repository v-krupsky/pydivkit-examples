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


# Results in template 'input_text_borderless'
class InputTextBorderless(dk.DivInput):
    __template_name__ = 'input_text_borderless'
    width = dk.DivMatchParentSize()
    height = dk.DivMatchParentSize()
    margins = dk.DivEdgeInsets(left=16, top=20, right=16, bottom=16)
    paddings = dk.DivEdgeInsets(left=16, top=10, right=16, bottom=10)
    alignment_horizontal = dk.DivAlignmentHorizontal.LEFT
    alignment_vertical = dk.DivAlignmentVertical.CENTER
    font_size = 16
    font_weight = dk.DivFontWeight.MEDIUM
    text_color = "#000000"
    hint_color = '#888888'
    highlight_color = '#e0bae3'
    line_height = 22


# Results in template 'input_text'
class InputText(InputTextBorderless):
    __template_name__ = 'input_text'
    background = [dk.DivSolidBackground(color='#0e000000')]
    border = dk.DivBorder(corner_radius=8)


# Results in template 'output_text'
class OutputText(dk.DivText):
    __template_name__ = 'output_text'
    width = dk.DivMatchParentSize()
    height = dk.DivWrapContentSize()
    paddings = dk.DivEdgeInsets(left=24, right=24, bottom=16)
    alpha = 1
    alignment_horizontal = dk.DivAlignmentHorizontal.CENTER
    alignment_vertical = dk.DivAlignmentVertical.CENTER
    font_size = 16
    font_weight = dk.DivFontWeight.MEDIUM
    text_alignment_horizontal = dk.DivAlignmentHorizontal.LEFT
    text_alignment_vertical = dk.DivAlignmentVertical.CENTER
    text_color = "#000000"



# Prepare DivData object
data = dk.DivData(
    log_id='sample_card',
    variables=[
        dk.StringVariable(
            name='my_single_text',
            value='This is single-line input',
        ),
        dk.StringVariable(
            name='my_multi_text',
            value='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                  'sed do eiusmodtempor incididunt ut labore et dolore magna '
                  'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                  'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                  'Duis aute irure dolor in reprehenderit in voluptate velit '
                  'esse cillum dolore eu fugiat nulla pariatur.',
        ),
        dk.StringVariable(
            name='my_borderless_text',
            value='',
        ),
        dk.StringVariable(
            name='my_email_text',
            value='',
        ),
        dk.StringVariable(
            name='my_number_text',
            value='',
        ),
        dk.StringVariable(
            name='my_focus_text',
            value='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                  'sed do eiusmodtempor incididunt ut labore et dolore magna '
                  'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                  'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
                  'Duis aute irure dolor in reprehenderit in voluptate velit '
                  'esse cillum dolore eu fugiat nulla pariatur.',
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
                        text='Text inputs',
                    ),
                    Subtitle(
                        text='You can input your own data and interact with '
                             'it.',
                    ),
                    InputText(
                        text_variable='my_single_text',
                        keyboard_type=dk.DivInputKeyboardType.SINGLE_LINE_TEXT,
                    ),
                    OutputText(
                        text='Text: @{my_single_text}',
                        ranges=[
                            dk.DivTextRange(
                                start=0,
                                end=5,
                                text_color='#777777'
                            )
                        ]
                    ),
                    Subtitle(
                        text='The input can consist of either one or multiple '
                             'lines.',
                    ),
                    InputText(
                        text_variable='my_multi_text',
                    ),
                    Subtitle(
                        text='The input text can also be presented in a '
                             'format of an underlined text.'
                    ),
                    InputTextBorderless(
                        hint_text='This is borderless text',
                        native_interface=dk.DivInputNativeInterface(
                            color='#000000'),
                        text_variable='my_borderless_text',
                    ),
                    Subtitle(
                        text='There are multiple types of keyboard inputs, '
                             'for example, for numbers, phones, e-mails etc.',
                    ),
                    InputText(
                        keyboard_type=dk.DivInputKeyboardType.EMAIL,
                        text_variable='my_email_text',
                        hint_text='This is input for e-mails',
                    ),
                    InputText(
                        keyboard_type=dk.DivInputKeyboardType.NUMBER,
                        text_variable='my_number_text',
                        hint_text='This is input for numbers',
                    ),
                    Subtitle(
                        text='There are also different features, such as '
                             'changing color of text, changing spacing '
                             'between lines and symbols or making the whole '
                             'text selected on tapping.',
                    ),
                    Subtitle(
                        text='The following text will be selected fully when '
                             'focused.',
                    ),
                    InputText(
                        text_variable='my_focus_text',
                        select_all_on_focus=True,
                        line_height=32,
                        letter_spacing=2,
                        text_color='#FF0000',
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
