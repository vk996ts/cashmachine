
var field_length = {'pin': 4, 'card': 16, 'cash': 5};

function display_val(val)
{
    var display_val = '';
    for(var i=0, s=val.length; i<s; i++)
    {
        display_val+=val[i];
        if((i+1)%4==0 && (i+1)<16)
        {
            display_val+='-';
        }
    }
    return display_val;
}

function display_stars(val)
{
    var stars = ""
    for(var i=0; i<val; i++)
    {
        stars+="*";
    }
    return stars;
}


$(document).ready(function(){

    if(document.getElementById('page'))
    {
        $(".card-number").html(display_val($("#id_number").val()));
        var max_length = eval('field_length.'+document.getElementById('page').value);

        $(".keyboard .btn").click(function(){
            var val = $("#id_number").val();
            var new_val = val+$(this).val();
            var action = $(this).attr("data-action");
            if(action)
            {
                if(action == "backspace" && new_val.length > 1)
                {
                    new_val = new_val.substr(0, new_val.length-2);
                }
                else if(action == 'clear')
                {
                    new_val = '';
                    $(".card-number").html('');
                }
            }

            if(new_val.length<=max_length){
                $("#id_number").val(new_val);
                if($("#page").val() != 'pin')
                {
                    $(".card-number").html(display_val(new_val));
                }
                else
                {
                    $(".card-number").html(display_stars(new_val.length));
                }
            }
            return false;
        });
    }
    else
    {
        var cn = display_val($("#cn").html());
        $("#cn").html(cn);
    }

});