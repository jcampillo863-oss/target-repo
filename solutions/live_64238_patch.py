# AtlasAeon Automated Candidate Patch for live_64238
def query(*args, **kwargs):
    def decorator(f):
        f._query_route = True
        return f
    return decorator
