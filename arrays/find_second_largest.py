from typing import List, Tuple

def find_second_largest(arr: List[int]) -> Tuple[int, int]:
    """
    Finds the second largest unique integer in an array and the index of its first occurrence.
    Does not use any built-in sorting or max/min functions.
    
    Args:
        arr: List of integers.
        
    Returns:
        A tuple of (value, index). Returns (-1, -1) if no distinct second largest exists.
    """
    n = len(arr)
    
    # Edge Case 1: Array has fewer than 2 elements
    if n < 2:
        return (-1, -1)

    # Pass 1: Find the index of the absolute maximum value
    max1_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max1_idx]:
            max1_idx = i

    # Pass 2: Find the index of the largest value strictly less than the maximum
    max2_idx = -1
    for i in range(n):
        # Ignore any elements that equal our absolute maximum
        if arr[i] != arr[max1_idx]:
            # If this is the first valid candidate, or if it's strictly greater 
            # than our current second max, update the index.
            # Strict greater-than (>) ensures we only capture the FIRST occurrence.
            if max2_idx == -1 or arr[i] > arr[max2_idx]:
                max2_idx = i

    # Edge Case 2: If max2_idx is still -1, all elements were identical
    if max2_idx == -1:
        return (-1, -1)

    return (arr[max2_idx], max2_idx)


if __name__ == "__main__":
    # Test cases mapped to your exact requirements
    test_cases = [
        ([3, 1, 6, 2, 6, 4], "value: 4, index: 5"),
        ([5, 5, 5, 5], "No distinct second largest exists."),
        ([1], "No distinct second largest exists."),
        ([-3, -1, -7, -2], "value: -2, index: 3"),
        ([9, 9, 8, 7], "value: 8, index: 2")
    ]

    print("Running Logic Foundation Tests...\n" + "="*40)
    
    for arr, expected in test_cases:
        val, idx = find_second_largest(arr)
        
        if val == -1 and idx == -1:
            result_str = "No distinct second largest exists."
        else:
            result_str = f"value: {val}, index: {idx}"
            
        print(f"Input:    {arr}")
        print(f"Expected: {expected}")
        print(f"Output:   {result_str}")
        print("-" * 40)
