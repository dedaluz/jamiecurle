require 'simplabs/highlight'

module ApplicationHelper

  def prettify_post_content(post, options = {})
    #
    #
    # try getting from the cache, if there's a hit return that
    content = CACHE.get("jc_post_#{post.id}")
    if ! content.nil?
      return content
    end
    # ok no hit, let's process it
    output = ''
    in_pre = false
    language = nil
    marked_down = markdown(post.body, options => 'strip' )
    text_pieces = marked_down.split(/(<code>|<code lang="[A-Za-z0-9_-]+">|<code lang='[A-Za-z0-9_-]+'>|<\/code>)/)
    text_pieces.collect do |piece|
      if piece =~ /^<code( lang=(["'])?(.*)\2)?>$/
        language = $3
        in_pre = true
        nil
      elsif piece == "</code>"
        in_pre = false
        language = nil
        nil
      elsif in_pre
        lang = language ? language : "ruby"
        output += '<pre><code lang="'+lang+'" class="syntax">' + highlight_code(lang, piece.strip) + '</code></pre>'
      else
        output += piece.strip
      end
    end
    # set the cache
    CACHE.set("jc_post_#{post.id}", output)
    output
  end

    def markdown(text, options = {})
      if options[:strip]
        RDiscount.new(strip_tags(text.strip)).to_html
      else
        RDiscount.new(text.strip).to_html
      end
    end

end
