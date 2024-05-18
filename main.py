from pytube import YouTube

link = input("Nhập link Youtube: ")

y_tube = YouTube(link)

print(f'Tiêu đề video: {y_tube.title}')

stream = y_tube.streams.filter(progressive="False")

video = list(enumerate(stream))

for i in video:
    print(i)

print("=================================")
index = int(input('Nhập vào video muốn tải: '))

stream[index].download()
print("Tải xuống thành công")