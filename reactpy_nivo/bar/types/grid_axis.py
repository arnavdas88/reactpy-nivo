from __future__ import annotations

from typing import Any, List, Optional, Union, Literal

from pydantic import BaseModel, Field

class AxisModel(BaseModel):
    enable: Optional[bool] = False
    tickSize: Optional[int] = 0
    tickPadding: Optional[int] = 0
    tickRotation: Optional[int] = 0
    legend: Optional[str] = 0
    legendPosition: Optional[Literal['start', 'middle', 'end']] = 'middle'
    legendOffset: Optional[int] = 0

class AxisTop(AxisModel):
    ...

class AxisBottom(AxisModel):
    ...

class AxisLeft(AxisModel):
    ...

class AxisRight(AxisModel):
    ...

class Grid(BaseModel):
    enableGridX: bool = False
    gridXValues: Optional[List[Union[int, str]]] = []
    enableGridY: bool = True
    gridYValues: Optional[List[Union[int, str]]] = []

class Axis(BaseModel):
    axisTop : Optional[AxisModel] = None
    axisBottom : Optional[AxisModel] = None
    axisLeft : Optional[AxisModel] = None
    axisRight : Optional[AxisModel] = None
