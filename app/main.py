"""
Minimal Streamlit UI for Navi AI (app/main.py)

This is a small scaffold so you can run a local UI and check the backend health.
Run locally with:

```powershell
streamlit run app/main.py
```

Features:
- Title and description
- Backend URL input (defaults to http://localhost:8000)
- Health check button that queries `GET /health`
- Image uploader placeholder (disabled until backend supports multipart)
"""

import streamlit as st
import requests


st.set_page_config(page_title="Navi AI — Demo UI", layout="centered")

st.title("Navi AI — Demo UI")
st.caption("Small Streamlit scaffold for the Navi AI project")

st.markdown(
	"""
	This minimal UI lets you check the backend health and demonstrates where
	a future image upload / detection component would live.
	"""
)

backend_url = st.text_input("Backend base URL", value="http://localhost:8000")

col1, col2 = st.columns(2)

with col1:
	if st.button("Check backend /health"):
		try:
			r = requests.get(f"{backend_url.rstrip('/')}/health", timeout=5)
			r.raise_for_status()
			st.success("Backend reachable")
			st.json(r.json())
		except Exception as e:
			st.error(f"Backend health check failed: {e}")

with col2:
	st.write("Deployment info")
	st.write("- Backend module: `backend/fastapi_app.py`")
	st.write("- File upload disabled until `python-multipart` is installed on deployment")

st.header("Image Upload (placeholder)")
st.info("The real /detect endpoint is not enabled in this deployment. Re-enable after installing python-multipart.")
uploaded_file = st.file_uploader("Upload an image for detection", type=["png", "jpg", "jpeg"], disabled=True)

if uploaded_file is not None:
	st.image(uploaded_file)
	st.warning("Upload handling is currently disabled on the server.")

st.markdown("---")
st.markdown("If you want, I can enable an upload flow and wire it to the backend once multipart support is available.")

