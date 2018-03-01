from Forums import models
from Forums import stores

post_story = stores.PostStore()
post_story.add(models.Post("Life", "Life is alawys  great"))
post_story.add(models.Post("Sunshine", "Sunshine is amazing"))
