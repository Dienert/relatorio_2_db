import React, { Component } from 'react';
import Plot from 'react-plotly.js'

class Grafico extends Component {
    constructor(props) {
        super(props);
    
        this.state = {dados: {x: [0], y: [0]}};
      }

    componentDidMount() {
        fetch(this.props.api)
          .then(res => res.json())
          .then(json => this.setState({ dados: json }));
      }

    render() {
        return (
          <div >
              <Plot
                data={[
                    {
                        type: this.props.graph_type,
                        mode: "lines+markers",
                        orientation: 'h',
                        x: this.state.dados.x,
                        y: this.state.dados.y,
                        marker: {color: 'rgb(55, 83, 109)'},
                    },
                ]}
                layout={ {title: this.props.title,
                            showlegend: false,
                            width: this.props.width, height: 400,
                            xaxis: {
                            title: this.props.x_axis_title,
                            autorange: true,
                            rangeslider: this.props.rangeslider,
                            type: this.props.x_data_type
                            },
                            yaxis: {
                            title: this.props.y_axis_title,
                            autorange: true,
                            tickfont: {
                              size: this.props.tick_font_size
                            },
                            range: [1, 24],
                            type: this.props.y_data_type
                            },
                        }
                        }/>
          </div>
        );
      }
    
}

export default Grafico;