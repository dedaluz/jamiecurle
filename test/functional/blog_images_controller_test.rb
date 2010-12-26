require 'test_helper'

class BlogImagesControllerTest < ActionController::TestCase
  setup do
    @blog_image = blog_images(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:blog_images)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create blog_image" do
    assert_difference('BlogImage.count') do
      post :create, :blog_image => @blog_image.attributes
    end

    assert_redirected_to blog_image_path(assigns(:blog_image))
  end

  test "should show blog_image" do
    get :show, :id => @blog_image.to_param
    assert_response :success
  end

  test "should get edit" do
    get :edit, :id => @blog_image.to_param
    assert_response :success
  end

  test "should update blog_image" do
    put :update, :id => @blog_image.to_param, :blog_image => @blog_image.attributes
    assert_redirected_to blog_image_path(assigns(:blog_image))
  end

  test "should destroy blog_image" do
    assert_difference('BlogImage.count', -1) do
      delete :destroy, :id => @blog_image.to_param
    end

    assert_redirected_to blog_images_path
  end
end
