
import json
import os

def append_questions(filename, new_questions):
    filepath = os.path.join("quiz", filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []
    
    # Check for duplicates to be safe
    existing_qs = {q['question'].strip().lower() for q in data}
    
    count = 0
    for q in new_questions:
        if q['question'].strip().lower() not in existing_qs:
            data.append(q)
            count += 1
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added {count} questions to {filename}. Total now: {len(data)}")

# --- Questions Data ---

# Chapter 2: Nhà nước xã hội chủ nghĩa
qs_02 = [
    {"question": "Nhà nước xã hội chủ nghĩa ra đời là kết quả của cuộc cách mạng nào?", "options": ["Cách mạng tư sản", "Cách mạng vô sản", "Cách mạng giải phóng dân tộc", "Cách mạng văn hóa"], "answer": "Cách mạng vô sản"},
    {"question": "Cơ sở kinh tế của nhà nước xã hội chủ nghĩa là gì?", "options": ["Chế độ tư hữu về tư liệu sản xuất", "Chế độ công hữu về tư liệu sản xuất chủ yếu", "Kinh tế thị trường tự do", "Kinh tế hỗn hợp"], "answer": "Chế độ công hữu về tư liệu sản xuất chủ yếu"},
    {"question": "Bản chất chính trị của nhà nước xã hội chủ nghĩa mang bản chất của giai cấp nào?", "options": ["Giai cấp nông dân", "Giai cấp công nhân", "Tầng lớp trí thức", "Giai cấp tư sản"], "answer": "Giai cấp công nhân"},
    {"question": "Sự thống trị của giai cấp vô sản khác với các giai cấp bóc lột trước đây ở điểm nào?", "options": ["Là sự thống trị của thiểu số đối với đa số", "Là sự thống trị của đa số đối với thiểu số", "Không sử dụng bạo lực", "Chỉ tập trung vào kinh tế"], "answer": "Là sự thống trị của đa số đối với thiểu số"},
    {"question": "Theo V.I. Lênin, nhà nước xã hội chủ nghĩa còn là nhà nước theo đúng nghĩa không?", "options": ["Là nhà nước theo đúng nghĩa", "Là nửa nhà nước", "Không còn là nhà nước", "Là nhà nước siêu nhiên"], "answer": "Là nửa nhà nước"},
    {"question": "Chức năng của nhà nước xã hội chủ nghĩa được chia thành những loại nào dựa trên phạm vi tác động?", "options": ["Chức năng kinh tế và chính trị", "Chức năng đối nội và đối ngoại", "Chức năng trấn áp và tổ chức", "Chức năng văn hóa và xã hội"], "answer": "Chức năng đối nội và đối ngoại"},
    {"question": "Trong nhà nước xã hội chủ nghĩa, chức năng nào đóng vai trò quyết định?", "options": ["Chức năng trấn áp", "Chức năng tổ chức và xây dựng", "Chức năng quân sự", "Chức năng ngoại giao"], "answer": "Chức năng tổ chức và xây dựng"},
    {"question": "V.I. Lênin cho rằng, cơ sở kinh tế của bạo lực cách mạng là gì?", "options": ["Sức mạnh quân sự", "Năng suất lao động xã hội cao hơn", "Sự ủng hộ của quốc tế", "Tài nguyên thiên nhiên"], "answer": "Năng suất lao động xã hội cao hơn"},
    {"question": "Mục tiêu hàng đầu của nhà nước xã hội chủ nghĩa là gì?", "options": ["Bảo vệ quyền lợi giai cấp thống trị", "Mở rộng lãnh thổ", "Chăm lo cho lợi ích của đại đa số nhân dân lao động", "Duy trì trật tự đẳng cấp"], "answer": "Chăm lo cho lợi ích của đại đa số nhân dân lao động"},
    {"question": "Nhà nước xã hội chủ nghĩa là công cụ để thực hiện quyền lực của ai?", "options": ["Của riêng giai cấp công nhân", "Của nhân dân", "Của Đảng Cộng sản", "Của các nhà tư bản"], "answer": "Của nhân dân"},
    {"question": "Mối quan hệ giữa dân chủ xã hội chủ nghĩa và nhà nước xã hội chủ nghĩa là gì?", "options": ["Dân chủ là cơ sở, nền tảng cho việc xây dựng nhà nước", "Nhà nước là công cụ thực thi dân chủ", "Cả a và b đều đúng", "Không có mối quan hệ nào"], "answer": "Cả a và b đều đúng"},
    {"question": "Công cụ sắc bén nhất để ngăn chặn hành vi xâm phạm quyền lợi nhân dân trong CNXH là gì?", "options": ["Dư luận xã hội", "Nhà nước xã hội chủ nghĩa", "Các tổ chức phi chính phủ", "Giáo dục đạo đức"], "answer": "Nhà nước xã hội chủ nghĩa"},
    {"question": "Theo Lênin, nhà nước kiểu mới trong thời kỳ quá độ là nhà nước:", "options": ["Dân chủ tư sản", "Chuyên chính vô sản", "Quân chủ lập hiến", "Phong kiến tập quyền"], "answer": "Chuyên chính vô sản"},
    {"question": "Đặc điểm nào KHÔNG phải là đặc điểm của nhà nước xã hội chủ nghĩa?", "options": ["Mang bản chất giai cấp công nhân", "Là công cụ của thiểu số trấn áp đa số", "Đại diện cho ý chí của nhân dân", "Đặt dưới sự lãnh đạo của Đảng Cộng sản"], "answer": "Là công cụ của thiểu số trấn áp đa số"},
    {"question": "Trong nhà nước xã hội chủ nghĩa, sự phân hóa giữa các giai cấp, tầng lớp diễn ra như thế nào?", "options": ["Ngày càng sâu sắc", "Từng bước được thu hẹp", "Giữ nguyên như cũ", "Biến mất hoàn toàn ngay lập tức"], "answer": "Từng bước được thu hẹp"},
    {"question": "Chức năng trấn áp của nhà nước xã hội chủ nghĩa hướng vào đối tượng nào?", "options": ["Nhân dân lao động", "Giai cấp bóc lột đã bị lật đổ và phần tử chống đối", "Tầng lớp trí thức", "Các dân tộc thiểu số"], "answer": "Giai cấp bóc lột đã bị lật đổ và phần tử chống đối"},
    {"question": "Nhà nước xã hội chủ nghĩa là tổ chức quản lý lĩnh vực nào của nhân dân?", "options": ["Chỉ kinh tế", "Chỉ chính trị", "Kinh tế, văn hóa, xã hội", "Chỉ quân sự"], "answer": "Kinh tế, văn hóa, xã hội"},
    {"question": "Nhà nước xã hội chủ nghĩa được xây dựng trên nền tảng tinh thần là?", "options": ["Chủ nghĩa tự do", "Lý luận chủ nghĩa Mác - Lênin và giá trị văn hóa tiến bộ", "Tôn giáo", "Chủ nghĩa dân tộc cực đoan"], "answer": "Lý luận chủ nghĩa Mác - Lênin và giá trị văn hóa tiến bộ"},
    {"question": "Cải tạo xã hội cũ, xây dựng thành công xã hội mới là nội dung chủ yếu của:", "options": ["Chức năng trấn áp", "Chức năng tổ chức và xây dựng", "Chức năng đối ngoại", "Chức năng quân sự"], "answer": "Chức năng tổ chức và xây dựng"},
    {"question": "Đảng ta xem Nhà nước là gì trong hệ thống chính trị?", "options": ["Trụ cột", "Lực lượng lãnh đạo", "Cơ sở xã hội", "Tổ chức quần chúng"], "answer": "Trụ cột"},
    {"question": "Để nhà nước xã hội chủ nghĩa không bị tha hóa, cần phải làm gì?", "options": ["Tăng cường quyền lực tuyệt đối", "Kiểm soát quyền lực bằng nền dân chủ xã hội chủ nghĩa", "Giảm bớt vai trò của pháp luật", "Loại bỏ vai trò của Đảng"], "answer": "Kiểm soát quyền lực bằng nền dân chủ xã hội chủ nghĩa"},
    {"question": "Nhà nước xã hội chủ nghĩa ra đời khi nào?", "options": ["Khi giai cấp công nhân xuất hiện", "Khi mâu thuẫn giai cấp gay gắt không thể điều hòa", "Sau khi cách mạng vô sản thành công", "Khi có đảng cộng sản"], "answer": "Sau khi cách mạng vô sản thành công"},
    {"question": "Sự trấn áp trong nhà nước xã hội chủ nghĩa là sự trấn áp của:", "options": ["Thiểu số với đa số", "Đa số với thiểu số", "Giai cấp này với giai cấp khác", "Nhà nước với công dân"], "answer": "Đa số với thiểu số"},
    {"question": "Nguyên tắc tổ chức và hoạt động cơ bản của nhà nước xã hội chủ nghĩa là:", "options": ["Tam quyền phân lập", "Tập trung dân chủ", "Tự do vô chính phủ", "Quân chủ chuyên chế"], "answer": "Tập trung dân chủ"},
    {"question": "Trong xã hội xã hội chủ nghĩa, giai cấp nào giữ địa vị thống trị về chính trị?", "options": ["Giai cấp tư sản", "Giai cấp nông dân", "Giai cấp vô sản (công nhân)", "Tầng lớp trí thức"], "answer": "Giai cấp vô sản (công nhân)"},
    {"question": "Nhà nước xã hội chủ nghĩa là một thiết chế:", "options": ["Phi giai cấp", "Mang tính giai cấp sâu sắc", "Siêu giai cấp", "Chỉ mang tính xã hội"], "answer": "Mang tính giai cấp sâu sắc"},
    {"question": "Nhà nước xã hội chủ nghĩa đại biểu cho:", "options": ["Lợi ích riêng của công nhân", "Lợi ích của giai cấp tư sản", "Ý chí chung của nhân dân lao động", "Lợi ích của quan lại"], "answer": "Ý chí chung của nhân dân lao động"},
    {"question": "Về phương diện kinh tế, nhà nước XHCN không còn tồn tại:", "options": ["Quan hệ sản xuất", "Lực lượng sản xuất", "Quan hệ sản xuất bóc lột", "Trao đổi hàng hóa"], "answer": "Quan hệ sản xuất bóc lột"},
    {"question": "Nhà nước xã hội chủ nghĩa thực hiện quyền lực của nhân dân thông qua:", "options": ["Các cơ quan đại diện và tham gia trực tiếp", "Chỉ thông qua bầu cử", "Chỉ thông qua biểu tình", "Thông qua vũ lực"], "answer": "Các cơ quan đại diện và tham gia trực tiếp"},
    {"question": "Nếu nhà nước xã hội chủ nghĩa đánh mất bản chất của mình sẽ dẫn đến:", "options": ["Dân chủ phát triển", "Xâm phạm quyền làm chủ của người dân, chuyên chế", "Kinh tế tăng trưởng nhanh", "Xã hội ổn định"], "answer": "Xâm phạm quyền làm chủ của người dân, chuyên chế"},
    {"question": "Chức năng nào thể hiện bản chất giai cấp của nhà nước rõ nét nhất?", "options": ["Chức năng xã hội", "Chức năng trấn áp", "Chức năng kinh tế", "Chức năng văn hóa"], "answer": "Chức năng trấn áp"},
    {"question": "Nhà nước xã hội chủ nghĩa có nhiệm vụ gì đối với các giá trị văn hóa?", "options": ["Xóa bỏ hoàn toàn văn hóa cũ", "Tiếp thu tinh hoa nhân loại và giữ gìn bản sắc dân tộc", "Chỉ phát triển văn hóa vô sản", "Ngăn cấm giao lưu văn hóa"], "answer": "Tiếp thu tinh hoa nhân loại và giữ gìn bản sắc dân tộc"},
    {"question": "Công cụ bạo lực trong nhà nước XHCN dùng để:", "options": ["Đàn áp nhân dân", "Bảo vệ thành quả cách mạng và an ninh chính trị", "Mở rộng lãnh thổ", "Giải quyết mâu thuẫn nội bộ nhân dân"], "answer": "Bảo vệ thành quả cách mạng và an ninh chính trị"},
    {"question": "Sự ra đời của nhà nước XHCN là tất yếu khách quan do:", "options": ["Ý muốn của lãnh tụ", "Mâu thuẫn giữa LLSX xã hội hóa cao và QHSX tư hữu TBCN", "Sự can thiệp của nước ngoài", "Sự suy đồi đạo đức"], "answer": "Mâu thuẫn giữa LLSX xã hội hóa cao và QHSX tư hữu TBCN"},
    {"question": "Nhà nước xã hội chủ nghĩa là kiểu nhà nước:", "options": ["Cuối cùng trong lịch sử", "Tồn tại vĩnh viễn", "Giống nhà nước tư bản", "Phi lịch sử"], "answer": "Cuối cùng trong lịch sử"},
    {"question": "Cơ quan nào trong bộ máy nhà nước XHCN đại diện cao nhất cho quyền lực nhân dân?", "options": ["Chính phủ", "Tòa án", "Quốc hội (Cơ quan quyền lực nhà nước cao nhất)", "Viện kiểm sát"], "answer": "Quốc hội (Cơ quan quyền lực nhà nước cao nhất)"},
    {"question": "Vai trò của Đảng Cộng sản đối với nhà nước XHCN là:", "options": ["Làm thay nhà nước", "Lãnh đạo nhà nước", "Đứng ngoài nhà nước", "Phụ thuộc nhà nước"], "answer": "Lãnh đạo nhà nước"},
    {"question": "Cơ sở xã hội của nhà nước XHCN là:", "options": ["Khối đại đoàn kết toàn dân tộc dựa trên liên minh công - nông - trí thức", "Giai cấp công nhân đơn độc", "Tầng lớp doanh nhân", "Giai cấp tư sản"], "answer": "Khối đại đoàn kết toàn dân tộc dựa trên liên minh công - nông - trí thức"},
    {"question": "Nhà nước XHCN quản lý xã hội chủ yếu bằng:", "options": ["Mệnh lệnh hành chính", "Hiến pháp và pháp luật", "Đạo đức", "Phong tục tập quán"], "answer": "Hiến pháp và pháp luật"},
    {"question": "Trong thời kỳ quá độ, nhà nước XHCN cần thiết để:", "options": ["Duy trì bóc lột", "Cải tạo xã hội cũ, xây dựng xã hội mới", "Bảo vệ quyền lợi tư bản", "Ngăn cản dân chủ"], "answer": "Cải tạo xã hội cũ, xây dựng xã hội mới"},
    {"question": "Theo quan điểm Mác - Lênin, khi chủ nghĩa cộng sản hoàn toàn thắng lợi, nhà nước sẽ:", "options": ["Phát triển mạnh mẽ nhất", "Tự tiêu vong", "Chuyển thành nhà nước toàn cầu", "Trở thành lực lượng quân sự"], "answer": "Tự tiêu vong"},
    {"question": "Nhà nước XHCN bảo đảm quyền bình đẳng cho:", "options": ["Chỉ đảng viên", "Mọi công dân", "Chỉ giai cấp công nhân", "Người giàu"], "answer": "Mọi công dân"},
    {"question": "Một trong những đặc trưng của nhà nước XHCN là:", "options": ["Quyền lực tập trung trong tay cá nhân", "Không có pháp luật", "Thực hiện dân chủ rộng rãi", "Phân biệt chủng tộc"], "answer": "Thực hiện dân chủ rộng rãi"},
    {"question": "Sức mạnh của nhà nước XHCN bắt nguồn từ:", "options": ["Vũ khí hiện đại", "Sự ủng hộ và tham gia của nhân dân", "Viện trợ nước ngoài", "Tài nguyên thiên nhiên"], "answer": "Sự ủng hộ và tham gia của nhân dân"},
    {"question": "Chức năng tổ chức và xây dựng của nhà nước XHCN thể hiện rõ nhất trong lĩnh vực:", "options": ["Quản lý kinh tế", "Quân sự", "Ngoại giao", "An ninh"], "answer": "Quản lý kinh tế"},
    {"question": "Khác với nhà nước tư sản, nhà nước XHCN:", "options": ["Bảo vệ chế độ tư hữu", "Xóa bỏ chế độ tư hữu, thiết lập công hữu", "Duy trì áp bức", "Không can thiệp kinh tế"], "answer": "Xóa bỏ chế độ tư hữu, thiết lập công hữu"},
    {"question": "Nhà nước XHCN là công cụ để giai cấp công nhân:", "options": ["Làm giàu cho bản thân", "Tổ chức, lãnh đạo xã hội xây dựng CNXH", "Đàn áp nông dân", "Thỏa hiệp với tư sản"], "answer": "Tổ chức, lãnh đạo xã hội xây dựng CNXH"},
    {"question": "Để phát huy vai trò của nhà nước XHCN, cần phải:", "options": ["Quan liêu hóa bộ máy", "Xây dựng nhà nước pháp quyền trong sạch, vững mạnh", "Giảm bớt dân chủ", "Tách rời Đảng và Nhà nước"], "answer": "Xây dựng nhà nước pháp quyền trong sạch, vững mạnh"}
]

# Chapter 3: Dân chủ XHCN và Nhà nước pháp quyền
qs_03 = [
    {"question": "Chế độ dân chủ nhân dân ở Việt Nam được xác lập từ năm nào?", "options": ["1930", "1945", "1954", "1975"], "answer": "1945"},
    {"question": "Đại hội nào của Đảng nhấn mạnh phát huy dân chủ để tạo động lực mạnh mẽ cho phát triển đất nước?", "options": ["Đại hội V", "Đại hội VI", "Đại hội VII", "Đại hội VIII"], "answer": "Đại hội VI"},
    {"question": "Bản chất của nền dân chủ xã hội chủ nghĩa ở Việt Nam là gì?", "options": ["Dân là gốc, là chủ, dân làm chủ", "Nhà nước làm chủ", "Đảng làm chủ", "Trí thức làm chủ"], "answer": "Dân là gốc, là chủ, dân làm chủ"},
    {"question": "Theo Hồ Chí Minh, nước ta là nước dân chủ, nghĩa là:", "options": ["Quyền hành và lực lượng đều ở nơi dân", "Quyền hành ở nơi quan", "Lực lượng ở quân đội", "Quyền hành ở quốc tế"], "answer": "Quyền hành và lực lượng đều ở nơi dân"},
    {"question": "Dân chủ xã hội chủ nghĩa vừa là mục tiêu, vừa là gì của sự phát triển đất nước?", "options": ["Phương tiện", "Động lực", "Kết quả", "Hình thức"], "answer": "Động lực"},
    {"question": "Dân chủ gắn liền với kỷ luật, kỷ cương và phải được thể chế hóa bằng:", "options": ["Đạo đức", "Pháp luật", "Hương ước", "Dư luận"], "answer": "Pháp luật"},
    {"question": "Hai hình thức thực hiện dân chủ ở Việt Nam là:", "options": ["Dân chủ tập trung và dân chủ phân tán", "Dân chủ gián tiếp và dân chủ trực tiếp", "Dân chủ tư sản và dân chủ vô sản", "Dân chủ nội bộ và dân chủ ngoại vi"], "answer": "Dân chủ gián tiếp và dân chủ trực tiếp"},
    {"question": "Hình thức dân chủ đại diện còn được gọi là:", "options": ["Dân chủ trực tiếp", "Dân chủ gián tiếp", "Dân chủ cơ sở", "Dân chủ tham gia"], "answer": "Dân chủ gián tiếp"},
    {"question": "Cơ quan quyền lực nhà nước cao nhất ở Việt Nam do nhân dân bầu ra là:", "options": ["Chính phủ", "Quốc hội", "Mặt trận Tổ quốc", "Viện kiểm sát"], "answer": "Quốc hội"},
    {"question": "Phương châm thực hiện quy chế dân chủ ở cơ sở là:", "options": ["Dân biết, dân bàn, dân làm, dân kiểm tra", "Đảng lãnh đạo, nhà nước quản lý", "Tự do tuyệt đối", "Tuân theo mệnh lệnh cấp trên"], "answer": "Dân biết, dân bàn, dân làm, dân kiểm tra"},
    {"question": "Một trong những đặc điểm của Nhà nước pháp quyền XHCN Việt Nam là:", "options": ["Tam quyền phân lập đối trọng", "Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp, kiểm soát", "Quyền lực tập trung vào một người", "Pháp luật không phải là tối thượng"], "answer": "Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp, kiểm soát"},
    {"question": "Nhà nước pháp quyền XHCN Việt Nam đặt dưới sự lãnh đạo của:", "options": ["Quốc hội", "Đảng Cộng sản Việt Nam", "Chủ tịch nước", "Nhân dân"], "answer": "Đảng Cộng sản Việt Nam"},
    {"question": "Trong Nhà nước pháp quyền XHCN Việt Nam, vị trí của Hiến pháp và pháp luật là:", "options": ["Thứ yếu", "Tối thượng", "Phụ thuộc chính sách", "Tùy nghi"], "answer": "Tối thượng"},
    {"question": "Mục tiêu của Nhà nước pháp quyền XHCN Việt Nam là:", "options": ["Phục vụ nhân dân, vì lợi ích của nhân dân", "Phục vụ giai cấp thống trị", "Bảo vệ quyền lợi tư bản", "Duy trì quyền lực nhà nước"], "answer": "Phục vụ nhân dân, vì lợi ích của nhân dân"},
    {"question": "Quyền lực nhà nước được phân công thành các nhánh nào?", "options": ["Lập pháp, hành pháp, tư pháp", "Kinh tế, chính trị, văn hóa", "Trung ương, địa phương, cơ sở", "Đảng, Nhà nước, Đoàn thể"], "answer": "Lập pháp, hành pháp, tư pháp"},
    {"question": "Đại hội nào của Đảng khẳng định quyền lực nhà nước là thống nhất nhưng có sự 'kiểm soát' giữa các cơ quan?", "options": ["Đại hội X", "Đại hội XI", "Đại hội XII", "Đại hội IX"], "answer": "Đại hội XII"},
    {"question": "Giải pháp để phát huy dân chủ XHCN ở Việt Nam là:", "options": ["Xây dựng thể chế kinh tế thị trường định hướng XHCN", "Xây dựng Đảng trong sạch vững mạnh", "Nâng cao vai trò các tổ chức chính trị - xã hội", "Cả a, b và c"], "answer": "Cả a, b và c"},
    {"question": "Để xây dựng Nhà nước pháp quyền, cần đẩy mạnh cải cách gì?", "options": ["Cải cách ruộng đất", "Cải cách hành chính", "Cải cách tôn giáo", "Cải cách quân đội"], "answer": "Cải cách hành chính"},
    {"question": "Nhà nước pháp quyền XHCN Việt Nam tôn trọng và bảo vệ:", "options": ["Quyền con người, quyền công dân", "Đặc quyền giai cấp", "Lợi ích nhóm", "Quyền lực tuyệt đối"], "answer": "Quyền con người, quyền công dân"},
    {"question": "Cơ sở kinh tế của dân chủ XHCN là:", "options": ["Chế độ tư hữu", "Chế độ công hữu về tư liệu sản xuất", "Kinh tế tự nhiên", "Kinh tế chỉ huy"], "answer": "Chế độ công hữu về tư liệu sản xuất"},
    {"question": "Dân chủ là bản chất của chế độ nào?", "options": ["Phong kiến", "Chiếm hữu nô lệ", "Xã hội chủ nghĩa", "Phát xít"], "answer": "Xã hội chủ nghĩa"},
    {"question": "Mối quan hệ giữa Đảng lãnh đạo, Nhà nước quản lý, Nhân dân làm chủ gọi là:", "options": ["Cơ chế thị trường", "Cơ chế tổng thể của hệ thống chính trị", "Quy luật giá trị", "Nguyên tắc tập trung"], "answer": "Cơ chế tổng thể của hệ thống chính trị"},
    {"question": "Một trong những trở ngại đối với việc thực hiện dân chủ ở nước ta là:", "options": ["Kinh tế phát triển quá nhanh", "Âm mưu 'diễn biến hòa bình' của các thế lực thù địch", "Dân trí quá cao", "Hội nhập quốc tế"], "answer": "Âm mưu 'diễn biến hòa bình' của các thế lực thù địch"},
    {"question": "Giám sát và phản biện xã hội là vai trò của:", "options": ["Chính phủ", "Mặt trận Tổ quốc và các tổ chức chính trị - xã hội", "Tòa án", "Công an"], "answer": "Mặt trận Tổ quốc và các tổ chức chính trị - xã hội"}
]

# Chapter 4: Cơ cấu xã hội và Liên minh giai cấp
qs_04 = [
    {"question": "Trong thời kỳ quá độ lên CNXH, cơ cấu xã hội - giai cấp biến đổi theo quy luật nào?", "options": ["Biến đổi ngẫu nhiên", "Bị chi phối bởi biến đổi cơ cấu kinh tế", "Do ý muốn chủ quan", "Không thay đổi"], "answer": "Bị chi phối bởi biến đổi cơ cấu kinh tế"},
    {"question": "Cơ cấu xã hội - giai cấp ở Việt Nam thời kỳ quá độ bao gồm những lực lượng nào?", "options": ["Công nhân, nông dân, tư sản", "Công nhân, nông dân, trí thức, doanh nhân", "Chủ nô, nô lệ", "Lãnh chúa, nông nô"], "answer": "Công nhân, nông dân, trí thức, doanh nhân"},
    {"question": "Giai cấp nào giữ vai trò lãnh đạo cách mạng Việt Nam?", "options": ["Giai cấp nông dân", "Giai cấp công nhân", "Đội ngũ trí thức", "Đội ngũ doanh nhân"], "answer": "Giai cấp công nhân"},
    {"question": "Đặc điểm nổi bật của cơ cấu xã hội - giai cấp trong thời kỳ quá độ là:", "options": ["Sự đa dạng và phức tạp", "Sự thuần nhất", "Chỉ còn một giai cấp", "Không còn phân hóa giàu nghèo"], "answer": "Sự đa dạng và phức tạp"},
    {"question": "Vị trí chiến lược của giai cấp nông dân là trong lĩnh vực nào?", "options": ["Công nghiệp hóa", "Nông nghiệp, nông thôn, xây dựng nông thôn mới", "Thương mại dịch vụ", "Khoa học công nghệ"], "answer": "Nông nghiệp, nông thôn, xây dựng nông thôn mới"},
    {"question": "Lực lượng lao động sáng tạo đặc biệt quan trọng trong tiến trình công nghiệp hóa, hiện đại hóa là:", "options": ["Giai cấp công nhân", "Giai cấp nông dân", "Đội ngũ trí thức", "Đội ngũ doanh nhân"], "answer": "Đội ngũ trí thức"},
    {"question": "Đội ngũ doanh nhân có vai trò gì trong thời kỳ quá độ?", "options": ["Phát triển kinh tế, giải quyết việc làm", "Lãnh đạo chính trị", "Sản xuất nông nghiệp", "Nghiên cứu khoa học"], "answer": "Phát triển kinh tế, giải quyết việc làm"},
    {"question": "Liên minh giai cấp, tầng lớp trong thời kỳ quá độ là sự liên kết giữa:", "options": ["Công nhân với tư sản", "Công nhân, nông dân và trí thức", "Nông dân với địa chủ", "Trí thức với tư bản"], "answer": "Công nhân, nông dân và trí thức"},
    {"question": "Nội dung cơ bản quyết định nhất của liên minh giai cấp là:", "options": ["Nội dung chính trị", "Nội dung kinh tế", "Nội dung văn hóa", "Nội dung tư tưởng"], "answer": "Nội dung kinh tế"},
    {"question": "Trong nội dung kinh tế, nhiệm vụ trọng tâm của liên minh là:", "options": ["Đấu tranh giai cấp", "Phát triển kinh tế nhanh và bền vững, CNH-HĐH", "Chia lại ruộng đất", "Tăng thuế"], "answer": "Phát triển kinh tế nhanh và bền vững, CNH-HĐH"},
    {"question": "Nội dung chính trị của liên minh giai cấp thể hiện ở:", "options": ["Giữ vững lập trường chính trị của giai cấp công nhân và vai trò lãnh đạo của Đảng", "Chia sẻ quyền lực cho các đảng phái", "Thực hiện đa nguyên chính trị", "Tập trung quyền lực vào nông dân"], "answer": "Giữ vững lập trường chính trị của giai cấp công nhân và vai trò lãnh đạo của Đảng"},
    {"question": "Cơ sở để thực hiện liên minh giai cấp về mặt chính trị - xã hội là:", "options": ["Khối đại đoàn kết toàn dân", "Mâu thuẫn đối kháng", "Sự tách biệt các giai cấp", "Lợi ích cục bộ"], "answer": "Khối đại đoàn kết toàn dân"},
    {"question": "Nội dung văn hóa - xã hội của liên minh nhằm mục tiêu:", "options": ["Xây dựng nền văn hóa tiên tiến, đậm đà bản sắc dân tộc", "Xóa bỏ văn hóa truyền thống", "Tiếp thu văn hóa phương Tây không chọn lọc", "Duy trì hủ tục lạc hậu"], "answer": "Xây dựng nền văn hóa tiên tiến, đậm đà bản sắc dân tộc"},
    {"question": "Xu hướng biến đổi của giai cấp nông dân trong thời kỳ quá độ là:", "options": ["Tăng nhanh về số lượng", "Giảm dần về số lượng và tỷ lệ", "Giữ nguyên số lượng", "Trở thành giai cấp thống trị"], "answer": "Giảm dần về số lượng và tỷ lệ"},
    {"question": "Để củng cố khối liên minh, cần hoàn thiện thể chế nào?", "options": ["Kinh tế bao cấp", "Kinh tế thị trường định hướng XHCN", "Kinh tế tư bản chủ nghĩa", "Kinh tế phong kiến"], "answer": "Kinh tế thị trường định hướng XHCN"},
    {"question": "Nguyên tắc cơ bản của liên minh giai cấp là:", "options": ["Đảm bảo lợi ích của các bên", "Lợi ích chỉ thuộc về công nhân", "Lợi ích chỉ thuộc về nông dân", "Ép buộc tham gia"], "answer": "Đảm bảo lợi ích của các bên"},
    {"question": "Vai trò của đội ngũ trí thức ngày càng tăng do:", "options": ["Yêu cầu của kinh tế tri thức và CM công nghiệp 4.0", "Sự suy giảm của công nhân", "Yêu cầu của nông nghiệp", "Chính sách ưu đãi"], "answer": "Yêu cầu của kinh tế tri thức và CM công nghiệp 4.0"},
    {"question": "Một trong những giải pháp xây dựng cơ cấu xã hội - giai cấp là:", "options": ["Hạn chế sự phát triển xã hội", "Đẩy mạnh CNH, HĐH", "Duy trì kinh tế tiểu nông", "Ngăn cản chuyển dịch cơ cấu"], "answer": "Đẩy mạnh CNH, HĐH"},
    {"question": "Khối liên minh công - nông - trí thức là nền tảng của:", "options": ["Nhà nước pháp quyền XHCN", "Kinh tế tư nhân", "Xã hội dân sự", "Thị trường chứng khoán"], "answer": "Nhà nước pháp quyền XHCN"},
    {"question": "Sự biến đổi cơ cấu xã hội - giai cấp ở Việt Nam diễn ra trong nội bộ:", "options": ["Chỉ giai cấp công nhân", "Từng giai cấp, tầng lớp cơ bản", "Chỉ giai cấp nông dân", "Chỉ đội ngũ doanh nhân"], "answer": "Từng giai cấp, tầng lớp cơ bản"},
    {"question": "Yếu tố nào là động lực chủ yếu của sự phát triển đất nước?", "options": ["Đại đoàn kết toàn dân tộc", "Đấu tranh giai cấp", "Mâu thuẫn nội bộ", "Viện trợ nước ngoài"], "answer": "Đại đoàn kết toàn dân tộc"},
    {"question": "Để phát triển đội ngũ doanh nhân, cần tạo môi trường gì?", "options": ["Hạn chế kinh doanh", "Thuận lợi cho sản xuất kinh doanh", "Bao cấp hoàn toàn", "Cạnh tranh không lành mạnh"], "answer": "Thuận lợi cho sản xuất kinh doanh"},
    {"question": "Trong liên minh, giai cấp công nhân giữ vai trò:", "options": ["Lãnh đạo", "Phụ thuộc", "Trung gian", "Đối lập"], "answer": "Lãnh đạo"},
    {"question": "Mục tiêu của liên minh giai cấp là:", "options": ["Dân giàu, nước mạnh, dân chủ, công bằng, văn minh", "Lợi ích nhóm", "Quyền lợi cá nhân", "Bảo vệ chế độ cũ"], "answer": "Dân giàu, nước mạnh, dân chủ, công bằng, văn minh"},
    {"question": "Sự chuyển dịch cơ cấu kinh tế sẽ dẫn đến:", "options": ["Sự chuyển dịch cơ cấu xã hội - giai cấp", "Sự cố định cơ cấu xã hội", "Sự biến mất của giai cấp", "Sự hình thành giai cấp bóc lột mới"], "answer": "Sự chuyển dịch cơ cấu xã hội - giai cấp"},
    {"question": "Liên minh giai cấp là vấn đề mang tính:", "options": ["Chiến thuật nhất thời", "Chiến lược lâu dài", "Thủ đoạn chính trị", "Hình thức"], "answer": "Chiến lược lâu dài"},
    {"question": "Trong thời kỳ quá độ, mâu thuẫn giữa các giai cấp trong khối liên minh là:", "options": ["Mâu thuẫn đối kháng", "Mâu thuẫn không đối kháng", "Mâu thuẫn không thể giải quyết", "Mâu thuẫn triệt để"], "answer": "Mâu thuẫn không đối kháng"},
    {"question": "Việc thực hiện tốt chính sách xã hội đối với các giai cấp nhằm:", "options": ["Tạo sự đồng thuận và động lực phát triển", "Gây chia rẽ", "Làm nghèo đất nước", "Hạn chế tự do"], "answer": "Tạo sự đồng thuận và động lực phát triển"},
    {"question": "Đẩy mạnh ứng dụng khoa học công nghệ vào sản xuất là nội dung của liên minh về:", "options": ["Chính trị", "Kinh tế", "Văn hóa", "An ninh"], "answer": "Kinh tế"},
    {"question": "Vai trò của Mặt trận Tổ quốc Việt Nam trong khối liên minh là:", "options": ["Lãnh đạo", "Quản lý", "Tập hợp, xây dựng khối đại đoàn kết", "Trấn áp"], "answer": "Tập hợp, xây dựng khối đại đoàn kết"},
    {"question": "Xây dựng nông thôn mới là nhiệm vụ trực tiếp của:", "options": ["Giai cấp công nhân", "Giai cấp nông dân", "Trí thức", "Doanh nhân"], "answer": "Giai cấp nông dân"},
    {"question": "Trí thức hóa giai cấp công nhân là xu hướng:", "options": ["Tất yếu trong cách mạng công nghiệp 4.0", "Không cần thiết", "Làm mất bản chất công nhân", "Chỉ diễn ra ở nước phát triển"], "answer": "Tất yếu trong cách mạng công nghiệp 4.0"},
    {"question": "Sự phát triển của kinh tế nhiều thành phần làm cho cơ cấu xã hội:", "options": ["Đơn giản đi", "Phức tạp và đa dạng hơn", "Không thay đổi", "Trở nên đồng nhất"], "answer": "Phức tạp và đa dạng hơn"},
    {"question": "Việc giải quyết việc làm và xóa đói giảm nghèo góp phần:", "options": ["Ổn định cơ cấu xã hội", "Gây bất ổn", "Tăng khoảng cách giàu nghèo", "Kìm hãm phát triển"], "answer": "Ổn định cơ cấu xã hội"},
    {"question": "Liên minh công - nông - trí thức là cơ sở để:", "options": ["Bảo vệ chế độ chính trị", "Phát triển kinh tế thị trường", "Giữ gìn bản sắc văn hóa", "Cả a, b và c"], "answer": "Cả a, b và c"},
    {"question": "Giai cấp nào là lực lượng nòng cốt trong khối liên minh?", "options": ["Công nhân", "Nông dân", "Trí thức", "Tư sản"], "answer": "Công nhân"},
    {"question": "Mối quan hệ giữa các giai cấp trong thời kỳ quá độ là:", "options": ["Hợp tác và đấu tranh trong nội bộ nhân dân", "Đấu tranh một mất một còn", "Hợp tác vô điều kiện", "Không có quan hệ gì"], "answer": "Hợp tác và đấu tranh trong nội bộ nhân dân"},
    {"question": "Để phát huy vai trò của thế hệ trẻ, cần:", "options": ["Giáo dục chính trị, tư tưởng, đạo đức", "Hạn chế tiếp cận thông tin", "Bắt buộc lao động sớm", "Không cần quan tâm"], "answer": "Giáo dục chính trị, tư tưởng, đạo đức"},
    {"question": "Phụ nữ có vai trò quan trọng trong:", "options": ["Gia đình và xã hội", "Chỉ trong gia đình", "Chỉ trong xã hội", "Không có vai trò gì"], "answer": "Gia đình và xã hội"},
    {"question": "Chính sách đối với giai cấp công nhân cần tập trung vào:", "options": ["Nâng cao trình độ, đời sống, bảo vệ quyền lợi", "Giảm lương", "Tăng giờ làm", "Hạn chế quyền lợi"], "answer": "Nâng cao trình độ, đời sống, bảo vệ quyền lợi"},
    {"question": "Xây dựng đội ngũ trí thức vững mạnh là để:", "options": ["Nâng tầm trí tuệ dân tộc", "Làm cảnh", "Đối trọng với công nhân", "Phục vụ nước ngoài"], "answer": "Nâng tầm trí tuệ dân tộc"},
    {"question": "Sự biến đổi cơ cấu xã hội ở Việt Nam mang tính:", "options": ["Quy luật phổ biến và đặc thù", "Ngẫu nhiên", "Chủ quan", "Cưỡng bức"], "answer": "Quy luật phổ biến và đặc thù"},
    {"question": "Khối đại đoàn kết toàn dân tộc dựa trên nền tảng:", "options": ["Liên minh công - nông - trí thức", "Liên minh công - tư", "Liên minh nông - tư", "Liên minh trí - tư"], "answer": "Liên minh công - nông - trí thức"},
    {"question": "Đổi mới hoạt động của Đảng và Nhà nước nhằm:", "options": ["Tăng cường khối liên minh", "Chia rẽ khối liên minh", "Làm suy yếu khối liên minh", "Thay thế khối liên minh"], "answer": "Tăng cường khối liên minh"}
]

# Chapter 5: Tôn giáo
qs_05 = [
    {"question": "Theo quan điểm Mác - Lênin, tôn giáo là:", "options": ["Một thực thể siêu nhiên", "Một hình thái ý thức xã hội phản ánh hư ảo hiện thực", "Chân lý tuyệt đối", "Khoa học về thần linh"], "answer": "Một hình thái ý thức xã hội phản ánh hư ảo hiện thực"},
    {"question": "Nguồn gốc tự nhiên của tôn giáo là do:", "options": ["Sự bất lực của con người trước sức mạnh tự nhiên", "Sự áp bức giai cấp", "Sự sợ hãi trước cái chết", "Trình độ văn hóa cao"], "answer": "Sự bất lực của con người trước sức mạnh tự nhiên"},
    {"question": "Nguồn gốc nhận thức của tôn giáo là:", "options": ["Sự tuyệt đối hóa cái chủ quan, biến cái khách quan thành siêu nhiên", "Sự hiểu biết tường tận về thế giới", "Sự phát triển của khoa học", "Sự giác ngộ chân lý"], "answer": "Sự tuyệt đối hóa cái chủ quan, biến cái khách quan thành siêu nhiên"},
    {"question": "Nguồn gốc tâm lý của tôn giáo bao gồm:", "options": ["Sự sợ hãi, may rủi, tình cảm, lòng biết ơn", "Sự dũng cảm", "Sự thờ ơ", "Sự căm ghét"], "answer": "Sự sợ hãi, may rủi, tình cảm, lòng biết ơn"},
    {"question": "Tính chất của tôn giáo bao gồm:", "options": ["Tính lịch sử, tính quần chúng, tính chính trị", "Tính giai cấp, tính nhân dân, tính dân tộc", "Tính khoa học, tính thực tiễn, tính sáng tạo", "Tính vĩnh viễn, tính bất biến, tính độc lập"], "answer": "Tính lịch sử, tính quần chúng, tính chính trị"},
    {"question": "Tôn giáo mang tính chính trị khi:", "options": ["Xã hội chưa có giai cấp", "Xã hội đã phân chia giai cấp và có đối kháng", "Xã hội công sản nguyên thủy", "Mọi người đều bình đẳng"], "answer": "Xã hội đã phân chia giai cấp và có đối kháng"},
    {"question": "Quan điểm của chủ nghĩa Mác - Lênin về sự tồn tại của tôn giáo:", "options": ["Tôn giáo sẽ mất đi ngay lập tức khi có CNXH", "Tôn giáo sẽ tồn tại lâu dài", "Tôn giáo là vĩnh cửu", "Cần dùng hành chính để xóa bỏ tôn giáo"], "answer": "Tôn giáo sẽ tồn tại lâu dài"},
    {"question": "Nguyên tắc giải quyết vấn đề tôn giáo là:", "options": ["Tôn trọng tự do tín ngưỡng, theo hoặc không theo", "Cấm đoán mọi tôn giáo", "Bắt buộc theo một tôn giáo", "Khuyến khích mê tín dị đoan"], "answer": "Tôn trọng tự do tín ngưỡng, theo hoặc không theo"},
    {"question": "Để khắc phục ảnh hưởng tiêu cực của tôn giáo, cần:", "options": ["Cải tạo xã hội cũ, xây dựng xã hội mới", "Dùng biện pháp hành chính", "Cấm các hoạt động lễ hội", "Trục xuất chức sắc"], "answer": "Cải tạo xã hội cũ, xây dựng xã hội mới"},
    {"question": "Cần phân biệt hai mặt nào trong vấn đề tôn giáo?", "options": ["Mặt chính trị và mặt tư tưởng", "Mặt kinh tế và mặt văn hóa", "Mặt nội dung và mặt hình thức", "Mặt tích cực và mặt tiêu cực"], "answer": "Mặt chính trị và mặt tư tưởng"},
    {"question": "Việt Nam là một quốc gia:", "options": ["Đa tôn giáo", "Đơn tôn giáo", "Không có tôn giáo", "Chỉ có Phật giáo"], "answer": "Đa tôn giáo"},
    {"question": "Đặc điểm quan hệ giữa các tôn giáo ở Việt Nam là:", "options": ["Xung đột gay gắt", "Chung sống hòa bình, đoàn kết", "Tách biệt hoàn toàn", "Cạnh tranh khốc liệt"], "answer": "Chung sống hòa bình, đoàn kết"},
    {"question": "Tín đồ các tôn giáo ở Việt Nam phần lớn là:", "options": ["Nhân dân lao động", "Tầng lớp thượng lưu", "Người nước ngoài", "Chức sắc tôn giáo"], "answer": "Nhân dân lao động"},
    {"question": "Chính sách nhất quán của Đảng và Nhà nước ta về tôn giáo là:", "options": ["Đại đoàn kết dân tộc, tôn trọng tự do tín ngưỡng", "Bài trừ tôn giáo", "Phân biệt đối xử", "Khuyến khích xung đột"], "answer": "Đại đoàn kết dân tộc, tôn trọng tự do tín ngưỡng"},
    {"question": "Công tác tôn giáo là trách nhiệm của:", "options": ["Riêng ngành công an", "Riêng Mặt trận Tổ quốc", "Cả hệ thống chính trị", "Riêng các chức sắc"], "answer": "Cả hệ thống chính trị"},
    {"question": "Nội dung cốt lõi của công tác tôn giáo là:", "options": ["Công tác vận động quần chúng", "Công tác quản lý hành chính", "Công tác xây dựng cơ sở thờ tự", "Công tác đào tạo chức sắc"], "answer": "Công tác vận động quần chúng"},
    {"question": "Mê tín dị đoan là:", "options": ["Niềm tin tôn giáo chân chính", "Niềm tin mê muội, cuồng tín, dẫn đến hành vi cực đoan", "Văn hóa truyền thống", "Khoa học tâm linh"], "answer": "Niềm tin mê muội, cuồng tín, dẫn đến hành vi cực đoan"},
    {"question": "Tín ngưỡng và tôn giáo:", "options": ["Là một", "Có sự giao thoa nhất định nhưng không đồng nhất", "Hoàn toàn khác biệt", "Đối lập nhau"], "answer": "Có sự giao thoa nhất định nhưng không đồng nhất"},
    {"question": "Khi giải quyết vấn đề tôn giáo cần có quan điểm:", "options": ["Lịch sử cụ thể", "Chủ quan duy ý chí", "Phi lịch sử", "Cứng nhắc"], "answer": "Lịch sử cụ thể"},
    {"question": "Các tôn giáo ở Việt Nam đều có quan hệ với:", "options": ["Các tổ chức quốc tế", "Chỉ trong nước", "Chỉ khu vực ASEAN", "Không có quan hệ quốc tế"], "answer": "Các tổ chức quốc tế"},
    {"question": "Việc theo đạo hay không theo đạo là quyền của:", "options": ["Gia đình", "Mỗi công dân", "Nhà nước", "Giáo hội"], "answer": "Mỗi công dân"},
    {"question": "Mặt chính trị trong tôn giáo phản ánh mối quan hệ giữa:", "options": ["Các tín đồ", "Tiến bộ và phản tiến bộ, mâu thuẫn giai cấp", "Thần linh và con người", "Các giáo lý"], "answer": "Tiến bộ và phản tiến bộ, mâu thuẫn giai cấp"},
    {"question": "Mặt tư tưởng trong tôn giáo phản ánh:", "options": ["Mâu thuẫn đối kháng", "Sự khác nhau về niềm tin", "Xung đột chính trị", "Lợi ích kinh tế"], "answer": "Sự khác nhau về niềm tin"},
    {"question": "Nhà nước XHCN đối với các tôn giáo:", "options": ["Bảo hộ các tôn giáo hoạt động đúng pháp luật", "Không quan tâm", "Cấm đoán", "Tài trợ toàn bộ"], "answer": "Bảo hộ các tôn giáo hoạt động đúng pháp luật"},
    {"question": "Mục tiêu của đoàn kết đồng bào tôn giáo là:", "options": ["Dân giàu, nước mạnh, dân chủ, công bằng, văn minh", "Phát triển tôn giáo", "Xóa bỏ tôn giáo", "Thống nhất giáo lý"], "answer": "Dân giàu, nước mạnh, dân chủ, công bằng, văn minh"},
    {"question": "Hoạt động lợi dụng tôn giáo để chống phá nhà nước bị:", "options": ["Nghiêm cấm", "Khuyến khích", "Làm ngơ", "Bảo vệ"], "answer": "Nghiêm cấm"},
    {"question": "Tôn giáo là nhu cầu tinh thần của:", "options": ["Một bộ phận nhân dân", "Toàn thể nhân dân", "Giai cấp thống trị", "Người lạc hậu"], "answer": "Một bộ phận nhân dân"},
    {"question": "Trong xu thế toàn cầu hóa, việc giải quyết vấn đề tôn giáo cần:", "options": ["Kết hợp ngoại giao và bảo vệ chủ quyền", "Đóng cửa biên giới", "Chấp nhận mọi yêu cầu quốc tế", "Cắt đứt quan hệ"], "answer": "Kết hợp ngoại giao và bảo vệ chủ quyền"},
    {"question": "Hiện tượng 'đạo lạ' cần được:", "options": ["Cảnh giác và quản lý", "Ủng hộ", "Tự do phát triển", "Không quan tâm"], "answer": "Cảnh giác và quản lý"},
    {"question": "Tôn giáo phản ánh hiện thực khách quan một cách:", "options": ["Chính xác", "Khoa học", "Hư ảo", "Biện chứng"], "answer": "Hư ảo"}
]

# Chapter 6: Gia đình
qs_06 = [
    {"question": "Khái niệm gia đình dựa trên những mối quan hệ cơ bản nào?", "options": ["Hôn nhân và huyết thống", "Kinh tế và chính trị", "Bạn bè và đồng nghiệp", "Láng giềng và cộng đồng"], "answer": "Hôn nhân và huyết thống"},
    {"question": "Ngoài hôn nhân và huyết thống, gia đình còn có thể hình thành từ quan hệ nào?", "options": ["Quan hệ nuôi dưỡng (cha mẹ nuôi - con nuôi)", "Quan hệ thầy trò", "Quan hệ chủ tớ", "Quan hệ mua bán"], "answer": "Quan hệ nuôi dưỡng (cha mẹ nuôi - con nuôi)"},
    {"question": "Vị trí của gia đình trong xã hội được ví như:", "options": ["Tế bào của xã hội", "Bộ não của xã hội", "Trái tim của xã hội", "Cánh tay của xã hội"], "answer": "Tế bào của xã hội"},
    {"question": "Gia đình là cầu nối giữa:", "options": ["Cá nhân với xã hội", "Nhà nước với Đảng", "Quá khứ với tương lai", "Kinh tế với chính trị"], "answer": "Cá nhân với xã hội"},
    {"question": "Chức năng đặc thù, riêng có của gia đình là:", "options": ["Tái sản xuất ra con người", "Phát triển kinh tế", "Giáo dục", "Vui chơi giải trí"], "answer": "Tái sản xuất ra con người"},
    {"question": "Chức năng tái sản xuất ra con người đáp ứng nhu cầu gì?", "options": ["Duy trì nòi giống và sức lao động", "Tăng trưởng GDP", "Ổn định chính trị", "Giao lưu văn hóa"], "answer": "Duy trì nòi giống và sức lao động"},
    {"question": "Chức năng nuôi dưỡng, giáo dục của gia đình có ý nghĩa gì?", "options": ["Hình thành nhân cách, đạo đức, lối sống", "Cung cấp kiến thức chuyên môn sâu", "Thay thế nhà trường", "Thay thế xã hội"], "answer": "Hình thành nhân cách, đạo đức, lối sống"},
    {"question": "Chức năng kinh tế của gia đình bao gồm:", "options": ["Sản xuất và tiêu dùng", "Chỉ tiêu dùng", "Chỉ sản xuất", "Quản lý thị trường"], "answer": "Sản xuất và tiêu dùng"},
    {"question": "Cơ sở xây dựng gia đình trong thời kỳ quá độ lên CNXH là:", "options": ["Hôn nhân tự nguyện, tiến bộ, một vợ một chồng, bình đẳng", "Hôn nhân sắp đặt", "Hôn nhân vì lợi ích kinh tế", "Đa thê"], "answer": "Hôn nhân tự nguyện, tiến bộ, một vợ một chồng, bình đẳng"},
    {"question": "Hôn nhân tiến bộ dựa trên cơ sở chủ yếu là:", "options": ["Tình yêu", "Của hồi môn", "Địa vị xã hội", "Sắc đẹp"], "answer": "Tình yêu"},
    {"question": "Biến đổi quy mô gia đình Việt Nam hiện nay theo xu hướng:", "options": ["Thu nhỏ (gia đình hạt nhân)", "Mở rộng (tứ đại đồng đường)", "Gia đình bộ tộc", "Không thay đổi"], "answer": "Thu nhỏ (gia đình hạt nhân)"},
    {"question": "Sự thay đổi trong chức năng sinh đẻ hiện nay thể hiện ở:", "options": ["Chủ động sinh đẻ, giảm mức sinh", "Sinh con càng nhiều càng tốt", "Phải có con trai", "Không sinh con"], "answer": "Chủ động sinh đẻ, giảm mức sinh"},
    {"question": "Kinh tế gia đình đang chuyển biến từ tự cấp tự túc sang:", "options": ["Kinh tế hàng hóa", "Kinh tế bao cấp", "Kinh tế hái lượm", "Không sản xuất"], "answer": "Kinh tế hàng hóa"},
    {"question": "Thách thức đối với chức năng giáo dục của gia đình hiện nay là:", "options": ["Xung đột giá trị, khoảng cách thế hệ, thiếu thời gian", "Thiếu trường học", "Trẻ em không muốn học", "Nhà nước cấm đoán"], "answer": "Xung đột giá trị, khoảng cách thế hệ, thiếu thời gian"},
    {"question": "Trong gia đình Việt Nam hiện nay, vai trò người chủ gia đình có xu hướng:", "options": ["Bình đẳng hơn giữa vợ và chồng", "Tuyệt đối thuộc về người chồng", "Tuyệt đối thuộc về người vợ", "Thuộc về con cái"], "answer": "Bình đẳng hơn giữa vợ và chồng"},
    {"question": "Phong trào xây dựng gia đình văn hóa nhằm mục tiêu:", "options": ["Gia đình ấm no, hòa thuận, tiến bộ, hạnh phúc", "Gia đình giàu có nhất", "Gia đình đông con nhất", "Gia đình quyền lực nhất"], "answer": "Gia đình ấm no, hòa thuận, tiến bộ, hạnh phúc"},
    {"question": "Yếu tố nào tác động mạnh mẽ đến sự biến đổi của gia đình Việt Nam?", "options": ["Công nghiệp hóa, hiện đại hóa, kinh tế thị trường, toàn cầu hóa", "Chiến tranh", "Thiên tai", "Sự cô lập"], "answer": "Công nghiệp hóa, hiện đại hóa, kinh tế thị trường, toàn cầu hóa"},
    {"question": "Để xây dựng gia đình Việt Nam hiện nay, cần kế thừa:", "options": ["Giá trị truyền thống tốt đẹp", "Hủ tục lạc hậu", "Tư tưởng phong kiến", "Gia trưởng độc đoán"], "answer": "Giá trị truyền thống tốt đẹp"},
    {"question": "Gia đình là tổ ấm mang lại giá trị gì cho cá nhân?", "options": ["Hạnh phúc, sự hài hòa", "Sự giàu sang", "Quyền lực", "Danh tiếng"], "answer": "Hạnh phúc, sự hài hòa"},
    {"question": "Quan hệ hôn nhân là cơ sở pháp lý cho sự tồn tại của:", "options": ["Gia đình", "Dòng họ", "Làng xã", "Công ty"], "answer": "Gia đình"},
    {"question": "Chế độ hôn nhân một vợ một chồng là điều kiện để đảm bảo:", "options": ["Hạnh phúc gia đình và bình đẳng giới", "Sự giàu có", "Dòng dõi", "Quyền lực người chồng"], "answer": "Hạnh phúc gia đình và bình đẳng giới"},
    {"question": "Thực hiện thủ tục pháp lý trong hôn nhân nhằm:", "options": ["Bảo vệ quyền lợi của các thành viên", "Ngăn cản tự do", "Thu phí", "Kiểm soát dân số"], "answer": "Bảo vệ quyền lợi của các thành viên"},
    {"question": "Sự bình đẳng trong gia đình được hiểu là:", "options": ["Vợ chồng có nghĩa vụ và quyền lợi ngang nhau", "Vợ quyết định tất cả", "Chồng quyết định tất cả", "Con cái quyết định"], "answer": "Vợ chồng có nghĩa vụ và quyền lợi ngang nhau"},
    {"question": "Chức năng thỏa mãn nhu cầu tâm sinh lý, tình cảm có vai trò:", "options": ["Duy trì sự bền vững của gia đình", "Không quan trọng", "Chỉ là phụ", "Gây mâu thuẫn"], "answer": "Duy trì sự bền vững của gia đình"},
    {"question": "Mô hình gia đình nào đang trở nên phổ biến ở đô thị và nông thôn Việt Nam?", "options": ["Gia đình hạt nhân", "Gia đình truyền thống lớn", "Gia đình chung dòng họ", "Gia đình mẫu hệ"], "answer": "Gia đình hạt nhân"},
    {"question": "Tác động tiêu cực của cơ chế thị trường đến gia đình là:", "options": ["Quan hệ tình cảm lỏng lẻo, thực dụng", "Tăng thu nhập", "Mở rộng giao lưu", "Nâng cao dân trí"], "answer": "Quan hệ tình cảm lỏng lẻo, thực dụng"},
    {"question": "Để phát triển kinh tế gia đình, Nhà nước cần:", "options": ["Có chính sách hỗ trợ, vay vốn, chuyển giao công nghệ", "Cấm kinh doanh", "Đánh thuế cao", "Không can thiệp"], "answer": "Có chính sách hỗ trợ, vay vốn, chuyển giao công nghệ"},
    {"question": "Tiêu chí gia đình văn hóa phải:", "options": ["Phù hợp và thiết thực", "Chạy theo thành tích", "Cứng nhắc", "Khó thực hiện"], "answer": "Phù hợp và thiết thực"},
    {"question": "Sự biến đổi chức năng kinh tế của gia đình từ tự cấp sang hàng hóa làm cho:", "options": ["Gia đình trở thành một bộ phận quan trọng của nền kinh tế quốc dân", "Gia đình bị cô lập", "Gia đình nghèo đi", "Gia đình mất chức năng"], "answer": "Gia đình trở thành một bộ phận quan trọng của nền kinh tế quốc dân"},
    {"question": "Giáo dục gia đình cần kết hợp chặt chẽ với:", "options": ["Giáo dục nhà trường và xã hội", "Giáo dục tôn giáo", "Giáo dục trực tuyến", "Tự học"], "answer": "Giáo dục nhà trường và xã hội"},
    {"question": "Trách nhiệm của cấp ủy, chính quyền đối với công tác gia đình là:", "options": ["Đưa vào chiến lược phát triển kinh tế - xã hội", "Không quan tâm", "Giao khoán cho đoàn thể", "Chỉ tuyên truyền miệng"], "answer": "Đưa vào chiến lược phát triển kinh tế - xã hội"},
    {"question": "Quan hệ giữa lợi ích gia đình và lợi ích xã hội trong CNXH là:", "options": ["Thống nhất", "Đối kháng", "Mâu thuẫn gay gắt", "Tách biệt"], "answer": "Thống nhất"},
    {"question": "Vấn đề bình đẳng giới trong gia đình hiện nay cần chú trọng:", "options": ["Thay đổi tâm lý truyền thống trọng nam khinh nữ", "Ưu tiên nữ giới tuyệt đối", "Ưu tiên nam giới", "Duy trì nề nếp cũ"], "answer": "Thay đổi tâm lý truyền thống trọng nam khinh nữ"},
    {"question": "Gia đình đơn thân, sống thử, kết hôn đồng tính là biểu hiện của:", "options": ["Sự biến đổi và đa dạng hóa các hình thức gia đình", "Sự suy đồi", "Sự tiến bộ tuyệt đối", "Truyền thống"], "answer": "Sự biến đổi và đa dạng hóa các hình thức gia đình"},
    {"question": "Chức năng nào của gia đình quyết định mật độ dân cư?", "options": ["Tái sản xuất ra con người", "Kinh tế", "Giáo dục", "Văn hóa"], "answer": "Tái sản xuất ra con người"}
]

# Apply to files
append_questions("quiz_02_nha_nuoc_xhcn.json", qs_02)
append_questions("quiz_03_dan_chu_xhcn_va_nha_nuoc_phap_quyen.json", qs_03)
append_questions("quiz_04_co_cau_xa_hoi_va_lien_minh_giai_cap.json", qs_04)
append_questions("quiz_05_ton_giao.json", qs_05)
append_questions("quiz_06_gia_dinh.json", qs_06)
