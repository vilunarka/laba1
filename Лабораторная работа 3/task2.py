def find_common_participants(first_group, second_group, separator=","):
    out = []
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    for index1 in first_group:
        for index2 in second_group:
            if index1 == index2:
                out.append(index1)
    out.sort()
    return(out)
    
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
