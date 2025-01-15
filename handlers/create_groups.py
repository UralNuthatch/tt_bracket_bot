def create_groups(participants):
    if not participants or len(participants) < 16:
        return None
    group_count = len(participants) // 4
    # рейтинг для новичка
    new_player_rttf = "250"
    participants = [[player[1], player[2]] if player[2] != "-" else [player[1], new_player_rttf] for player in participants]
    sorted_participants = sorted(participants, key=lambda x: int(x[1]))
    # формирование групп змейкой в зависимости от рейтинга рттф
    groups = [[] for _ in range(group_count)]
    step = 1
    i = 0
    while sorted_participants:
        groups[i].append(sorted_participants.pop())
        i += step
        if i == group_count:
            i -= 1
            step = -1
        elif i == -1:
            i = 0
            step = 1
    return groups