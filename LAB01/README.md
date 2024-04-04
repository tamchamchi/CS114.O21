<h1 align="center"><b>DIGIT CLASSIFICATION</b></h1>

## THÀNH VIÊN NHÓM: <br>
| STT    | MSSV          | Họ và Tên              | Github                                               | Email                   |
| :------: |:-------------:| :----------------------|:-----------------------------------------------------|:-------------------------
| 1      | 22520054   | Nguyễn Duy Tâm Anh |https://github.com/tamchamchi          |22520054@gm.uit.edu.vn   |
| 2      | 22521322     | Trần Văn Thân       |https://github.com/vanthan04|22521322@gm.uit.edu.vn   |
| 3      | 22521626     | Nguyễn Mạnh Tường          |https://github.com/greatwall2704              |22521626@gm.uit.edu.vn   |

## TRÌNH BÀY VẤN ĐỀ:
- Thực hiện test trên tập dữ liệu của nhóm.
- Tìm ra nguyên nhân tại sao hiệu xuất lại thấp.
- Nêu giải pháp.
- Thực hiện chạy lại model sau khi tiền xử lý

## THỰC HIỆN TEST TRÊN TẬP DỮ LIỆU CỦA NHÓM:
- Tập dữ liệu test: 120 bức ảnh
- Sau khi thực hiện chạy trên tập dữ liệu của nhóm thì độ chính xác của model rất thấp: **15,8%** <br>
- Trong khi thực hiện tập dữ liệu cũ thì lại có độ chính xác rất cao: **>98,5%**<br>
**=>** Thế là chúng ta có thể kết luận rằng model này không hiệu quả với tập dữ liệu thức tế? <br>
**!Chưa thể kết luận:** Vì tập dữ liệu của chúng ta chưa qua xử lý. 

## NGUYÊN NHÂN:
- **Ảnh màu (RGB)**: Việc xử lý ảnh màu sẽ không hiệu quả vì model được huấn luyện trên ảnh **trắng-đen (binary)**.
- **Chất lượng hình ảnh**: Có nhiều nguyên nhân ảnh hưởng:
     - *Ánh sáng* 
     - *Nét chữ* 
     - *Độ phân giải của ống kính camera*
     - *Độ tương phản giữa chữ viết và nền*
     - *Nền chứa các chi tiết không cần thiết* 

## GIẢI PHÁP:
- Thay đổi màu sắc ảnh sáng trắng đen: Sử dụng phương pháp ngưỡng hóa (thresholding).
- Chụp ảnh trong điều kiện ánh sáng thích hợp.
- Sử dụng các nét chữ đậm hơn.
- Sử dụng màu mực và giấy có độ tương phản cao như: mực đen - giấy trăng.
- Sử dụng giấy trơn để viết. <br>
=> Độ chính xác tăng:  **75.83%**



