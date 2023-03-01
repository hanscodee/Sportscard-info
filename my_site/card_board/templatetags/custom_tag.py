from django import template

# 实例化
register = template.Library()        # register

@register.simple_tag                 
def showlist(x,n):
    a = x[n]
    n += 1
    return a,n


@register.simple_tag                 
def count(n):
    n += 1
    return n