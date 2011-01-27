Jamiecurle::Application.routes.draw do

  resources :journals

  devise_for :users
  #devise_for :users, :path_names => { :sign_in => 'login', :sign_out => 'logout', :password => 'secret', :confirmation => 'verification'}
  #
  #
  #
  
  controller :sessions do
    get 'login' => :new
    post 'login' => :create
    delete 'logout' => :destroy
  end
  
  #
  #
  #
  resources :users
  
  resources :tags
  
  
  #
  # posts
  match '/posts/feed', :to => 'posts#feed'
  match '/posts/feed/:tag', :to => 'posts#feed'
  resources :posts do 
    resources :blog_images
  end
  
  #
  # This is the root
  #
  root :to => "posts#index"
end
