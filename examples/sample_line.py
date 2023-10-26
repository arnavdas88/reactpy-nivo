from reactpy import component, html, run
from reactpy.backend.starlette import Options
from reactpy.backend.fastapi import configure

from reactpy_nivo.plot import ResponsiveLine, ResponsiveLineCanvas
from reactpy_nivo.line.types.generic import ThemeColor
from reactpy_nivo.line.types import Base, Margin, XScale, YScale
from reactpy_nivo.line.types import Grid, Axis, AxisLeft, AxisRight, AxisTop, AxisBottom, AxisModel
from reactpy_nivo.line.types import Style, Colors, Def, FillItem, InheritColor
from reactpy_nivo.line.types import Legend, Effect, EffectStyle
from reactpy_nivo.line.types import Point
from fastapi import FastAPI
from reactpy.core.types import VdomDict

import pandas as pd

df = pd.read_json("data/transportation.json")

@component
def HelloWorld() -> VdomDict:
    base = Base(
        data = df.to_dict(orient='records'),
        margin = Margin( top=50, right=130, bottom=50, left=60 ),
        xScale = XScale( type= 'point' ),
        yScale = YScale( type= 'linear' ),
        yFormat = " >-.2f"
    )
    axis = Axis(
        axisBottom = AxisModel(
            enable = True,
            tickSize = 5,
            tickPadding = 5,
            tickRotation = 0,
            legend = "Transportation",
            legendPosition = "middle",
            legendOffset = 32,
        ),
        axisLeft = AxisModel(
            enable = True,
            tickSize = 5,
            tickPadding = 5,
            tickRotation = 0,
            legend = "Count",
            legendPosition = "middle",
            legendOffset = -40,
        )
    ) 
    style = Style(
        colors = Colors(scheme = "nivo"), 
        enableArea = False
    )
    legend = Legend(
        dataFrom = 'keys',
        anchor = 'top-right',
        direction = 'column',
        justify = False,
        translateX = 120,
        translateY = 0,
        itemsSpacing = 2,
        itemWidth = 100,
        itemHeight = 20,
        itemDirection = 'left-to-right',
        itemOpacity = 0.35,
        symbolSize = 20,
        effects = [
            Effect( on = 'hover', style = EffectStyle(itemOpacity = 1, itemWidth = 60) )
        ]
    )
    point = Point(
        pointSize= 10,
        pointColor= ThemeColor(theme = 'background'),
        pointBorderWidth= 2,
        pointBorderColor= InheritColor(from_= 'serieColor' ),
        pointLabelYOffset= -12,
    )
    respbar_obj = ResponsiveLine(
        {
            **base.dict(exclude_none = True, by_alias=True),
            "useMesh": True,
            **style.dict(exclude_none = True, by_alias=True),
            **axis.dict(exclude_none = True, by_alias=True),
            "legends": [ legend.dict(exclude_none = True, by_alias=True) ],
            **point.dict(exclude_none = True, by_alias=True)
        }
    )
    return html.div(
        {"class": "nivo-plot"},
        respbar_obj
    )

description = """This is an example FastApi application that explains how 
`reactpy-nivo` can be used to create beautiful charts, easily and build 
industry ready dashboards, without actually using any frontend software
stack."""

app = FastAPI(
    title="ReactPy - Nivo",
    description=description,
    summary="A `Nivo Charts` component implemented in `ReactPy`",
    version="0.0.1",
    contact={
        "name": "Arnav Das",
        "url": "about.me/arnav-das",
        "email": "arnav.das88@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

options = Options()
options.head = (*options.head, html.style("div.nivo-plot > div{ height: 400px; width: 800px;  }"))
configure(app, HelloWorld, options=options)