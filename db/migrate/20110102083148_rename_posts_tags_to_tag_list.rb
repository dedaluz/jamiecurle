class RenamePostsTagsToTagList < ActiveRecord::Migration
  def self.up
    rename_column "posts", "tags", "tag_list"
  end

  def self.down
    rename_column "posts", "tag_list", "tags"
  end
end
