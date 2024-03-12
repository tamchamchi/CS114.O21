#Should reconsider this item is xxx% higher than in-store. 
#Tôi có một chuỗi như này hãy sử dụng thư viện để trả về giá trị xxx trong chuỗi đó
import re

def find_percentage(text):
     """
     Hàm trích xuất số thập phân đúng trước chuỗi '% higher than in-store'.
     Hàm trích xuất số thập phân đúng trước chuỗi '% lower than in-store'.
     Args:
          text: Chuỗi đầu vào để xử lý.
     Returns:
          Số thập phân (float).
     """
     pattern = 0
     # Biểu thức chính quy để trích xuất số thập phân
     if "% lower than in-store" in text:
          pattern = r"(?P<percentage>\d+\.?\d*)% lower than in-store"
     if "% higher than in-store" in text:
          pattern = r"(?P<percentage>\d+\.?\d*)% higher than in-store"
     # Tìm kiếm chuỗi '% higher than in-store' trong chuỗi đầu vào
     match = re.search(pattern, text)
     percentage_str = match.group("percentage")
     # Chuyển đổi sang kiểu float
     return float(percentage_str)

def KiemTraCoTheMua(TienHienCo,list_GiaHang,list_ThongBao):
     TongHoaDonMuaOnl = sum(list_GiaHang)
     TongHoaDonMuaOff = sum(list_GiaMatHang)
     for GiaHang,ThongBao in zip(list_GiaHang,list_ThongBao):
          if "% lower than in-store" in ThongBao:
               TongHoaDonMuaOnl-=GiaHang*find_percentage(ThongBao)/100
          if "% higher than in-store" in ThongBao:
               TongHoaDonMuaOff+=GiaHang*find_percentage(ThongBao)/100
     if TienHienCo >= TongHoaDonMuaOff or TienHienCo >= TongHoaDonMuaOnl:
          return 'true'
     
     return 'false'
 
list_GiaMatHang=list(map(int,input().split()))
list_ThongBao = []
for i in range(len(list_GiaMatHang)):
     list_ThongBao.append(input())

TienHienCo = int(input())
print(KiemTraCoTheMua(TienHienCo,list_GiaMatHang,list_ThongBao))



               
          
