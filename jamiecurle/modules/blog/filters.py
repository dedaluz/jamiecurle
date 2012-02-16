# -*- coding: utf-8 -*-
import calendar
import re
import pygments
from pygments import lexers, formatters
import markdown


def render(content):
    regex = re.compile(r'(<code(.*?)</code>)', re.DOTALL)
    code_blocks = []

    for i, m in enumerate(regex.finditer(content)):
        code = m.group(0)
        # if code is inline leave it alone
        #print code.find('inline')
        #if code.find('inline') > 0:
        #    continue
        # if there is a lang attribute, use that
        if code.find('lang') > 0:
            # get the language
            try:
                language = re.split(r'"|\'', code)[1]
                # fix some wonky lexers
                if language == 'conf': language = 'nginx'
                if language == 'regex': language = 'perl'
                # all goods
                lexer = lexers.get_lexer_by_name(language)
            except IndexError:
                lexer = lexers.guess_lexer(str(code))
            except ValueError:
                lexer = lexers.PythonLexer()
            # remove the code tags
            code = code.replace('</code>', '')
            code = code.replace('<code>', '')
            code = re.sub('<code(.*?)>', '', code)
            # create the pygmented code with the lexer
            pygmented_string = pygments.highlight(code, lexer, formatters.HtmlFormatter(linenos=True))
            # put the code blocks into the list for processintg later
            code_blocks.append(pygmented_string)
        else:
            code_blocks.append(code)
            # replace the <code> tags with placeholders that can be used to replace
        content = content.replace(m.string[m.start():m.end()], '{{CODE%s}}' % i)
        # now process as markdown
        
        # replaced placeholders with the actual code
        for i, code in enumerate(code_blocks):
            content = content.replace('<p>{{CODE%s}}</p>' % i, code)
            content = content.replace('{{CODE%s}}' % i, code)
    # return
    return content


def colour_for_date(date):
    colours = [
        (255.0,27.7126443311),
        (245.578313253,34.2094985159),
        (203.248995984,49.2263282726),
        (154.297188755,61.2968854298),
        (95.9748995984,72.8323699422),
        (34.8704819277,75.0),
        (0.0,70.2606837,50),
        (7.51004016064,66.8215903765),
        (52.7921686747,56.165939981),
        (124.598393574,44.4600275525),
        (200.859437751,31.5213531977),
        (241.8062249,25.0),
    ]
    # get the month
    current = colours[date.month - 1 ]
    days_in_month = calendar.monthrange(date.year, date.month)
    days_in_month = days_in_month[1]
    # 
    try:
        next = colours[date.month]
    except IndexError:
        next = colours[0]
    hue_delta = next[0] - current[0]
    sat_delta = next[1] - current[1]
    hue_per_day = hue_delta / days_in_month
    sat_per_day = sat_delta / days_in_month
    hue = current[0] + (date.day * hue_per_day)
    sat = current[1] + (date.day * sat_per_day)
    
    return 'hsla(%s,%s%%,50%%, 1)' % (hue, sat)


def archivedateformat(value, format='%B %Y'):
    return value.strftime(format)

def datetimeformat(value, format='%d %B %Y'):
    return value.strftime(format)