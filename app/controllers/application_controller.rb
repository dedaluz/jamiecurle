class ApplicationController < ActionController::Base

  protect_from_forgery
  
  before_filter :authorize, :only => [:new, :edit]
  protected
    def authorize
      unless User.find_by_id(session[:user_id])
        redirect_to login_url, :notice => "Login"
      end
    end
end
