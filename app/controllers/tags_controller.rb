class TagsController < ActionController::Base

  def show
    @posts = Post.tagged_with(params[:id])
  end

  def index
    @tags = Post.tag_counts_on(:tags)
  end

end