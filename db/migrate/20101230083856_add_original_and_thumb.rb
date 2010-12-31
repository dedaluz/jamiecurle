class AddOriginalAndThumb < ActiveRecord::Migration
  def self.up
    add_column "blog_images", "original", :string
    add_column "blog_images", "thumb", :string
  end

  def self.down
    remove_column "blog_images", "original"
    remove_column "blog_images", "thumb"
  end
end
