module ApplicationHelper
  def format_text(text)
    RedCloth.new(text).to_html
  end
end
