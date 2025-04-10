import streamlit as st
import json

offsets = [
    [0, 0, 0], [14, 14, 13], [35, 10, -6], [43, 8, -19], [57, 8, -10], [52, 8, 6],
    [51, 8, 28], [36, 8, 54], [16, 14, 48], [18, 13, -17], [31, 25, -19], [33, 15, -31],
    [42, 41, -25], [48, 41, -15], [55, 48, -24], [56, 34, 2], [53, 43, 43], [41, 43, 57],
    [30, 36, 49], [11, 36, 57], [3, 41, 51], [40, -3, 48], [26, -3, 38], [25, 3, 33],
    [17, 3, 31], [27, -3, 22], [20, -3, 16], [37, -9, 1], [53, -9, 8], [58, -10, 25],
    [37, -28, 12], [36, -18, 36], [10, -18, 37], [-13, -27, 27], [-16, -27, 7],
    [-18, -26, -16], [10, -24, -11], [12, -22, -28], [22, -28, -5], [17, -10, -7],
    [-10, -3, 2], [-11, -3, -18], [-24, -3, -25], [1, 0, -28], [-13, 8, 4],
    [-15, 17, -9], [11, 15, 10]
]

st.set_page_config(page_title="Skytils Route Generator", layout="centered")
st.title("Skytils Route Generator")

coord_input = st.text_input("Enter base coordinates (X Y Z)", placeholder="e.g. 200 200 200")

if st.button("Generate Route"):
    try:
        x_str, y_str, z_str = coord_input.strip().split()
        x, y, z = int(x_str), int(y_str), int(z_str)

        route = []
        for i, (dx, dy, dz) in enumerate(offsets[1:], start=1):
            route.append({
                "x": x + dx,
                "y": y + dy,
                "z": z + dz,
                "r": 0,
                "g": 1,
                "b": 0,
                "options": {"name": str(i)}
            })

        route_json = json.dumps(route, separators=(',', ':'))

        st.success("Route generated!")

        st.text_area("Generated JSON", value=route_json, height=300, key="route_json")

        # Button Row with matching style
        st.markdown("""
        <style>
        .button-row {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        .button-row button {
            background-color: #0e1117;
            border: 1px solid #444;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        .button-row button:hover {
            background-color: #1a1e27;
        }
        </style>

        <div class="button-row">
            <button onclick="copyText()">📋 Copy</button>
            <a download="skytils_route.txt" href="data:text/plain;charset=utf-8,{data}" target="_blank">
                <button>💾 Download</button>
            </a>
        </div>

        <textarea id="toCopy" style="opacity:0; height:0;">{data}</textarea>

        <script>
        function copyText() {{
            var copyText = document.getElementById("toCopy");
            copyText.style.display = "block";
            copyText.select();
            document.execCommand("copy");
            copyText.style.display = "none";
            alert("Copied to clipboard!");
        }}
        </script>
        """.replace("{data}", route_json), unsafe_allow_html=True)

    except Exception:
        st.error("Invalid format. Please enter coordinates like: `200 200 200`")
