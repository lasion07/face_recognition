import streamlit as st

from ..model import Model

st.set_page_config(page_title="Tìm kiếm", page_icon="🔍")

@st.cache_data # Disable for Debugging
def find_in_database(image):
    model = Model()
    results = model.find(image)
    return results

def show_information(json_file):
    st.info("Full name:", json_file["Full name"])
    st.info("Birthday:", json_file["Birthday"])
    st.text_input("Born:", json_file["Born"])
    st.text_input("Height:", json_file["Height"])
    st.text_input("Nationality:", json_file["Nationality"])

if __name__ == "__main__":
    st.sidebar.title("Nhận dạng bằng khuôn mặt")
    st.sidebar.markdown("Đồ án chuyên ngành - Nhóm 16")
    
    st.title("Tìm kiếm thông tin bằng khuôn mặt")
        
    uploaded_file = st.file_uploader("Choose an image")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        input_image = read_image_from_bytes(bytes_data)
        
        st.header("Input image")
        st.image(bytes_data, channels="BGR")

        results = find_in_database(input_image)

        st.header("Result")

        if len(results) == 0:
            st.write("No face is found...")

        if st.checkbox('Show json output'):
            st.json(results)
        
        for i in range(len(results)):
            result = results[i]
            x1, y1, x2, y2 = xywh_to_xyxy(result["x"], result["y"], result["w"], result["h"])
            st.subheader(f"Face {i+1}")
            st.image(input_image[y1:y2, x1:x2], channels="BGR")

            if result["found"]:
                show_information(result)
                # Another case when there is a lack of the about of this person
            else:
                st.write("This person is not found in database...")
        
        st.header("This is the end of the result...")