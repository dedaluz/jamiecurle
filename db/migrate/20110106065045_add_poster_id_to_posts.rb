class AddPosterIdToPosts < ActiveRecord::Migration
  def self.up
    add_column "posts", "blog_image_id", :integer
    add_index "posts", "blog_image_id"
  end

  def self.down
    remove_index "posts", "blog_image_id"
    remove_column "posts", "blog_image_id"
  end
end
