def solution(numbers, target):
    root_node = [0]
    
    for number in numbers:
        child_node = []
        for result in root_node: 
            child_node.append(result + number)
            child_node.append(result - number)
        root_node = child_node
        
    return root_node.count(target)