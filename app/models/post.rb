class Post < ActiveRecord::Base
  
  has_many :blog_images
  
  def to_param
    "#{id}-#{title.gsub(/[^a-z0-9]+/i, '-')}"
  end
end
