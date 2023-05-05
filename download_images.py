from google_images_download import google_images_download

# specify the keyword and download limit
keyword = "cats"
limit = 100


# specify the arguments for the image downloader
arguments = {
    "keywords": keyword,
    "limit": limit,
    "print_urls": True,
    "output_directory": "./images",
    "image_directory": keyword,
    "format": "jpg",
}

# create an instance of the image downloader
downloader = google_images_download.googleimagesdownload()

# download the images
response = downloader.download(arguments)

# print the number of images downloaded
num_downloaded = len(response[0][keyword])
print(f"Downloaded {num_downloaded} out of {limit} images")

# print any errors that occurred during the download
if response[0][keyword] == "ERROR":
    print("Error:", response[keyword][1])