def GetMemberList(members):
    members = members.split(',')
    for idx, _ in enumerate(members):
        while members[idx][0] == ' ':
            members[idx]=members[idx][1:]
    return members