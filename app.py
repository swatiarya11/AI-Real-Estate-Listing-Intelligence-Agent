import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Real Estate Intelligence",
    page_icon="🏠",
    layout="wide"
)

WEBHOOK_URL = "http://localhost:5678/webhook/analyze-listings"

SHEET_ID = "1oP7XKv1DcGoB4iFJjXhRjyeau1Wq0E-Dhwxbe85pslg"

CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/"
    f"{SHEET_ID}/gviz/tq?tqx=out:csv"
)

# =====================================================
# LOAD GOOGLE SHEET
# =====================================================

@st.cache_data(ttl=10)
def load_sheet():
    try:
        df = pd.read_csv(CSV_URL)

        if "Title" in df.columns:
            df = df.drop_duplicates(
                subset=["Title"],
                keep="last"
            )
            
            df = df.reset_index(drop=True)
            
        return df

    except Exception as e:
        st.error(f"Failed to load Google Sheet: {e}")
        return pd.DataFrame()


df = load_sheet()

# =====================================================
# LOGIN
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🏠 AI Real Estate Listing Intelligence Agent")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == "admin"
            and password == "admin123"
        ):
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Listings",
        "AI Analysis",
        "Alerts",
        "Google Sheets",
        "About"
    ]
)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.title("🏠 AI Real Estate Listing Intelligence Agent")

    Properties_Logged = len(df)

    Premium_Properties = 0
    avg_score = 0

    if (
        not df.empty
        and "Investment_Score" in df.columns
    ):

        df["Investment_Score"] = pd.to_numeric(
            df["Investment_Score"],
            errors="coerce"
        )

        Premium_Properties = len(
            df[df["Investment_Score"] >= 8]
        )

        avg_score = round(
            df["Investment_Score"].mean(),
            1
        )

    last_run = "N/A"

    if (
        not df.empty
        and "Timestamp" in df.columns
    ):
        last_run = str(
            df["Timestamp"].iloc[-1]
        )[:10]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Properties Logged",
        Properties_Logged
    )

    col2.metric(
        "Premium Properties",
        Premium_Properties
    )

    col3.metric(
        "Average Score",
        avg_score
    )

    col4.metric(
        "Last Run",
        last_run
    )

    st.divider()

    if st.button("🚀 Run Analysis Pipeline"):

        try:

            response = requests.post(
                WEBHOOK_URL,
                timeout=30
            )

            if response.status_code == 200:

                st.success(
                    "Workflow executed successfully"
                )

                st.info(
                    f"Executed at "
                    f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
                )

                st.cache_data.clear()
                st.rerun()

            else:
                st.error(
                    f"Workflow failed "
                    f"({response.status_code})"
                )

        except Exception as e:
            st.error(str(e))

    st.subheader("Investment Score Distribution")

    if (
        not df.empty
        and "Investment_Score" in df.columns
    ):
        st.bar_chart(
            df["Investment_Score"]
            .value_counts()
            .sort_index()
        )

# =====================================================
# LISTINGS
# =====================================================

elif page == "Listings":

    st.title("📋 Property Listings")

    search = st.text_input(
        "Search Property"
    )

    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["Title"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    display_cols = [
        "Title",
        "Price",
        "Beds",
        "Baths"
    ]

    display_cols = [
        c for c in display_cols
        if c in filtered_df.columns
    ]

    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True
    )

# =====================================================
# AI ANALYSIS
# =====================================================

elif page == "AI Analysis":

    st.title("🤖 AI Property Analysis")

    if (
        df.empty
        or "AI_Analysis" not in df.columns
    ):
        st.warning(
            "AI Analysis data not found"
        )

    else:

        property_names = (
            df["Title"]
            .fillna("Unknown")
            .tolist()
        )

        selected_property = st.selectbox(
            "Select Property",
            property_names
        )

        selected_row = df[
            df["Title"] == selected_property
        ].iloc[0]

        st.markdown(
            selected_row["AI_Analysis"]
        )

# =====================================================
# ALERTS
# =====================================================

elif page == "Alerts":

    st.title("📨 High Potential Properties")

    if (
        df.empty
        or "Investment_Score"
        not in df.columns
    ):
        st.warning("No alert data")

    else:

        top_df = (
            df.sort_values(
                "Investment_Score",
                ascending=False
            )
            .head(10)
        )

        for _, row in top_df.iterrows():

            st.success(
                f"{row['Title']} | "
                f"Score: {row['Investment_Score']}"
            )

# =====================================================
# GOOGLE SHEETS
# =====================================================

elif page == "Google Sheets":

    st.title("📊 Google Sheets Data")

    st.info(
        f"Total Records: {len(df)}"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# ABOUT
# =====================================================

elif page == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
### AI Real Estate Listing Intelligence Agent

This project automates:

- Property Fetching
- Data Cleaning
- Investment Scoring
- AI Analysis
- Telegram Notifications
- Google Sheets Logging

### Technology Stack

- Streamlit
- n8n
- RapidAPI
- Groq LLM
- Telegram Bot
- Google Sheets

### Workflow

Streamlit
↓
n8n Webhook
↓
Property API
↓
AI Analysis
↓
Telegram
↓
Google Sheets
""")