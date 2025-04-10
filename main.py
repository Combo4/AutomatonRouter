import streamlit as st
import json
import pyperclip

# 47 relative offsets
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

st.set_page_config(page_title="Skytils Route Generator", layout="centered", page_icon="🧭")

st.markdown(
    "<h1 style='text-align: center; color: lime;'>Skytils Route Generator</h1>",
    unsafe_allow_html=True
)

with st.form("coords_form"):
    coord_input = st.text_input("Enter base coordinates (x y z)", placeholder="e.g., 700 50 500")
    submitted = st.form_submit_button("Generate Route")

if submitted:
    try:
        x_str, y_str, z_str = coord_input.strip().split()
        base_x, base_y, base_z = int(x_str), int(y_str), int(z_str)

        route = []
        for i, (dx, dy, dz) in enumerate(offsets[1:], start=1):
            point = {
                "x": base_x + dx,
                "y": base_y + dy,
                "z": base_z + dz,
                "r": 0,
                "g": 1,
                "b": 0,
                "options": {
                    "name": str(i)
                }
            }
            route.append(point)

        route_json = json.dumps(route, separators=(',', ':'))

        # Show the JSON and allow copying
        st.code(route_json, language='json')

        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(route_json)
            st.success("Copied to clipboard!")

    except ValueError:
        st.error("Please enter 3 integers separated by spaces (e.g., 700 50 500)")
