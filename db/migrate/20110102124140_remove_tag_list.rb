class RemoveTagList < ActiveRecord::Migration
  def self.up
    remove_column "posts", "tag_list"
  end

  def self.down
    add_column "posts", "tag_list", :string
  end
end
