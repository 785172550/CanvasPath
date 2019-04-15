function enroll_student(course_id, student_email) {
    $.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});

    $.get("/users/enroll/", {'course': course_id, 'student_email': student_email}, function (ret) {
        alert(ret)
    })
}

function assign_prof(course_id, prof_email) {
    $.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});

    $.get("/users/assign/", {'course': course_id, 'prof_email': prof_email}, function (ret) {
        alert(ret)
    })
}
