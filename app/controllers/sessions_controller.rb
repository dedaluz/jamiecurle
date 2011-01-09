class SessionsController < ApplicationController
  skip_before_filter :authorize

  def new
    if session[:user_id]
      redirect_to posts_url
    end
  end

  def create
    if user = User.authenticate(params[:email], params[:password])
      session[:user_id] = user.id
      redirect_to posts_url
    else
      redirect_to login_url, :alert => "you're not known to me"
    end
    
  end

  def destroy
    session[:user_id] = nil
    redirect_to posts_url, :notice => "Logged out"
  end

end
