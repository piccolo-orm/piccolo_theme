from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, \
    Number, Operator, Punctuation, String, Text


class RailscastsStyle(Style):
    """
    Port of the railscasts color scheme for Vim.
    """

    default_style = ''

    background_color = "#222"
    highlight_color = "#e6e1dc"

    styles = {
        Comment.Multiline:       "italic #bc9458",
        Comment.Preproc:         "bold #bc9469",
        Comment.Single:          "italic #bc9458",
        Comment.Special:         "bold italic #bc9469",
        Comment:                "italic #bc9458",
        Error:                  "#ffc66d",

        Keyword:                "#cc7833",
        Keyword.Reserved:       "#da4939",
        Keyword.Type:           "#5a647e",

        Name:                   "#fff",
        Name.Attribute:         "#da4939",
        Name.Builtin:           "#6d9cbe",
        Name.Builtin.Pseudo:    "#fff",
        Name.Class:             "#ffc66d",
        Name.Constant:          "#6d9cbe",
        Name.Decorator:         "#da4939",
        Name.Function:          "#ffc66d",
        Name.Tag:               "#e8bf6a",

        Number:                 "#a5c261",

        Operator:               "#fff",
        Operator.Word:          "#cc7833",

        Punctuation:            "#fff",

        String:                 "#a5c261",
        String.Escape:          "#da4939",

        Text:                   "#fff",
    }
