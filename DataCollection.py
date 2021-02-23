# FlickrAPI Object to collect photos of Cats & Owls

# Importing libraries
import urllib
import flickrapi

from time import sleep

from config import secrets



# To authenticate, plug in your API Key as the first argument and the Secret Code as the second.
print("Connecting to Flickr...")
flickr = flickrapi.FlickrAPI(secrets['API_Key'], secrets['Secret_code'], cache=True)
print(flickr)

# Getting the photos through the walk method
cat_photos = flickr.walk(text = 'cat',
                     tag_mode = 'all',
                     tags = 'cat',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

owl_photos = flickr.walk(text = 'owl',
                     tag_mode = 'all',
                     tags = 'owl',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

# Extracting URLs of photos from the response
cat_urls = []
for i, photo in enumerate(cat_photos):
    cat_urls.append(photo.get('url_c'))

    if i > 1050:
        break
print("Cat urls found: ", len(cat_urls))

owl_urls = []
for i, photo in enumerate(owl_photos):
    owl_urls.append(photo.get('url_c'))

    if i > 1050:
        break
print("Owl urls found: ", len(owl_urls))


# Removing None type objects & taking only the first 960 URLs. 950 images for training & 10 images for testing
cat_urls = [x for x in cat_urls if x is not None][:960]
owl_urls = [x for x in owl_urls if x is not None][:960]

# =====================================  Downloading the images to folders ==========================================
train_dir = "Train/"
test_dir = "Test/"
# Mention full paths to either training/testing folders
# 1) Cat Images
for count, url in enumerate(cat_urls[:480]):
    urllib.request.urlretrieve(
        url, train_dir + 'Cats/' + 'cat_' + str(count) + '.jpg')

sleep(100)

for count, url in enumerate(cat_urls[480:]):
    urllib.request.urlretrieve(
        url, train_dir + 'Cats/' + 'cat_' + str(480 + count) + '.jpg')

# 2) Owl Images
for count, url in enumerate(owl_urls[:480]):
  urllib.request.urlretrieve(
      url, train_dir + 'Owls/' + 'owl_' + str(count) + '.jpg')

sleep(100)

for count, url in enumerate(owl_urls[480:]):
    urllib.request.urlretrieve(
        url, train_dir + 'Owls/' + 'owl_' + str(450 + count) + '.jpg')


