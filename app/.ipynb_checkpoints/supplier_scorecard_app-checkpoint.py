import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Custom CSS
st.set_page_config(page_title="📦 Procurement Intelligence", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 10px; border-radius: 10px; border-left: 5px solid #004a99; }
    </style>
    """, unsafe_allow_html=True)

# 2. Data Loading
@st.cache_data
def load_data():
    # Adjusted path for local run vs root run
    try:
        df = pd.read_csv('data/processed/final_scorecard_2025.csv')
    except:
        df = pd.read_csv('../data/processed/final_scorecard_2025.csv')
    return df

scorecard = load_data()

# 3. Sidebar Navigation
category_filter = st.sidebar.multiselect(
    "Filter by Supplier Category",
    options=scorecard['Category'].unique(),
    default=scorecard['Category'].unique()
)

# Apply Filter
filtered_df = scorecard[scorecard['Category'].isin(category_filter)]

# 4. Executive KPI Row
st.title("Supplier Performance & Strategic Scorecard")

# Custom CSS for the "Card" look
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #004a99;
    }
    [data-testid="stMetricLabel"] {
        font-size: 16px;
        font-weight: bold;
        color: #333333;
    }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        border-left: 5px solid #004a99; /* D&S Blue Accent */
    }
    </style>
    """, unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Total Partners", len(filtered_df))
with kpi2:
    avg_score = filtered_df['Final_Score'].mean()
    st.metric("Avg Performance Score", f"{avg_score:.1f}/100")
with kpi3:
    # Filtering for scores below a 'B' grade (80)
    risk_count = len(filtered_df[filtered_df['Final_Score'] < 80])
    st.metric("At-Risk Suppliers", risk_count)
with kpi4:
    total_spend = filtered_df['Total_Spend'].sum()
    st.metric("Total Managed Spend", f"${total_spend:,.0f}")

st.markdown("---")

# 5. Visual Intelligence Layer
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Strategic Value vs. Reliability Matrix")

    avg_spend = filtered_df['Total_Spend'].mean()
    passing_score = 80  

    fig = px.scatter(
        filtered_df, 
        x="Total_Spend", 
        y="Final_Score", 
        size="Total_Orders", 
        color="Supplier_Tier",
        hover_name="Supplier",
        text="Supplier",
        color_discrete_map={
            'A (Strategic Partner)': '#2ecc71',
            'B (Preferred)': '#3498db',         
            'C (Active Monitoring)': '#f1c40f', 
            'F (Critical Risk / Re-Bid)': '#e74c3c'
        },
        labels={
            "Total_Spend": "Total Spend (USD)",
            "Final_Score": "Performance Score (0-100)"
        }
    )

    fig.add_vline(x=avg_spend, line_dash="dash", line_color="#666666", 
                  annotation_text="Avg Spend", annotation_font_color="white")
    fig.add_hline(y=passing_score, line_dash="dash", line_color="#666666", 
                  annotation_text="Target Score (80)", annotation_font_color="white")

    fig.update_traces(
        textposition='top center', 
        marker=dict(line=dict(width=1, color='white'))
    )

    fig.update_layout(
        template="plotly_dark",   
        plot_bgcolor="#0E1117",  
        paper_bgcolor="#0E1117",
        font_color="white",       
        xaxis=dict(showgrid=True, gridcolor='#262730'), 
        yaxis=dict(showgrid=True, gridcolor='#262730'),
        legend_title_font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Supplier Tier Distribution")

    fig2 = px.pie(
        filtered_df, 
        names="Supplier_Tier", 
        hole=0.4, # Creates the "Donut" look
        color="Supplier_Tier",
        color_discrete_map={
            'A (Strategic Partner)': '#2ecc71',
            'B (Preferred)': '#3498db',
            'C (Active Monitoring)': '#f1c40f',
            'F (Critical Risk / Re-Bid)': '#e74c3c'
        }
    )

    # Dark Mode Styling Polish
    fig2.update_traces(
        textinfo='percent+label', 
        textfont_size=12,
        marker=dict(line=dict(color='#0E1117', width=2)) # Dark gap between slices
    )

    fig2.update_layout(
        template="plotly_dark",
        plot_bgcolor="#0E1117",
        paper_bgcolor="#0E1117",
        font_color="white",
        showlegend=False, # Hiding legend to save space since labels are on the chart
        margin=dict(t=30, b=0, l=0, r=0)
    )

    st.plotly_chart(fig2, use_container_width=True)

# 6. Detailed Action Registry
st.subheader("Partner Performance Detail")
st.dataframe(
    filtered_df[['Supplier', 'Category', 'Final_Score', 'Supplier_Tier', 'Avg_OTD_Rate', 'Avg_Price_Variance', 'Risk_Alert']].sort_values('Final_Score', ascending=False),
    use_container_width=True,
    hide_index=True
)

# 7. Strategic Insight Footer
st.markdown("""
    <div style="
        background-color: #161b22; 
        border-left: 5px solid #2ecc71; 
        padding: 20px; 
        border-radius: 5px;
        margin-top: 20px;">
        <h4 style="color: #2ecc71; margin-top: 0;"> Strategic Insight</h4>
        <p style="color: #c9d1d9; font-size: 16px; margin-bottom: 0;">
            <b>Internal Brands (Dayliff)</b> currently maintain <b>0% price variance</b>, 
            acting as the primary hedge against OEM price creep.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 | Developed by Aklilu Abera | Supply Chain Data Analyst")
