class AddPublished < ActiveRecord::Migration
  def self.up
    add_column "posts", "published", :boolean
    add_index "posts", "published"
  end

  def self.down
    remove_index "posts", "published"
    remove_column "posts", "published"
  end
end
