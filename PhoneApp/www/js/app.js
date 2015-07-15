$(function(){
    var $lstQuestions = $('#lstQuestions');
    var questionsUrl = 'http://127.0.0.1:8000/polls/api/questions/';
    
    
    function handleData(data){
        console.log(JSON.stringify(data));
    }
    
    $.ajax({
        type: "GET",
        url: questionsUrl,
        dataType: "json",
        headers: {
            "Authorization": "Token 3f7ea2dbe3c2cab9b55346200d7ef4796f53c731"
        },
        error: function(e){
            $('div#one p#error').html('ERROR - ' + e.status + ' ' + e.statusText);
            console.log('ERROR');
            console.log(e);
        },
        success: function(data){
            $lstQuestions.empty();
            $.each(data, function(index, item){
                $lstQuestions.append('<li><a href="#">'+ item.question_text +'</a></li>');
                //console.log(index);
                console.log(item);
            })
            $lstQuestions.listview('refresh');
        },
    })

});