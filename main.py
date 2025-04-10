import streamlit as st
import json

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

st.set_page_config(page_title="Skytils Route Generator", layout="centered")

st.title("Skytils Route Generator")

x = st.number_input("Enter base X", value=0)
y = st.number_input("Enter base Y", value=0)
z = st.number_input("Enter base Z", value=0)

if st.button("Generate Route"):
    route = []
    for i, (dx, dy, dz) in enumerate(offsets[1:], start=1):
        route.append({
            "x": x + dx,
            "y": y + dy,
            "z": z + dz,
            "r": 0,
            "g": 1,
            "b": 0,
            "options": {
                "name": str(i)
            }
        })

    route_json = json.dumps(route, separators=(',', ':'))

    st.success("Route generated!")
    st.text_area("Generated JSON", value=route_json, height=300)
    st.download_button("Download JSON", route_json, file_name="skytils_route.txt")
