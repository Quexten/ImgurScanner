from imgurpython import ImgurClient
import csv
import time

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

client = ImgurClient(client_id, client_secret)

jpeg_count = 0
png_count = 0
gif_count = 0

def countImage( type ):
    global jpeg_count
    global png_count
    global gif_count
    if(type == "image/jpeg"):
        jpeg_count += 1
    elif(type == "image/png"):
        png_count += 1
    elif(type == "image/gif"):
        gif_count += 1
	
# Crawling Requests
items = client.gallery(page=0)
for item in items:
    print(item.link)
    if(not item.is_album):
        countImage(item.type)
    else:
        for image in client.get_album_images(item.id):
            countImage(image.type)

total_count = jpeg_count + png_count + gif_count

print("JPEG:"   + str(jpeg_count)   + " " + str(round(100 * (float(jpeg_count)    / float(total_count)), 2)) + "%")
print("PNG:"    + str(png_count)    + " " + str(round(100 * (float(png_count)     / float(total_count)), 2)) + "%")
print("GIF:"    + str(gif_count)    + " " + str(round(100 * (float(gif_count)     / float(total_count)), 2)) + "%")
print("Total:"  + str(total_count))
		
new_rows = []

with open('imgur_count.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        new_rows.append(row)
    new_rows.append([time.strftime("%m/%d/%Y")+ " - " +time.strftime("%H:%M"), str(jpeg_count), str(png_count), str(gif_count)])

with open('imgur_count.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(new_rows)
	
new_rows = []

with open('imgur_percentage.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        new_rows.append(row)
    new_rows.append([time.strftime("%m/%d/%Y")+ " - " + time.strftime("%H:%M"), str(round(100 * (float(jpeg_count) / float(total_count)), 2)),str(round(100 * (float(png_count) / float(total_count)), 2)), str(round(100 * (float(gif_count) / float(total_count)), 2))])

with open('imgur_percentage.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(new_rows)