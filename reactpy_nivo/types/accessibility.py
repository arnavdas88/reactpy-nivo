from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple, Callable

from pydantic import BaseModel, Field, field_serializer, model_serializer

from .generic import ColorType, InheritColor, ThemeColor

class Accessibility(BaseModel):
    isFocusable : bool = False
    role : Optional[str] = None
    ariaLabel : Optional[str] = None
    ariaLabelledBy : Optional[str] = None
    ariaDescribedBy : Optional[str] = None
    barAriaLabel : Optional[Callable] = None
    barAriaLabelledBy : Optional[Callable] = None
    barAriaDescribedBy : Optional[Callable] = None
