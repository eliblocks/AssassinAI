
# coding: utf-8

# In[5]:

from clarifai import rest
from clarifai.rest import ClarifaiApp


# In[6]:

app = ClarifaiApp("uNNYPKmRH92ahYBt4cZYYGAYsziXVCcWvBS9VqJX", "ak54oZ41klsyaQ9kYnn9YJIF-Vt7tIdB5d52GxzC")

# before search, first need to upload a few images
# app.inputs.create_image_from_filename("E://New Downloads//IMG_20170211_211334.jpg", concepts=["Borislav Milkov"], not_concepts=["Swift"])
# app.inputs.create_image_from_filename("E://New Downloads//IMG_20170211_211339.jpg", concepts=["Borislav Milkov"], not_concepts=["Swift"])
# app.inputs.create_image_from_filename("E://New Downloads//IMG_20170211_211343.jpg", concepts=["Borislav Milkov"], not_concepts=["Swift"])
# app.inputs.create_image_from_url(url="http://starsignstyle.com/wp-content/uploads/2015/12/taylor-swift-astrology.jpg", concepts=["Swift"], not_concepts=["Borislav Milkov"])
# app.inputs.create_image_from_url(url="https://s-media-cache-ak0.pinimg.com/originals/cd/e9/67/cde967a6c9871d09b8ef750151ce8f78.jpg", concepts=["Swift"], not_concepts=["Borislav Milkov"])
# app.inputs.create_image_from_url(url="https://assets.entrepreneur.com/content/16x9/822/20150720165857-taylor-swift.jpeg", concepts=["Swift"], not_concepts=["Borislav Milkov"])
# app.inputs.create_image_from_url(url="http://i.dailymail.co.uk/i/pix/2016/01/02/03/2FBB20FC00000578-0-image-m-33_1451707088839.jpg", concepts=["Swift"], not_concepts=["Borislav Milkov"])
app.inputs.create_image_from_url(url="http://great-hairstyles.net/wp-content/uploads/2015/07/taylor-swift-updo.jpg", concepts=["Swift"], not_concepts=["Borislav Milkov"])

#model = app.models.create("myfaces1", concepts=["Borislav Milkov", "Swift"])
model = app.models.get('myfaces1')

model.train()


# In[7]:

from clarifai.rest import Image as ClImage

model = app.models.get('myfaces1')
image = ClImage(url='http://great-hairstyles.net/wp-content/uploads/2015/07/taylor-swift-updo.jpg')
model.predict([image])


# In[ ]:



