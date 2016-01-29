/**
 * Created by yeoman on 29.01.2016.
 */

function ajaxcall(){
  $.ajax({
      type:'GET',
      url:'http://127.0.0.1:8000/check_message',
      success:function (response){
          if(response != 0){
               $('#notification').html(response);
              }
      }
  })
}
ajaxcall();
setInterval(ajaxcall, 10000);