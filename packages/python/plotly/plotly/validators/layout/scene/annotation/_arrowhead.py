import _plotly_utils.basevalidators


class ArrowheadValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self, plotly_name="arrowhead", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowheadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 8),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
