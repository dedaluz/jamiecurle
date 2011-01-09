class CreateBlogImages < ActiveRecord::Migration
  def self.up
    create_table :blog_images do |t|
      t.string :src
      t.string :img

      t.timestamps
    end
  end

  def self.down
    drop_table :blog_images
  end
end
