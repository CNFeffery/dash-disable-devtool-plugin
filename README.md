# dash-disable-devtool-plugin

A plugin to disable browser developer tools and other page operation permissions for Dash applications using Dash Hooks. You can check out this project on PyPi at: https://pypi.org/project/dash-disable-devtool-plugin

## Installation

```bash
pip install dash-disable-devtool-plugin
```

## Usage

```python
from dash import Dash
# Import the disable devtool plugin
from dash_disable_devtool_plugin import setup_disable_devtool_plugin

# Enable the disable devtool plugin for the current app
setup_disable_devtool_plugin()

app = Dash(__name__)
# Rest of your app code...
```

## Example

Run the included example. In this basic example, first of all, the normal ways to open the browser developer tools via shortcut keys will be blocked. Even if the browser developer tools are opened through other means, it will be quickly detected, and trigger the default page content clearing and rewriting.

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## API Reference

### `setup_disable_devtool_plugin()`

This function sets up the disable-devtool plugin for your Dash application, preventing users from accessing browser developer tools.

| Parameter        | Type   | Default                                                                 | Description                                                                                                                                                                                                  |
| ---------------- | ------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `script_src`     | `str`  | `"https://cdn.jsdelivr.net/npm/disable-devtool"`                        | Source URL of the disable-devtool script. Alternative CDNs: `https://unpkg.com/disable-devtool/disable-devtool.min.js`, `https://registry.npmmirror.com/disable-devtool/latest/files/disable-devtool.min.js` |
| `disable_menu`   | `bool` | `False`                                                                 | Disables right-click context menu when `True`.                                                                                                                                                               |
| `disable_select` | `bool` | `False`                                                                 | Disables text selection when `True`.                                                                                                                                                                         |
| `disable_copy`   | `bool` | `False`                                                                 | Disables copy operations (Ctrl+C) when `True`.                                                                                                                                                               |
| `disable_cut`    | `bool` | `False`                                                                 | Disables cut operations (Ctrl+X) when `True`.                                                                                                                                                                |
| `disable_paste`  | `bool` | `False`                                                                 | Disables paste operations (Ctrl+V) when `True`.                                                                                                                                                              |
| `rewrite_html`   | `str`  | `"The current application disables debugging through developer tools."` | HTML content replacing the entire page when developer tools are detected.                                                                                                                                    |
