from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple

from pydantic import BaseModel, Field, field_serializer, model_serializer

CATEGORICAL_COLORS = [
    "nivo",	
    "category10",	
    "accent",	
    "dark2",	
    "paired",	
    "pastel1",	
    "pastel2",	
    "set1",	
    "set2",	
    "set3",
]

DIVERGING_COLORS = [
    "brown_blueGreen",	
    "purpleRed_green",	
    "pink_yellowGreen",	
    "purple_orange",	
    "red_blue",	
    "red_grey",	
    "red_yellow_blue",	
    "red_yellow_green",	
    "spectral",
]

SEQUENTIAL_COLORS = [
    "blues",
    "greens",
    "greys",
    "oranges",
    "purples",
    "reds",
    "blue_green",
    "blue_purple",
    "green_blue",
    "orange_red",
    "purple_blue_green",
    "purple_blue",
    "purple_red",
    "red_purple",
    "yellow_green_blue",
    "yellow_green",
    "yellow_orange_brown",
    "yellow_orange_re",
]

ColorScheme = Literal[*CATEGORICAL_COLORS, *DIVERGING_COLORS, *SEQUENTIAL_COLORS]
Modifiers = List[Tuple[Literal['darker', 'brighter', 'opacity'], float]]
Anchors = Literal['top-left', 'top', 'top-right', 'left', 'center', 'right', 'bottom-left', 'bottom', 'bottom-right']
Direction = Literal['row', 'column']
ItemDirection = Literal['left-to-right', 'right-to-left', 'top-to-bottom', 'bottom-to-top']

class InheritColor(BaseModel):
    from_: str = Field(..., serialization_alias='from')
    modifiers: Modifiers

class ThemeColor(BaseModel):
    theme : Literal['background', 'grid.line.stroke', 'labels.text.fill']

ColorType = Union[InheritColor, ThemeColor, str]