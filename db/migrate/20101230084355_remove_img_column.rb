class RemoveImgColumn < ActiveRecord::Migration
  def self.up
    remove_column "blog_images" , "img"
  end

  def self.down
    add_column "blog_images", "img", :string
  end
end
