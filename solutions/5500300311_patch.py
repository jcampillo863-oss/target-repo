# AtlasAeon Automated Candidate Patch for 5500300311
def query(*args, **kwargs):
    def decorator(f):
        f._query_route = True
        return f
    return decorator
