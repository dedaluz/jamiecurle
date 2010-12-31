class AddTitleToBlogImage < ActiveRecord::Migration
  def self.up
    add_column "blog_images", "title", :string
  end

  def self.down
    remove_column "blog_images", "title"
  end
end
