import streamlit as st
import requests
import time
import json

st.set_page_config(page_title="Fake News Detection and Verification Tool", layout="wide", page_icon="📰")

st.markdown(
    """
    <style>
    .app-header {
      display: flex;
      align-items: center;
      gap: 18px;
      margin-bottom: 8px;
    }
    .app-title {
      font-family: 'Inter', sans-serif;
      font-weight: 800;
      font-size: 36px;
      color: #0f172a;
      margin: 0;
    }
    .app-sub {
      color: #64748b;
      margin-top: 6px;
      font-size: 14px;
    }
    .card {
      background: #ffffff;
      border-radius: 12px;
      padding: 18px;
      box-shadow: 0 6px 20px rgba(16,24,40,0.06);
      border: 1px solid #eef2ff;
    }
    .badge {
      display:inline-block;
      padding:6px 10px;
      border-radius:999px;
      background:linear-gradient(90deg,#eef2ff,#f8fafc);
      color:#4f46e5;
      font-weight:700;
      font-size:12px;
      border:1px solid rgba(79,70,229,0.08);
    }
    .prediction-pill {
      display:inline-block;
      padding:10px 16px;
      border-radius:10px;
      font-weight:800;
      color:#ffffff;
      font-size:18px;
    }
    .pred-fake { background: linear-gradient(90deg,#ef4444,#dc2626); }
    .pred-real { background: linear-gradient(90deg,#10b981,#059669); }
    .label-sm { font-size:12px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.06em; }
    .detail-mono { font-family: monospace; font-size:13px; color:#0f172a; }
    .small-muted { color:#64748b; font-size:13px; }
    .claim-pill { background:#f8fafc; border-left:4px solid #4f46e5; padding:12px; border-radius:8px; margin-bottom:10px; }
    .verif-card { padding:12px; border-radius:8px; background:#ffffff; border:1px solid #eef2ff; }
    .v-true { border-left:4px solid #10b981; background:#f0fdf4; }
    .v-false { border-left:4px solid #ef4444; background:#fff1f2; }
    .step-active { color:#4f46e5; font-weight:700; }
    .step-done { color:#10b981; font-weight:700; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-header">
      <div>
        <div class="badge">Enterprise</div>
      </div>
      <div>
        <div class="app-title">Fake News Detection and Verification Tool</div>
        <div class="app-sub">Fast, transparent classification with claim-level verification and explainability.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

API = "http://127.0.0.1:5000/analyze"

col_left, col_right = st.columns([2, 1])

with col_left:
    text = st.text_area("Enter News Article", height=280)
    if not text:
        st.caption("Paste the full article or a claim to analyze. The system will extract claims and verify them against fact-check sources.")
with col_right:
    source = st.text_input("News Source")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;'><span class='label-sm'>Quick Actions</span></div>", unsafe_allow_html=True)
    sample1 = st.button("Sample: Medical Misinformation")
    sample2 = st.button("Sample: Economic Report")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='label-sm'>System</div>", unsafe_allow_html=True)
    st.markdown("<div class='small-muted'>Model</div><div class='detail-mono'>RoBERTa (custom)</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown("<div class='small-muted'>Endpoint</div><div class='detail-mono'>%s</div>" % API, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if sample1:
    st.session_state['sample_loaded'] = True
    text = "Scientists at Harvard University have developed a vaccine that provides 100% protection against all COVID-19 variants according to a new study published yesterday."
    st.experimental_rerun()
if sample2:
    st.session_state['sample_loaded'] = True
    text = "The Federal Reserve raised interest rates by 25 basis points in its latest policy meeting to combat rising inflation."
    st.experimental_rerun()

analyze_button = st.button("Analyze Article", key="analyze")

if analyze_button:
    if not text or text.strip() == "":
        st.error("Please provide article text before analysis.")
    else:
        steps = [
            "Validating article structure",
            "Cleaning & tokenizing",
            "Lemmatizing & feature extraction",
            "Running RoBERTa inference",
            "Extracting candidate claims",
            "Verifying claims with Fact Check API",
            "Compiling explanation and metrics"
        ]
        step_placeholders = [st.empty() for _ in steps]
        progress_bar = st.progress(0)
        for i, step in enumerate(steps):
            step_placeholders[i].markdown(f"<div class='step-active'>➤ {step}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(((i + 1) / len(steps)) * 100))
            time.sleep(0.45)
            step_placeholders[i].markdown(f"<div class='step-done'>✔ {step}</div>", unsafe_allow_html=True)
        progress_bar.empty()

        payload = {
            "text": text,
            "source": source
        }

        with st.spinner("Contacting analysis service and fetching results..."):
            try:
                response = requests.post(API, json=payload, timeout=30)
                result = response.json()
            except Exception as e:
                st.error("Analysis service error: %s" % str(e))
                result = None

        if result:
            st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
            pr_col1, pr_col2 = st.columns([2, 1])
            with pr_col1:
                pred = result.get("prediction", "N/A")
                if pred == "FAKE":
                    pill_html = f"<div class='prediction-pill pred-fake'>{pred}</div>"
                else:
                    pill_html = f"<div class='prediction-pill pred-real'>{pred}</div>"
                st.markdown(pill_html, unsafe_allow_html=True)
                st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
                st.subheader("Explanation")
                st.write(result.get("explanation", "No explanation returned."))
                st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
                st.subheader("Suspicious Claims")
                suspicious = result.get("suspicious_phrases", [])
                if isinstance(suspicious, list) and suspicious:
                    for s in suspicious:
                        st.markdown(f"<div class='claim-pill'>{s}</div>", unsafe_allow_html=True)
                else:
                    st.info("No suspicious phrases extracted.")
            with pr_col2:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("<div class='label-sm'>Source Trust</div>", unsafe_allow_html=True)
                trusted = result.get("trusted_source", "Unknown")
                st.markdown(f"<div style='font-size:18px;font-weight:700;margin-top:8px'>{trusted}</div>", unsafe_allow_html=True)
                st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
                st.markdown("<div class='label-sm'>System Metrics</div>", unsafe_allow_html=True)
                metrics = result.get("metrics", {})
                try:
                    st.json(metrics)
                except:
                    st.write(metrics)
                st.markdown("</div>", unsafe_allow_html=True)

            ver_col = st.container()
            st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
            st.markdown("<div class='label-sm'>Verification Results</div>", unsafe_allow_html=True)
            verifs = result.get("verification_results", []) or result.get("verification_results", [])
            if verifs:
                cols = st.columns(3)
                for i, v in enumerate(verifs):
                    with cols[i % 3]:
                        status = v.get("status", v.get("verdict", "UNVERIFIED"))
                        cls = "v-true" if status == "TRUE" else "v-false" if status == "FALSE" else ""
                        st.markdown(f"<div class='verif-card {cls}'><div style='font-weight:800;color:#0f172a'>{status}</div><div style='margin-top:6px'>{v.get('claim','')}</div><div style='margin-top:6px;color:#64748b;font-size:12px'>Source: {v.get('source','N/A')}</div></div>", unsafe_allow_html=True)
            else:
                st.info("No external verification matches found.")

            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
            st.success("Analysis complete")