import streamlit as st
import os
import json

# Xác định đường dẫn tới thư mục database
database_dir = "database"

# Tạo thư mục database nếu chưa tồn tại
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

# Kiểm tra xem tệp tin cơ sở dữ liệu đã tồn tại chưa
database_file = os.path.join(database_dir, "database.json")
if not os.path.exists(database_file):
    # Nếu chưa tồn tại, tạo một cơ sở dữ liệu mẫu trống
    with open(database_file, "w") as f:
        json.dump({}, f)


# Định nghĩa các hàm để xử lý các trường hợp khác nhau
def handle_image_upload():
    uploaded_files = st.file_uploader("Thêm một hoặc nhiều ảnh", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Đọc dữ liệu từ tệp tin được tải lên
            image_data = uploaded_file.read()
            # Hiển thị hình ảnh
            st.image(image_data, caption='Ảnh được tải lên', use_column_width=True)
            # Đóng tệp tin (không cần phải đóng)
        register_information()


def register_information():
    with st.form("registration_form"):
        name = st.text_input("Họ và tên", placeholder="Nhập họ và tên đầy đủ của bạn")
        birth_date = st.date_input("Ngày sinh")
        gender = st.selectbox("Giới tính", options=["Nam", "Nữ", "Khác"])
        nationality = st.text_input("Quốc tịch", placeholder="Nhập quốc tịch của bạn")
        hometown = st.text_input("Quê quán", placeholder="Nhập quê quán")
        address = st.text_input("Nơi thường trú", placeholder="Nhập địa chỉ thường trú")
        email = st.text_input("Email", placeholder="Nhập email của bạn")

        submitted = st.form_submit_button("Đăng ký")

        # Kiểm tra dữ liệu đã điền đầy đủ
        if name and birth_date and gender and nationality and hometown and address:
            if submitted:
                # Kiểm tra xem email đã tồn tại trong cơ sở dữ liệu chưa
                database_data = {}
                if os.path.exists(database_file):
                    with open(database_file, "r") as f:
                        database_data = json.load(f)

                # Kiểm tra nếu email đã tồn tại trong cơ sở dữ liệu
                if email in database_data:
                    st.warning("Thông tin đã tồn tại trong cơ sở dữ liệu!")
                    # Hiển thị nút "Cập Nhật" và "Không"
                    update_button = st.form_submit_button("Cập Nhật")
                    cancel_button = st.form_submit_button("Không")

                    if update_button:
                        # Cập nhật thông tin
                        database_data[email] = {
                            "name": name,
                            "birth_date": str(birth_date),
                            "gender": gender,
                            "nationality": nationality,
                            "hometown": hometown,
                            "address": address
                        }
                        with open(database_file, "w") as f:
                            json.dump(database_data, f)
                        st.success("Thông tin đã được cập nhật thành công!")

                    if cancel_button:
                        # Không cập nhật thông tin
                        st.info("Thông tin không được cập nhật.")
                        return 

                else:
                    # Thực hiện xử lý đăng ký khi thông tin chưa có trong cơ sở dữ liệu
                    database_data[email] = {
                        "name": name,
                        "birth_date": str(birth_date),
                        "gender": gender,
                        "nationality": nationality,
                        "hometown": hometown,
                        "address": address
                    }
                    with open(database_file, "w") as f:
                        json.dump(database_data, f)
                    st.success("Thông tin nhân dạng đã được đăng ký thành công!")
        else:
            st.warning("Vui lòng điền đầy đủ thông tin!")


st.title("Đăng ký thông tin nhân dạng")

# Tải ảnh lên hoặc chụp ảnh
function_choice = st.radio("Chọn chức năng", ("Tải Ảnh Lên", "Chụp Ảnh"))

if function_choice == "Tải Ảnh Lên":
    # Tải ảnh lên
    handle_image_upload()

elif function_choice == "Chụp Ảnh":
    # Chụp ảnh từ webcam
    img_file_buffer = st.file_uploader("Chụp ảnh", type=["jpg", "jpeg", "png"])
    if img_file_buffer is not None:
        # Đọc dữ liệu từ tệp tin được tải lên
        image_data = img_file_buffer.read()
        # Hiển thị hình ảnh
        st.image(image_data, caption='Ảnh đã chụp', use_column_width=True)

        # Đăng ký thông tin
        register_information()
