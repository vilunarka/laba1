def find_common_participants(first_group, second_group, separator=","):
    out = []
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    for i in first_group:
        for j in second_group:
            if i == j:
                out.append(i)

    out.sort()
    return(out)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
