from django.template.defaulttags import register
from django.utils import timezone
from bs4 import BeautifulSoup

@register.filter
def add_class(field, classname):
    return field.as_widget(attrs={'class':classname})

@register.filter
def sort_lower(arr, field):
    return sorted(arr, key=lambda tag: getattr(tag, field).lower())

@register.filter
def get_post_image(post, classname):
    soup = BeautifulSoup(post.body, 'html.parser')
    images = soup.select('img')
    if images != []:
        image = images[0]

        if image.get('style'):
            image['style'] = ''

        new_soup = BeautifulSoup()
        div = new_soup.new_tag('div', **{'class':classname})
        div.append(image)

        return div.decode()

@register.filter
def get_post_body(post, args):
    params = args.split()
    classname = params[0]
    size = int(params[1])

    soup = BeautifulSoup(post.body, 'html.parser')
    word_list = soup.getText().split()
    
    if len(word_list) <= size:
        words_body = ' '.join(word_list)
    else:
        words_body = ' '.join(word_list[:size] + ['...'])

    new_soup = BeautifulSoup()
    div = new_soup.new_tag('div', **{'class':classname})
    p = new_soup.new_tag('p')
    p.string = words_body
    div.append(p)
    return div