from core.libs.exceptions import FyleError
from core.models.assignments import AssignmentStateEnum, GradeEnum
from core.models.teachers import Teacher


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B

def test_list_teachers(client, h_principal):
    """
    Test case for successfully retrieving the list of teachers.
    """
   
    response = client.get('/principal/teachers', headers=h_principal)
    assert response.status_code == 200  
    data = response.json['data']
    
    assert isinstance(data, list)
    assert len(data) > 0
    for teacher in data:
        assert 'id' in teacher # Check if 'id' is present in the teacher data
        teacher = Teacher.get_by_id(teacher['id'])
        assert teacher is not None, f"Teacher with ID {teacher['id']} should exist."
        # Check if the representation matches the expected format
        assert repr(teacher) == f'<Teacher {teacher.id!r}>', f"Expected representation for teacher ID {teacher.id} does not match."