class PostsController < ApplicationController
  
  
  
  
  def feed
    if params[:tag].nil?
      @posts = Post.find(:all, :order => 'created_at DESC', :limit => 10, :conditions => "published = true")
    else
      @posts = Post.tagged_with(params[:tag])
    end
  end
  
  # GET /posts
  # GET /posts.xml
  def index
    conditions  = "published = true" unless user_signed_in? or request.remote_ip == '188.220.35.125'
    @posts = Post.find(:all, :order => 'created_at DESC',  :conditions => conditions)
    respond_to do |format|
      format.html # index.html.erb
      format.xml  { render :xml => @posts }
    end
  end

  # GET /posts/1
  # GET /posts/1.xml
  def show
    #
    conditions  = "published = true" unless user_signed_in? or request.remote_ip == '188.220.35.125'
    
    @post = Post.find_by_url(params[:id], :conditions => conditions)
    # perhaps this is an old url?
    if @post.nil?
      @post = Post.find(params[:id])
      if !@post.nil?
        redirect_to post_path(@post), :status=>301 
      end
    end
  end

  # GET /posts/new
  # GET /posts/new.xml
  def new
    @post = Post.new
    respond_to do |format|
      format.html # new.html.erb
      format.xml  { render :xml => @post }
    end
  end

  # GET /posts/1/edit
  def edit
    # get the post
    @post = Post.find_by_url(params[:id])
    #@post = Post.find_by_url(params[:id])
  end

  # POST /posts
  # POST /posts.xml
  def create
    @post = Post.new(params[:post])

    respond_to do |format|
      if @post.save
        format.html { redirect_to(@post, :notice => 'Post was successfully created.') }
        format.xml  { render :xml => @post, :status => :created, :location => @post }
      else
        format.html { render :action => "new" }
        format.xml  { render :xml => @post.errors, :status => :unprocessable_entity }
      end
    end
  end

  # PUT /posts/1
  # PUT /posts/1.xml
  def update
    @post = Post.find_by_url(params[:id])
    # delete cache
    CACHE.delete("jc_post_#{@post.id}")
    #
    
    p params[:post][:continue]
    
    respond_to do |format|
      if @post.update_attributes(params[:post])
        format.html { redirect_to( edit_post_path, :notice => 'Post was successfully updated.' )}
        #format.html { redirect_to(@post, :notice => 'Post was successfully updated.') }
        format.xml  { head :ok }
      else
        format.html { render :action => "edit" }
        format.xml  { render :xml => @post.errors, :status => :unprocessable_entity }
      end
    end
  end

  # DELETE /posts/1
  # DELETE /posts/1.xml
  def destroy
    @post = Post.find_by_url(params[:id])
    @post.destroy

    respond_to do |format|
      format.html { redirect_to(posts_url) }
      format.xml  { head :ok }
    end
  end
end
