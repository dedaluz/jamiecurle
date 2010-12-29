class BlogImage < ActiveRecord::Base
  
  belongs_to :post
  
  validates :src, :presence => true
  validates :uploaded_file, :confirmation => true
  
  attr_reader :uploaded_file
    
  def uploaded_file=(uploaded_file)
    @uploaded_file=uploaded_file
    
    print 'hello2'
    
  end

end
