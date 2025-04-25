import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="SHOP.CO",  layout="wide")

# ---- CSS Styling ----
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
        }
        .shop-header {
            font-size: 3em;
            font-weight: 900;
            color: white;  /* Changed to white */
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.4);  /* Optional: makes white text pop */
        }
        .cart-badge {
            background-color: #ff4b4b;
            color: white;
            padding: 2px 10px;
            border-radius: 50%;
            font-size: 14px;
            margin-left: 5px;
        }
        .footer {
            text-align: center;
            padding: 30px 0 10px;
            color: #888;
            font-size: 14px;
        }
        .footer a {
            color: #444;
            margin: 0 10px;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)


# ---- Product Data ----
products = pd.DataFrame({
    "Product": ["Shirt", "Jeans", "Shoes", "Cap", "Watch", "Jacket"],
    "Category": ["Clothing", "Clothing", "Footwear", "Accessories", "Accessories", "Clothing"],
    "Price": [1500, 2500, 3500, 2000, 500, 3000],
    "Description": [
        "Premium cotton shirt, perfect for casual and formal occasions.",
        "Slim-fit jeans with a modern cut and stretch fabric.",
        "Stylish sneakers for daily wear and comfort.",
        "Cool summer cap made from breathable fabric.",
        "Elegant watch to complete your everyday look.",
        "Warm and stylish winter jacket with hood."
    ],
    "Image": [
        "https://img.sonofatailor.com/images/customizer/product/Black_O_Crew_Regular_NoPocket.jpg",
        "https://www.calvinklein.com.my/on/demandware.static/-/Sites-ck-master-catalog/default/dw0b2e959e/J224927/C25_01_J2249271BY_MO-ST-F1.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3Y0hluKxupGkTUwtqSGDNxurms-GXMX17iA&s",
        "https://m.media-amazon.com/images/I/61j-nUQuKRL._AC_SL1100_.jpg",
        "https://static-01.daraz.pk/p/39b2f8c5c03f999c95a61c4766889298.jpg",
        "https://deeds.pk/cdn/shop/files/New-Winter-Men-s-Hooded-Parkas-Windbreaker-Fashion-Thermal-Coats-Mens-Thick-Warm-Glossy-Black-Jackets_jpg_640x640_jpg.webp?v=1737463407"
    ]
})

# ---- Session State ----
if "cart" not in st.session_state:
    st.session_state.cart = []
if "view_product" not in st.session_state:
    st.session_state.view_product = None

# ---- Header ----
cart_count = len(st.session_state.cart)
st.markdown(f"<div class='shop-header'>SHOP.CO 🛒 <span class='cart-badge'>{cart_count}</span></div>", unsafe_allow_html=True)

# ---- Filters ----
st.sidebar.header("🔍 Filter Products")
category_filter = st.sidebar.multiselect("Category", options=products["Category"].unique())
max_price = st.sidebar.slider("Max Price", 500, 5000, 5000)
search_term = st.sidebar.text_input("Search Product")

filtered = products[
    (products["Price"] <= max_price) &
    (products["Category"].isin(category_filter) if category_filter else True)
]
if search_term:
    filtered = filtered[filtered["Product"].str.contains(search_term, case=False)]

# ---- Product Detail Page ----
if st.session_state.view_product is not None:
    product = st.session_state.view_product
    st.image(product["Image"], width=300)
    st.markdown(f"## {product['Product']}")
    st.markdown(f"**Category:** {product['Category']}")
    st.markdown(f"**Price:** ${product['Price']}")
    st.markdown(f"**Description:** {product['Description']}")
    if st.button("Add to Cart"):
        st.session_state.cart.append(product)
        st.success(f"{product['Product']} added to cart!")
    if st.button("🔙 Back to Products"):
        st.session_state.view_product = None
        st.rerun()
    st.stop()

# ---- Show Products Grid ----
st.subheader("🧾 Products")
cols = st.columns(3)
for i, row in filtered.iterrows():
    with cols[i % 3]:
        st.image(row["Image"], width=200)
        st.markdown(f"**{row['Product']}**")
        st.caption(f"₹{row['Price']} - {row['Category']}")
        if st.button("View Details", key=f"view_{i}"):
            st.session_state.view_product = row
            st.rerun()
        if st.button("Add to Cart", key=f"cart_{i}"):
            st.session_state.cart.append(row)
            st.success(f"Added {row['Product']} to cart!")

# ---- Sidebar Cart ----
st.sidebar.header("🛒 Cart")
total = 0
for idx, item in enumerate(st.session_state.cart):
    st.sidebar.markdown(f"- {item['Product']} - ₹{item['Price']}")
    total += item["Price"]
    if st.sidebar.button(f"Remove {item['Product']}", key=f"remove_{idx}"):
        st.session_state.cart.pop(idx)
        st.rerun()
if total > 0:
    st.sidebar.markdown(f"**Total: ₹{total}**")
    if st.sidebar.button("🧹 Clear Cart"):
        st.session_state.cart.clear()
        st.rerun()
else:
    st.sidebar.markdown("_Your cart is empty._")

# ---- Footer ----
st.markdown("""
    <div class='footer'>
        Made with ❤️ by <b>HIKMAT KHAN</b><br>
        <a href="https://github.com/hikmatkhan090" target="_blank">GitHub</a> |
        <a href="https://twitter.com/yourhandle" target="_blank">Twitter</a> |
        <a href="https://www.linkedin.com/in/hikmat-khan-652301256/" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
