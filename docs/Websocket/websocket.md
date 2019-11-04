# Tìm hiểu về Websocket
- Trước khi bạn có thể hiểu được công nghệ này, bạn cần có cái nhìn cơ bản về lưu lượng truy cập web HTTP trước.
## Regular HTTP:
1. Một client yếu cầu một trang web từ một server
2. Server tính toán phản hồi
3. Server gửi lại phản hồi cho client

<img src="https://i.imgur.com/ILQ6h9H.png">

## Ajax Polling:
1. Client gửi request liên tục lên server sử dụng HTTP
2. Client nhận trang web yêu cầu và thực thi JavaScript trên trang yêu cầu 1 file từ server theo khoảng thời gian liên tục và đều đặn (ví dụ: 0,5 giây).
3. Server tính toán mỗi phản hồi và gửi lại cho client, tương tự như lưu lượng HTTP bình thường

<img src="https://i.imgur.com/RnPooLD.png">

## Ajax Long-Polling:
1. Client gửi request liên tục lên server sử dụng HTTP
2. Client nhận trang web yêu cầu và thực thi JavaScript trên trang yêu cầu 1 file từ server
3. Server sẽ không phản hồi ngay khi nhận được được request mà nó chờ cho đến khi có dữ liệu mới
4. Khi có dữ liệu mới, Server phản hồi lại Client bằng dữ liệu mới đó
5. Client nhận dữ liệu mới và gửi ngay request khác đến Server, khởi động lại tiến trình

<img src="https://i.imgur.com/1k3RF62.png">

## HTML5 Server Sent Events (SSE) / EventSource:
1. Client gửi request liên tục lên server sử dụng HTTP
2. Client nhận trang web yêu cầu và thực thi JavaScript trên trang yêu cầu và mở một kết nối với server
3. Server gửi lại một sự kiện về Client khi có dữ liệu mới
	- Lưu lượng real-time từ server về client
	- Bạn sẽ sử dụng server có một vòng lặp
	- Không thể kết nối tới server từ một domain khác
	- Link thông tin thêm: [article](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), [article](http://html5doctor.com/server-sent-events/#api), [article](https://www.html5rocks.com/en/tutorials/eventsource/basics/), [tutorial](https://jaxenter.com/tutorial-jsf-2-and-html5-server-sent-events-104548.html)
	
<img src="https://i.imgur.com/MF6xr3k.png">

## HTML5 Websockets:
1. Client gửi request liên tục lên server sử dụng HTTP
2. Client nhận trang web yêu cầu và thực thi JavaScript trên trang yêu cầu và mở một kết nối với server
3. Server và client có thể gửi và nhận các tin nhắn cho nhau khi có dữ liệu mới
	- Lưu lượng real-time từ server về client và từ client lên server
	- Bạn sẽ sử dụng server có một vòng lặp
	- Với websocket, bạn có thể kết nối với server từ một domain khác
	- Bạn cũng có thẻ kết nối tới server bằng cách sử dụng websocket server từ bên thứ 3, ví dụ như Pusher. 
	- Server và Client có thể gửi tin nhắn ở cùng 1 thời điểm
	- Thông tin thêm: [article](http://www.developerfusion.com/article/143158/an-introduction-to-websockets/), [article](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications), [tutorial](https://code.tutsplus.com/tutorials/start-using-html5-websockets-today--net-13270) 

<img src="https://i.imgur.com/NwAk8nH.png">
