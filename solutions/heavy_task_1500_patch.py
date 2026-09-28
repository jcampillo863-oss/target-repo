# AtlasAeon Automated Candidate Patch for heavy_task_1500
def query(*args, **kwargs):
    def decorator(f):
        f._query_route = True
        return f
    return decorator
