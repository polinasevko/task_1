def unification_source_data(rooms, students):
    rooms_with_studs = []
    # fill room info
    for room in rooms:
        rooms_with_studs.append(
            {'room_id': room['id'],
             'room_name': room['name'],
             'students': []}
        )
    # fill students info
    for stud in students:
        new_student = {
            'stud_id': stud['id'],
            'stud_name': stud['name'],
        }
        room_number = stud['room']
        rooms_with_studs[room_number]['students'].append(new_student)
    return rooms_with_studs
