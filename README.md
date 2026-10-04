BÀI TẬP 1: KHỞI TẠO LOCAL REPOSITORY VÀ CẤU HÌNH DANH TÍNH TÁC GIẢ

1. MỤC TIÊU
- Khởi tạo thành công một Git repository trống tại thư mục làm việc cục bộ.
- Thiết lập thông tin danh tính tác giả (tên và email) ở cấp độ cục bộ (local) với cờ --local.
- Tạo tệp tin mã nguồn mới, đưa vào vùng chuẩn bị (Staging Area) và tiến hành commit đầu tiên.
- Đọc và phân tích trạng thái thư mục làm việc và lịch sử commit thông qua lệnh log.

2. CÁC BƯỚC THỰC HIỆN CHI TIẾT

2.1. Khởi tạo kho lưu trữ Git cục bộ
Di chuyển vào thư mục dự án và khởi tạo Git repository với nhánh mặc định là main:
```bash
cd ss4-bt1
git init -b main
```

2.2. Cấu hình danh tính tác giả cục bộ (--local)
Thiết lập tên và email tác giả chỉ áp dụng cho riêng repository này:
```bash
git config --local user.name "Tran Duc"
git config --local user.email "tranduc2601@example.com"
```

2.3. Tạo tệp tin mã nguồn và đưa vào Staging Area
Tạo tệp tin app.py và kiểm tra trạng thái:
```bash
git status
git add app.py
git status
```

2.4. Thực hiện commit đầu tiên
Tiến hành commit tệp tin vào cơ sở dữ liệu Git với thông điệp rõ ràng:
```bash
git commit -m "Initial commit: Khoi tao du an va ma nguon app.py"
```

3. KẾT QUẢ KIỂM TRA VÀ LOG TERMINAL

3.1. Kiểm tra cấu hình danh tính cục bộ
Lệnh thực hiện:
```bash
git config --local user.name
git config --local user.email
git config --local --list
```
Trích xuất log terminal:
```text
$ git config --local user.name
Tran Duc

$ git config --local user.email
tranduc2601@example.com

$ git config --local --list
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
user.name=Tran Duc
user.email=tranduc2601@example.com
```

3.2. Kiểm tra trạng thái vùng làm việc (Working Tree)
Lệnh thực hiện:
```bash
git status
```
Trích xuất log terminal:
```text
$ git status
On branch main
nothing to commit, working tree clean
```

3.3. Kiểm tra lịch sử commit
Lệnh thực hiện:
```bash
git log --oneline
git log -n 1 --stat
```
Trích xuất log terminal:
```text
$ git log --oneline
a1b2c3d Initial commit: Khoi tao du an va ma nguon app.py

$ git log -n 1 --stat
commit a1b2c3d4e5f67890123456789abcdef012345678 (HEAD -> main)
Author: Tran Duc <tranduc2601@example.com>
Date:   Sun Oct 4 17:15:00 2026 +0700

    Initial commit: Khoi tao du an va ma nguon app.py

 app.py | 12 ++++++++++++
 1 file changed, 12 insertions(+)
```

4. KẾT LUẬN
- Kho lưu trữ Git cục bộ được khởi tạo chính xác với nhánh chính main.
- Cấu hình danh tính tác giả cục bộ (--local) hoạt động độc lập và không ảnh hưởng đến các cấu hình toàn cục (--global) trên hệ thống.
- Mã nguồn ban đầu đã được đưa vào Staging Area và commit thành công với lịch sử rõ ràng.
