
$(function(){
    // build the structure
    var holder = $('<div id="js_tags_widget"></div>');
    var tags = $('<div id="js_tag_widget_tags">asd</a>')
    
    //holder.append(tags)
    // move the curre
    holder.append(tags)
    //w = tags.width();
    //console.log(w);
    $('#id_tags').wrap(holder)
    // fill in some tmp tags
   tags.append('<a href="#">Tag 1</a> <a href="#">Tag 2</a> <a href="#">Tag 3</a>')
})