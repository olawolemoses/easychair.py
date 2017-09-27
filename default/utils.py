def get_post_dict(post, key):

    result = {}
    if post:
        import re
        patt = re.compile('^([a-zA-Z_]\w+)\[([a-zA-Z_\-][\w\-]*)\]$')
        for post_name, value in post.items():
            value = post[post_name]
            print post_name
            match = patt.match(post_name)
            if match:
                print post_name, value, "match"
            if not match or not value:
                continue
            name = match.group(1)
            print name
            if name == key:
                k = match.group(2)
                print k
                result.update({k:value})
    return result
