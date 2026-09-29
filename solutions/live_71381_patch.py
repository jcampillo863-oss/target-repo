# AtlasAeon Automated Candidate Patch for live_71381
def query(*args, **kwargs):
    def decorator(f):
        f._query_route = True
        return f
    return decorator
