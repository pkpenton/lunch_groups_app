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
    number_of_groups = len(randomized_guest_team)
    total_attendees = (len(randomized_primary_team) + len(randomized_guest_team))
    group_size = (total_attendees / number_of_groups) - 1
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
    randomized_primary_team = randomize_team(clean_lists(primary_team))
    randomized_guest_team = randomize_team(clean_lists(guest_team))

    return split_into_groups(randomized_primary_team, randomized_guest_team)


if __name__ == '__main__':
    main()
