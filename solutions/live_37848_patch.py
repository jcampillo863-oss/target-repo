# AtlasAeon Automated Candidate Patch for live_37848
def query(*args, **kwargs):
    def decorator(f):
        f._query_route = True
        return f
    return decorator
