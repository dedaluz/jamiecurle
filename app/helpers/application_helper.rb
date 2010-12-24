require 'simplabs/highlight'

module ApplicationHelper

   def prettify(text, options = {})
      text_pieces = text.split(/(<code>|<code lang="[A-Za-z0-9_-]+">|
        <code lang='[A-Za-z0-9_-]+'>|<\/code>)/)
      in_pre = false
      language = nil
      output = ''
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
          output += '<code lang="" class="syntax">' + highlight_code(lang, piece.strip) + '</code>'
        else
          output += markdown(piece.strip, options => 'strip' )
        end
      end
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
