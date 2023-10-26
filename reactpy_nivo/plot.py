from pathlib import Path
from typing import Literal
from reactpy.web.module import export, module_from_file, module_from_url


_js_module = module_from_file(
    "nivo",
    file=Path(__file__).parent / "bundle.js",
    fallback="⏳",
)

ResponsiveBar = export(_js_module, "ResponsiveBar")
ResponsiveBarCanvas = export(_js_module, "ResponsiveBarCanvas")

ResponsiveLine = export(_js_module, "ResponsiveLine")
ResponsiveLineCanvas = export(_js_module, "ResponsiveLineCanvas")