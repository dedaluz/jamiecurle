class BlogImage < ActiveRecord::Base
  belongs_to :post

  validates :src, :presence => true
  validates :title, :presence => true
  
  attr_reader :uploaded_file
  
  before_create :process_upload
  before_destroy :unlink_files
  
  
  def unlink_files
    files  = ["#{RAILS_ROOT}#{self.original}", "#{RAILS_ROOT}#{self.thumb}", "#{RAILS_ROOT}#{self.src}"]
    
    files.each do |f|
      begin
        File.unlink(f)
      rescue
      end
    end
  
  end
  def process_upload
    # set up some sensiable filenames
    @filename = sanitize_filename(self.src.original_filename)
    @src_title_filename = self.title.gsub(/[^\w\.\_]/,'_') + '.jpg'
    # Make the path if it doesn't exist
    if !File.exists?(File.dirname(self.original_path))
        FileUtils.mkdir_p(File.dirname(self.original_path))
    end
    # move it and write attribute
    FileUtils.copy(self.src.tempfile.path, self.original_path)
    write_attribute(:original, "/files/#{self.post.id}/#{@filename}")
    #
    #
    # src needs to be resized to 833 wide
    src = MiniMagick::Image.open(self.original_path)
    src.resize(833)
    src.write(self.src_path)
    write_attribute(:src, "/files/#{self.post.id}/#{@src_title_filename}")
    #
    #
    # create an 100 x 100 thumbnail
    thumbnail = MiniMagick::Image.open(self.original_path)
    thumbnail = resize_and_crop(thumbnail, 200)
    thumbnail.write(self.thumb_path)
    write_attribute(:thumb, "/files/#{self.post.id}/thumb_#{@src_title_filename}")
  end
  def original_path
      File.expand_path("#{RAILS_ROOT}/public/files/#{self.post.id}/#{@filename}")
  end
  def src_path
      File.expand_path("#{RAILS_ROOT}/public/files/#{self.post.id}/#{@src_title_filename}")
  end
  def thumb_path
      File.expand_path("#{RAILS_ROOT}/public/files/#{self.post.id}/thumb_#{@src_title_filename}")
  end
  
  
  def resize_and_crop(image, size)
    if image[:width] < image[:height]
      remove = ((image[:height] - image[:width])/2).round
      image.shave("0x#{remove}")
    elsif image[:width] > image[:height]
      remove = ((image[:width] - image[:height])/2).round
      image.shave("#{remove}x0")
    end
    image.resize("#{size}x#{size}")
    return image
  end


  private
    def sanitize_filename(original_filename)
      # get only the filename, not the whole path (from IE)
      filename = File.basename(original_filename) 
      # replace all none alphanumeric, underscore or perioids with underscore
      filename.gsub(/[^\w\.\_]/,'_')
      # todo make, sure names are unique, if not make them unique
      #
      #
    end
end
