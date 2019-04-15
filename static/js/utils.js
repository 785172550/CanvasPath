function enroll_student(course_id, student_email) {

    $.get("/users/enroll/", {'course': course_id, 'student_email': student_email}, function (ret) {
        alert(JSON.stringify(ret))
    });
}

function assign_prof(course_id, prof_email) {
    $.get("/users/assign/", {'course': course_id, 'prof_email': prof_email}, function (ret) {
        alert(JSON.stringify(ret))
    });
}

function add_course(c_id, c_name, c_dec, sec_no, sec_type) {
    $.post("/users/add_course/", {
        'course': c_id,
        'name': c_name,
        'dec': c_dec,
        'sec_no': sec_no,
        'sec_type': sec_type
    }, function (ret) {
        alert(JSON.stringify(ret))
    });
}

function delete_course(c_id, button) {
    var con = confirm("Delete this Row?")
    if (con) {
        $.get("/users/add_course/", {'delete_id': c_id}, function (ret) {
            alert(JSON.stringify(ret))
        });
        var t = $('#course-table').DataTable();
        t.row($(button).parents('tr').remove().draw(false));
    } else {

    }

}
