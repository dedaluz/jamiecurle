class CreateJournals < ActiveRecord::Migration
  def self.up
    create_table :journals do |t|
      t.string :title
      t.string :description
      t.text :content
      t.boolean :published

      t.timestamps
    end
  end

  def self.down
    drop_table :journals
  end
end
