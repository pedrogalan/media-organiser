from Media import Media

photo = Media("./samples/photo-with-metainf.jpg")
print photo.toString()

photo = Media("./samples/photo-without-metainf.jpg")
print photo.toString()
