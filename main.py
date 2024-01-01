import streamlit as st

from model import Model
from utils.commons import read_image_from_bytes, xywh_to_xyxy

st.set_page_config(page_title="Nhận dạng khuôn mặt", page_icon="🇻🇳")

@st.cache_data # Disable for Debugging
def find_in_database(image, distance_metric, max_distance):
    model = Model(threshold=max_distance, distance_metric=distance_metric)
    results = model.find(image)
    return results

if __name__ == "__main__":
    st.sidebar.title("Nhận dạng bằng khuôn mặt")
    st.sidebar.markdown("Đồ án chuyên ngành - Nhóm 16")
    
    st.title("Tìm kiếm thông tin bằng khuôn mặt")
        
    uploaded_file = st.file_uploader("Choose an image")
    if uploaded_file is None:
        uploaded_file = st.camera_input("Or take a photo")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        input_image = read_image_from_bytes(bytes_data)
        
        st.header("Input image")
        st.image(bytes_data, use_column_width=True, channels="BGR")

        # Settings
        distance_metric = 'cosine'
        max_distance = 0.4

        if st.checkbox('Show advanced settings'):
            st.header("Settings")
            distance_metric = st.selectbox(
                'Distance metric',
                ('cosine', 'euclidean', 'euclidean_l2'))
            max_distance = st.slider("Max distance", min_value=0.1, max_value=2.0, value=0.4, step=0.1)

        show_json = st.checkbox('Show json output')

        if st.button("Find"):
            results = find_in_database(input_image, distance_metric, max_distance)

            st.header("Result")

            if show_json:
                st.json(results)
            
            for i in range(len(results)):
                result = results[i]
                x1, y1, x2, y2 = xywh_to_xyxy(result["x"], result["y"], result["w"], result["h"])
                
                st.subheader(f"Face {i+1}")

                col1, col2 = st.columns(2)
                
                with col1:
                    st.image(input_image[y1:y2, x1:x2], use_column_width=True, channels="BGR")
                
                with col2:
                    if result["found"]:                    
                        st.info(f'**No.**: {result["No."]}')
                        st.info(f'**Full name**: {result["Full name"]}')
                        st.info(f'**Date of birth**: {result["Date of birth"]}')
                        st.info(f'**Sex**: {result["Sex"]}')
                        st.info(f'**Nationality**: {result["Nationality"]}')
                        st.info(f'**Place of origin**: {result["Place of origin"]}')
                        st.info(f'**Place of residence**: {result["Place of residence"]}')
                        # Another case when there is a lack of the about of this person
                    else:
                        st.error("This person is not found in database...")
            
            st.header("This is the end of the result...")