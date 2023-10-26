from __future__ import annotations

from typing import Any, List, Optional, Union, Literal

from pydantic import BaseModel, Field

class Margin(BaseModel):
    top: float
    right: float
    bottom: float
    left: float

class XScale(BaseModel):
    type: Literal['linear', 'point']

class YScale(BaseModel):
    type: Literal['linear', 'point']
    min: Optional[Union[float, Literal['auto']]] = "auto"
    max: Optional[Union[float, Literal['auto']]] = "auto"
    stacked: Optional[bool] = True
    reverse: Optional[bool] = False

class Base(BaseModel):
    data: Any
    xScale: Optional[XScale] = None
    xFormat: Optional[str] = None
    yScale: Optional[YScale] = None
    yFormat: Optional[str] = None

    height: Optional[float] = None
    width: Optional[float] = None
    pixelRatio: Optional[float] = None
    margin: Optional[Margin] = None