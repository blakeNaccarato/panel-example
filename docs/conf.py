"""Docs config."""

from datetime import date
from pathlib import Path

# ! Root
ROOT = Path(".")
DOCS = Path("docs")
"""Root directory of the project."""
# ! Paths
STATIC = DOCS / "_static"
"""Static assets folder, used in configs and setup."""
CSS = STATIC / "local.css"
"""Local CSS file, used in configs and setup."""
# ! Template answers
AUTHORS = "Blake Naccarato"
"""Authors of the project."""
USER = "blakeNaccarato"
"""Host GitHub user or organization for this repository."""
REPO = "panel-example"
"""GitHub repository name."""
PACKAGE = REPO
"""Package name."""
VERSION = "0.0.0"
"""Package version."""

# ! Setup


def dpaths(*paths: Path, rel: Path = DOCS) -> list[str]:
    """Get the string-representation of paths relative to docs for Sphinx config.

    Parameters
    ----------
    paths
        Paths to convert.
    rel
        Relative path to convert to. Defaults to the 'docs' directory.
    """
    return [dpath(path, rel) for path in paths]


def dpath(path: Path, rel: Path = DOCS) -> str:
    """Get the string-representation of a path relative to docs for Sphinx config.

    Parameters
    ----------
    path
        Path to convert.
    rel
        Relative path to convert to. Defaults to the 'docs' directory.
    """
    return path.relative_to(rel).as_posix()


# ! Basics
project = PACKAGE
copyright = f"{date.today().year}, {AUTHORS}"  # noqa: A001
version = VERSION
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extensions = ["myst_nb", "sphinx_thebe"]
# ! Theme
html_title = PACKAGE
# html_favicon = "_static/favicon.ico"
# html_logo = "_static/favicon.ico"
html_static_path = dpaths(STATIC)
html_css_files = dpaths(CSS, rel=STATIC)
html_theme = "sphinx_book_theme"
html_context = {
    # ? MyST elements don't look great with dark mode, but allow dark for accessibility.
    "default_mode": "light"
}
html_thebe_common: dict[str, str] = {
    "repository_url": f"https://github.com/{USER}/{REPO}",
    "path_to_docs": dpath(DOCS),
}
html_theme_options = {
    **html_thebe_common,
    "navigation_with_keys": False,  # https://github.com/pydata/pydata-sphinx-theme/pull/1503
    "repository_branch": "main",
    "show_navbar_depth": 2,
    "show_toc_level": 4,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "use_repository_button": True,
}
thebe_config = {
    **html_thebe_common,
    "repository_branch": "HEAD",
    "selector": "div.highlight",
}
# ! MyST
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 6
myst_substitutions = {}
# ! NB
nb_execution_raise_on_error = True
