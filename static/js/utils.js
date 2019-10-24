function http_get(url, map_args, res_func = undefined) {
    $.get(url, map_args, function (ret) {
        if (res_func !== undefined) {
            res_func(ret);
        }
        alert(JSON.stringify(ret));
    }).fail(() => console.log('send request error.'))
}

function http_post(url, data_args, res_func = undefined) {
    $.post(url, data_args, function (ret) {
        if (res_func !== undefined) {
            res_func(ret);
        }
        alert(JSON.stringify(ret));
    }, 'json').fail(() => console.log('send request error.'))
}

function enroll_student(course_id, student_email) {

    $.get("/users/enroll/", {'course': course_id, 'student_email': student_email},
        function (ret) {
            alert(JSON.stringify(ret))
        }).fail(() => console.log('send request error'));
}

function assign_prof(course_id, prof_email) {
    $.get("/users/assign/", {'course': course_id, 'prof_email': prof_email},
        function (ret) {
            alert(JSON.stringify(ret))
        });
}

function create_hw(course_id, prof_email) {
    $.get("/users/assign/", {'course': course_id, 'prof_email': prof_email},
        function (ret) {
            alert(JSON.stringify(ret))
        });
}

function create_exam(course_id, prof_email) {
    $.get("/users/assign/", {'course': course_id, 'prof_email': prof_email},
        function (ret) {
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

$(document).ready(function () {
    $('#couser_manage').DataTable();
    $('#student_table').DataTable();
    $('#prof_table').DataTable();
    $('#stu_course').DataTable();
    $('#dataTable1').DataTable();

    $.fn.editable.defaults.mode = 'popup';

    //make username editable

    $('.editable').children('a').each(function () {
        name = $(this).attr('name')
        $(this).editable({
            type: 'text',
            pk: 1,
            name: name,
            url: '/users/change_grade',
            success: function (response, newValue) {
                console.log(response)
            }
        });
        console.log(name)
    })

    // editable({
    //     type: 'text',
    //     pk: 1,
    //     name: $
    //     url: '/users/change_grade',
    //     success: function (response, newValue) {
    //         console.log(response)
    //     }
    // });
});

