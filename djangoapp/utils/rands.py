from django.utils.text import slugify

def random_letters(n=5):
    from random import SystemRandom
    random = SystemRandom()
    import string
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))

def slugify_new(text):
    return slugify(text) + '-' + random_letters()