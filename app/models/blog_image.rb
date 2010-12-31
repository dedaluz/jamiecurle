class BlogImage < ActiveRecord::Base
  
  belongs_to :post
  
  validates :src, :presence => true
  validate :title, :presence => true
  
  attr_reader :uploaded_file
  
  before_create :process_upload
  
  def process_upload
    # give it a sanesible filename
    @filename = sanitize_filename(self.src.original_filename)
    # Make the path if it doesn't exist
    if !File.exists?(File.dirname(self.path))
        FileUtils.mkdir_p(File.dirname(self.path))
    end
    # move it
    FileUtils.copy(self.src.tempfile.path, self.path)
    #
    #
    # todo make, sure names are unique
    write_attribute(:original, "/files/#{self.post.id}/#{@filename}")
    #
    #
    # todo - offer a resize on the src
    write_attribute(:src, "/files/#{self.post.id}/#{@filename}")
    # create an 100 x 100 thumbnail
    thumbnail = MiniMagick::Image.open(self.path)
    thumbnail.resize "100x100"
    thumbnail.write(self.thumb_path)
    write_attribute(:thumb, "/files/#{self.post.id}/thumb_#{@filename}")
  end
  
  def path
      File.expand_path("#{RAILS_ROOT}/public/files/#{self.post.id}/#{@filename}")
  end
  def thumb_path
      File.expand_path("#{RAILS_ROOT}/public/files/#{self.post.id}/thumb_#{@filename}")
  end

  private
    def sanitize_filename(original_filename)
      # get only the filename, not the whole path (from IE)
      filename = File.basename(original_filename) 
      # replace all none alphanumeric, underscore or perioids with underscore
      filename.gsub(/[^\w\.\_]/,'_') 
    end
end
