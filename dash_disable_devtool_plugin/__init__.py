import re
from dash import hooks


def setup_disable_devtool_plugin(
    script_src: str = "https://cdn.jsdelivr.net/npm/disable-devtool",
    disable_menu: bool = False,
    disable_select: bool = False,
    disable_copy: bool = False,
    disable_cut: bool = False,
    disable_paste: bool = False,
    rewrite_html: str = "The current application disables debugging through developer tools.",
):
    """Setup the disable devtool plugin

    Args:
        script_src (str, optional): The source link of the disable devtool script, other commonly used options include public CDN sources such as https://unpkg.com/disable-devtool/disable-devtool.min.js and https://registry.npmmirror.com/disable-devtool/latest/files/disable-devtool.min.js. Defaults to "https://cdn.jsdelivr.net/npm/disable-devtool".
        disable_menu (bool, optional): Disable the context menu. Defaults to False.
        disable_select (bool, optional): Disable text selection. Defaults to False.
        disable_copy (bool, optional): Disable copy. Defaults to False.
        disable_cut (bool, optional): Disable cut. Defaults to False.
        disable_paste (bool, optional): Disable paste. Defaults to False.
        rewrite_html (str, optional): The content of rewriting the page after triggering the browser developer tool detection. Defaults to "The current application disables debugging through developer tools.".
    """

    @hooks.index()
    def add_disable_devtool(app_index: str):
        # Extract the last line of the footer part
        match = re.findall("[ ]+</footer>", app_index)

        if match:
            # Add the disable devtool script
            app_index = app_index.replace(
                match[0],
                f"""<script src="{script_src}"></script>
<script type="application/javascript">
    // Enable disable devtool with options
    DisableDevtool(
        {{
            disableMenu: {str(disable_menu).lower()},
            disableSelect: {str(disable_select).lower()},
            disableCopy: {str(disable_copy).lower()},
            disableCut: {str(disable_cut).lower()},
            disablePaste: {str(disable_paste).lower()},
            rewriteHTML: "{rewrite_html}",
        }}
    )
</script>
"""
                + match[0],
            )

        return app_index
