def merge_sort(array): 
    if len(array) > 1: 
        i = j = k = comparisons = 0
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
  
        comparisons += merge_sort(left) 
        comparisons += merge_sort(right) 
  
        while i < len(left) and j < len(right): 
            comparisons += 1
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1
            k += 1

        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1
          
        while j < len(right): 
            array[k] = right[j] 
            j += 1
            k += 1
        return (comparisons)
    return (0)