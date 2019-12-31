"""ReStructured text knowledge for scriv."""

from scriv.format import FormatTools


class RstTools(FormatTools):
    """Specifics about how to work with ReStructured Text."""

    NEW_TEMPLATE = """\
        .. A new scriv entry.
        ..
        .. Uncomment the header that is right (remove the leading dots).
        ..
        {% for cat in config.categories -%}
        .. {{ cat }}
        .. {{ '=' * (cat|length) }}
        ..
        .. - A bullet item for the {{ cat }} category.
        ..
        {% endfor -%}
        """