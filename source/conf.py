import os

# Configuration file for Sphinx documentation

# -- Project information -----------------------------------------------------
project = "IOT Workshop"
author = "Hanzehogeschool"
copyright = "CC BY-NC-SA 4.0"
version = "1.2.0"
release = "1.2.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx_exercise",
    "sphinx_design",
    "sphinx.ext.mathjax",
    "sphinx_external_toc",
    "sphinxcontrib.video",
    "sphinx_immaterial"
]

external_toc_path = "_toc.yml"
language = "nl"

# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]

# -- MyST-NB configuration ---------------------------------------------------
nb_execution_mode = "cache"
nb_execution_timeout = 60

# -- HTML output options -----------------------------------------------------
html_theme = "sphinx_immaterial"
html_title = "IOT Workshop"
html_logo = "_static/logo_iot_dark.svg"

html_theme_options = {
    "repo_url": "https://github.com/hanze-hbo-ict/IOT",
    "repo_name": "IOT",
    "repo_type": "github",
    "edit_uri": "blob/main/source",

    # Optional: site icon
    # "icon": {
    #     "repo": "fontawesome/brands/github",
    # },

    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo-blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-7",
                "name": "Schakel naar dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo-blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-4",
                "name": "Schakel naar light mode",
            },
        },
    ],
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Voor GitHub Pages subpath
html_baseurl = os.environ.get("SPHINX_BASE_URL", "")