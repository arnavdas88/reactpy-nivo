import React from "react";
import ReactDOM from "react-dom";
import htm from "htm";

export * from '@nivo/bar'
export * from '@nivo/line'

const html = htm.bind(React.createElement);

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

