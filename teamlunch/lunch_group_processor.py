import random
import funcy as fn


def clean_lists(team_list):
    clean_team_list = [person.lower().strip() for person in team_list]
    for person in clean_team_list:
        if clean_team_list.count(person) > 1:
            clean_team_list.remove(person)
    return clean_team_list


def randomize_team(cleaned_team_list):
    random.shuffle(cleaned_team_list)
    return cleaned_team_list


def split_into_groups(randomized_primary_team, randomized_guest_team):
    # TODO: this is fucked, make two lists and concat them together instead
    total_attendees = len(randomized_primary_team) + len(randomized_guest_team)

    if total_attendees % 5 == 0:
        group_size = 5
    elif total_attendees % 6 == 0:
        group_size = 6
    elif total_attendees % 7 == 0:
        group_size = 7
    elif total_attendees % 8 == 0:
        group_size = 8
    elif total_attendees % 9 == 0:
        group_size = 9
    else:
        group_size = 6

    chunked_list = fn.chunks(group_size, randomized_primary_team)

    for i in range(len(randomized_guest_team)):
        chunked_list[i % len(chunked_list)].append(randomized_guest_team.pop())

    chunked_list_last_child = chunked_list[-1]
    if len(chunked_list_last_child) < 5:
        for i in range(len(chunked_list_last_child)):
            chunked_list[i % len(chunked_list)].append(chunked_list_last_child.pop())
        del chunked_list[-1]

    return chunked_list


def main():
    # primary_team and guest_team are declared by the user upon form submission
    randomized_primary_team = randomize_team(clean_lists(primary_team))
    randomized_guest_team = randomize_team(clean_lists(guest_team))

    return split_into_groups(randomized_primary_team, randomized_guest_team)


if __name__ == '__main__':
    main()
