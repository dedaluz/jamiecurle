class RemoveBlogImageIdFromPosts < ActiveRecord::Migration
  def self.up
    remove_index "posts", "blog_image_id"
    remove_column "posts", "blog_image_id"
    add_column "blog_images", "post_id", :integer
    add_index "blog_images", "post_id"
  end

  def self.down
    remove_index "blog_images", "post_id"
    remove_column "blog_images", "post_id"
  end
end
