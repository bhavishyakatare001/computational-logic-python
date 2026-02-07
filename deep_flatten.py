def deep_flatten(items):

    if not isinstance(items, (list, tuple)):
        return [items]
        
    flat_list = []
    for item in items:
        if isinstance(item, (list, tuple)):
            flat_list.extend(deep_flatten(item))
        else:
            flat_list.append(item)
    return flat_list

if __name__ == "__main__":
  
    assert deep_flatten([1, [2, [3]]]) == [1, 2, 3]
    assert deep_flatten([]) == []
    assert deep_flatten(99) == [99]
    print("Logic Foundations: All tests passed. Code is commit-ready.")
