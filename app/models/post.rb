class Post < ActiveRecord::Base
  has_many :blog_images
  acts_as_url :title, :sync_url=> true
  acts_as_taggable
  


  def poster
      # skiper everything of we have a blog_image_id
      # onwards
      #p self.blog_image_id.nil?
      if ! self.blog_image_id.nil?
        #p 'image'
        return BlogImage.find(self.blog_image_id)
      end
      #p 'findy findy'
      # no joy? grab the counter it from the cache
      key = "jc_post_blog_images_count_#{self.id}"
      count = CACHE.get(key)
      # set it if it's not in there
      if count == nil
        count = self.blog_images.count
        CACHE.set("jc_post_blog_images_count_#{self.id}", count)
      end
      # if there are no posts return a blank image
      if count == 0
        poster = BlogImage.new()
        poster.thumb = '/images/thumb_default.jpg'
      else
        poster = self.blog_images[0]
      end
      poster
  end
  
  def to_param
    url
  end
  
  def sto_param
    "#{id}-#{title.gsub(/[^a-z0-9]+/i, '-')}"
  end
end
