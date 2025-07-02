from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(list,chunk_size):
    chunk=[]
    for item in list:
        chunk.append(item)
        if len(chunk)==chunk_size:
            yield chunk
            chunk=[]
    yield chunk
