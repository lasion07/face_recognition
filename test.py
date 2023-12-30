import streamlit as st

# Định nghĩa các hàm để xử lý các trường hợp khác nhau
def handle_image_upload():
    uploaded_files = st.file_uploader("Thêm một hoặc nhiều ảnh", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Đọc dữ liệu từ tệp tin được tải lên
            image_data = uploaded_file.read()
            # Hiển thị hình ảnh
            st.image(image_data, caption='Ảnh được tải lên', use_column_width=True)
            # Đóng tệp tin
            uploaded_file.close()

# def register_information():
#     with st.form("registration_form"):
#         st.text_input("Họ và tên", placeholder="Nhập họ và tên đầy đủ của bạn")
#         st.date_input("Ngày sinh")
#         st.selectbox("Giới tính", options=["Nam", "Nữ", "Khác"])
#         st.text_input("Quốc tịch", placeholder="Nhập quốc tịch của bạn")
#         st.text_input("Quê quán", placeholder="Nhập quê quán")
#         st.text_input("Nơi thường trú", placeholder="Nhập địa chỉ thường trú")
#         submitted = st.form_submit_button("Đăng ký")
#         if submitted:
#             st.success("Thông tin nhân dạng đã được đăng ký thành công!")

# Tiêu đề
st.title("Đăng ký thông tin nhân dạng")

# Tải ảnh lên
handle_image_upload()

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
# Đăng ký thông tin cá nhân
# register_information()
#
# # Xử lý trường hợp thông tin đã tồn tại
# if st.checkbox("Thông tin nhân dạng đã có trong cơ sở dữ liệu?"):
#     if st.button("Cập nhật"):
#         st.success("Thông tin nhân dạng đã được cập nhật!")
#     else:
#         st.error("Thông tin nhân dạng không được cập nhật do không điền đủ thông tin.")
