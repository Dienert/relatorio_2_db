import React, { Component } from 'react';
import Grafico from './Grafico'

class Relatorio extends Component {

    render() {
        return (
          <div>
            <Grafico api='http://localhost:5000/vendasanuais'
                title="Vendas por ano"
                width={650}
                x_axis_title="Anos"
                y_axis_title="Vendas ($)"
                x_data_type="date"
                graph_type="scatter"
                rangeslider={{}}
            />
            <br />
            <Grafico api='http://localhost:5000/vendasmensais'
                title="Vendas por mês"
                width={650}
                x_axis_title="Mês"
                y_axis_title="Vendas ($)"
                x_data_type="date"
                graph_type="scatter"
                rangeslider={{}}
            />
            <Grafico api='http://localhost:5000/vendaspordia'
                title="Vendas por dia da semana"
                width={650}
                x_axis_title="Dia da Semana"
                y_axis_title="Vendas ($)"
                x_data_type="category"
                graph_type="scatter"
                rangeslider={{}}
            />
            <Grafico api='http://localhost:5000/vendasporhora'
                title="Vendas por Hora do Dia"
                width={650}
                x_axis_title="Hora do Dia"
                y_axis_title="Vendas ($)"
                x_data_type="category"
                graph_type="scatter"
                rangeslider={{}}                
            />
            <Grafico api='http://localhost:5000/produtosmaiscomprados'
                title="10 Produtos Mais Comprados"
                width={400}
                x_axis_title="Frequência"
                y_data_type="category"
                graph_type="bar"
                tick_font_size={9.5}
            />
            <Grafico api='http://localhost:5000/produtosmaiorreceita'
                title="10 Produtos de Maior Receita"
                width={400}
                x_axis_title="Receita"
                y_data_type="category"
                graph_type="bar"
                tick_font_size={9.5}
            />
            <Grafico api='http://localhost:5000/clientesmaisfrequentes'
                title="10 Clientes Mais Frequentes"
                width={400}
                x_axis_title="Frequência"
                y_data_type="category"
                graph_type="bar"
                tick_font_size={9.5}
            />
            <Grafico api='http://localhost:5000/clientesmaiscompram'
                title="10 Clientes que mais compram"
                width={400}
                x_axis_title="Soma das compras ($)"
                y_data_type="category"
                y_title_standoff={25}
                graph_type="bar"
                tick_font_size={9.5}
            />
          </div>
        );
      }
    
}

export default Relatorio;