def solution(sizes):
    lenSizes = len(sizes)
    width = sizes[0][0]
    height = sizes[0][1]
    
    if width > height :
      for i in range (lenSizes) :
        if sizes[i][0] < sizes[i][1] :
          tmp = sizes[i][0]
          sizes[i][0] = sizes[i][1]
          sizes[i][1] = tmp
    else :
      for i in range (lenSizes) :
        if sizes[i][0] > sizes[i][1] :
          tmp = sizes[i][0]
          sizes[i][0] = sizes[i][1]
          sizes[i][1] = tmp
    print(sizes)
    
    maxWidth  = width
    maxHeight = height
    for i in range (lenSizes) :
      if sizes[i][0] > maxWidth :
        maxWidth = sizes[i][0]
      if sizes[i][1] > maxHeight :
        maxHeight = sizes[i][1]
    print(maxWidth)
    print(maxHeight)
            
    return maxWidth * maxHeight