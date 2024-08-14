import streamlit as st
import plotly.graph_objects as go
import numpy as np

col1, col2 = st.columns([2, 2])

with col1:
    total_energy = 100
    renewable_energy = 4.67
    other_energy = total_energy - renewable_energy

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=renewable_energy,
        number={'valueformat': ".2f"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, renewable_energy], 'color': "green"},
                {'range': [renewable_energy, 100], 'color': "red"}],
            'threshold': {
                'line': {'color': "black", 'width': 5},
                'thickness': 0.75,
                'value': renewable_energy}}))

    fig_gauge.update_layout(
        title="Percentage of Renewable Energy<br>in Electricity Generation Mix",
        title_x=0,  # Center the title
        margin=dict(l=20, r=30, t=40, b=10),
        height=300,
    )

    renewable_energy_percentage = renewable_energy / total_energy * 100
    others_percentage = other_energy / total_energy * 100

    formatted_renewable_energy_percentage = f"{renewable_energy_percentage:.2f}"
    formatted_others_percentage = f"{others_percentage:.2f}"

    st.plotly_chart(fig_gauge)
    st.write("Total Generation Capacity: 29437 MW")
    st.write("Renewable Generation Capacity: 1374.76 MW")
    st.write("Non-Renewable Generation Capacity: 28062.24 MW")
with col2:
    technologies = ['Solar', 'Wind', 'Hydro', 'Biogas to Electricity', 'Biomass to Electricity']
    off_grid = [373.84, 2, 0, 0.69, 0.4]
    on_grid = [706.85, 60.9, 230, 0, 0]

    # Create a stacked bar chart using Plotly
    fig_bar = go.Figure()

    # Add Off-grid bars
    fig_bar.add_trace(go.Bar(
        x=technologies,
        y=off_grid,
        name='Off-grid',
        marker_color='blue'
    ))

    # Add On-grid bars
    fig_bar.add_trace(go.Bar(
        x=technologies,
        y=on_grid,
        name='On-grid',
        marker_color='orange'
    ))

    # Update layout for the stacked bar chart
    fig_bar.update_layout(
        barmode='stack',
        title='Renewable Energy Share',  # Center the title
        xaxis_title='Technology',
        yaxis_title='Total (MW)',
        xaxis_tickangle=-45,
        height=350,
        margin=dict(l=20, r=10, t=40, b=20)  # Ensure margins are consistent
    )

    # Display the bar chart
    st.plotly_chart(fig_bar, use_container_width=True)

# Display the results below the charts
