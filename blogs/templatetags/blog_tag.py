from blogs.models import airticle
from django import template

register = template.Library()

@register.simple_tag
def get_recent_airticle_date():
    return airticle.objects.dates('create_time','month',order='DESC')


@register.simple_tag
def get_recent_airticle(num=3):
    return airticle.objects.all().order_by('-create_time')[:num]


def recent_airticles(**kwargs):
    pass
