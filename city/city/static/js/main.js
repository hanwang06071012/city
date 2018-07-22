function getCookie(sName){
  var aCookie=document.cookie.split("; ");
  for(var i=0;i<aCookie.length;i++){
    var aCrumb=aCookie[i].split("=");if(sName==aCrumb[0])
    return(aCrumb[1]);
  }
  return null;
}

function deleteCurrentRow(obj){
       var tr=obj.parentNode.parentNode.parentNode.parentNode.parentNode;
       var tbody=tr.parentNode;
       tbody.removeChild(tr);
   }

function array2arg(data){
    total = [];
    for(var item in data){
       total.push(item+"="+data[item]); 
    }
    if(total.length == 0){
        return "";
    }
    return "?"+total.join("&");
}

function base_ajax(url, timeout, data,okfunc){
        $.ajax({
            url: url+array2arg(data),
            type: 'GET',
            async: true,
            timeout: timeout,
            dataType: 'json',
            beforeSend: function(xhr) {
                layer.load(1, {
                    offset: 'auto',
                    shadeClose: 'true'
                });
            },
            success: function(data, textStatus, jqXHR) {
                layer.closeAll('loading');
                okfunc(data); 
            },
            error: function(xhr, textStatus) {
                console.log(xhr,textStatus);
                if (textStatus == 'timeout' || textStatus== 'error') {
                    console.log(textStatus);
                    layer.closeAll('loading');
                    return
                }
               if (xhr.status==404){
                   layer.msg("该记录不存在或被删除!");
               }else if(xhr.status == 401){
                   layer.msg("没有权限!");
               }else if(xhr.status == 403){
                   layer.msg("没有权限!");
               }else if(xhr.status == 500){
                   layer.msg("系统错误!");
               }else if(xhr.status == 503){
                   layer.msg("系统错误!");
                   console.log(data);
               }else if(xhr.status == 302){
                   location.href = xhr.getResponseHeader("Location");
               }else if (xhr.responseText.search("login") != -1 && textStatus == "parsererror"){
                   window.location.href="{% url 'accounts:logout' %}";
               } 
            },
            complete: function(XMLHttpRequest, status) {
                if (status == 'timeout') {
                    console.log("timeout");
                    layer.closeAll('loading');
                }
            }
        })
}

function base_ajax_post(url, timeout, data,okfunc){
        $.ajax({
            url: url,
            type: 'POST',
            async: true,
            timeout: timeout,
            data:data,
            dataType: 'json',
            beforeSend: function(xhr) {
                layer.load(1, {
                    offset: 'auto',
                    shadeClose: 'true'
                });
            },
            success: function(data, textStatus, jqXHR) {
                layer.closeAll('loading');
                okfunc(data); 
            },
            error: function(xhr, textStatus) {
                layer.closeAll('loading');
                if (textStatus == 'timeout') {
                    console.log("timeout");
                    return
                }
               if (xhr.status==404){
                   layer.msg("该记录不存在或被删除!");
               }else if(xhr.status == 401){
                   layer.msg("没有权限!");
               }else if(xhr.status == 403){
                   layer.msg("没有权限!");
               }else if(xhr.status == 500){
                   layer.msg("系统错误!");
               }else if(xhr.status == 503){
                   layer.msg("系统错误!");
                   console.log(data);
               }else if(xhr.status == 302){
                   location.href = xhr.getResponseHeader("Location");
               }else if (xhr.responseText.search("login") != -1 && textStatus == "parsererror"){
                   window.location.href="{% url 'accounts:logout' %}";
               } 
            },
            complete: function(XMLHttpRequest, status) {
                if (status == 'timeout') {
                    console.log("timeout");
                    layer.closeAll('loading');
                }
            }
        })
}

function get_namespace_options(url,timeout,domid){
  base_ajax(url, timeout,{},
        function(data){
            if (data["error"]==1){
            console.log(data.msg);
            }else{
            $("#"+domid).empty(); 
            $('#'+domid).select2({
                language: 'zh-CN',
                tags:true,
                data: data.namespaceoptions.results
            });
          }
        }
      )
}

function clear_tbody(tid){
       $("#"+tid+" tbody").html("");
}


function redraw_table(url, timeout, tid, table_func,list_name){
        $.ajax({
            url:url,
            type:'GET',
            async:true,    //或false,是否异步
            timeout:timeout,    //超时时间
            dataType:'json',    //返回的数据格式：json/xml/html/script/jsonp/text
            beforeSend: function (xhr) {
                        layer.load(1,{offset:'auto',shadeClose:'true'});    // 数据加载成功之前，使用loading组件
                    },
            success:function(data,textStatus,jqXHR){
                console.log(data);
                layer.closeAll('loading');
                if (data["error"]==1){
                  layer.msg(data.msg);
                }else{
                clear_tbody(tid);
                table_func(data[list_name]);
              }
            },
            error:function(xhr,textStatus){
                if (textStatus == 'timeout') {
                    console.log("timeout");
                    layer.closeAll('loading');
                    return
                }
               if (xhr.status==404){
                   layer.msg("该记录不存在或被删除!");
               }else if(xhr.status == 401){
                   layer.msg("没有权限!");
               }else if(xhr.status == 403){
                   layer.msg("没有权限!");
               }else if(xhr.status == 500){
                   layer.msg("系统错误!");
               }else if(xhr.status == 302){
                   location.href = xhr.getResponseHeader("Location");
               }else if (xhr.responseText.search("login") != -1 && textStatus == "parsererror"){
                  window.location.href="{% url 'accounts:logout' %}";
               }   
            },
            complete: function (XMLHttpRequest,status) {
                if(status == 'timeout') {
                  clear_tbody(tid);
                  table_func("",1);
                }
            }
        })
}

function label_display(label_data){
     var totalinfo="";
     if (label_data == null){
         return "_"; 
     }else{
     for ( var j in label_data){
         totalinfo=totalinfo+'<span class="label label-default">'+j+":"+label_data[j]+'</span><br />'
     }   
     return totalinfo;
     }
}   

function array2label(data,num){
    num = num || 5;
    console.log(data,num);
    var total="";
    if (data.length == 1 && data[0]==""){
      return "-";
    }else{
    var n = 1;
    for (var i in data){
      if (n % num == 0){
        total=total + '<span class="label label-default">' +data[i]+'</span><br />';
      }else{
        total=total + '<span class="label label-default">' +data[i]+'</span>&nbsp;';
      } 
      n=n+1;
    
    }
    return total;
    }
}

function draw_subject_table(table_data,tid,status){
    var status = arguments[1] ? arguments[1] : 0;
    var tid = tid;
    var ajax_status={1:"请求超时，请刷新重试....",0:"成功..."};
    function null2str(data){
        if (data == null){
            return "_";
        }else{
        return data;
        }
    }
    if (status != 1){
        if (table_data.length == 0){
            $(tid).append('<tr role="row" class="odd"><td colspan="'+$(tid).find('thead tr').children('th').length+'" class="text-center">无数据</td></tr>');
        }else{
        for(j = 0,len=table_data.length; j < len; j++) {
            var htmltext='<tr role="row" class="odd">'
                        +'<td class="text-center">'+null2str(table_data[j].api_group)+'</td>'
                        +'<td class="text-center">'+table_data[j].kind+'</td>'
                        +'<td class="text-center">'+table_data[j].name+'</td>'
                        +'<td class="text-center">'+table_data[j].namespace+'</td>'
                        +'</tr>'
                        $(tid).append(htmltext);
         
        }
}}else{
    $(tid).append('<tr role="row" class="odd"><td colspan="'+$(tid).find('thead tr').children('th').length+'" class="text-center">'+ajax_status[status]+'</td></tr>');
}
}

function draw_data_table(table_data,tid,status){
    var status = arguments[1] ? arguments[1] : 0;
    var tid=tid;
    if (status != 1){
        if (table_data == null){
            $(tid).append('<tr role="row" class="odd"><td colspan="2" class="text-center">无数据</td></tr>');
        }else{
        for(var item in table_data) {
            var htmltext='<tr role="row" class="odd">'
                        +'<td class="text-left" style="width:90px; vertical-align: top;">'+item+'</td>'
                        +'<td class="text-left"><pre>'+table_data[item]+'</pre></td>'
                        +'</tr>'
                        $(tid).append(htmltext);
         
        }
}}else{
    $(tid).append('<tr role="row" class="odd"><td colspan="2" class="text-center">'+ajax_status[status]+'</td></tr>');
}
}

function ajax_table(url, timeout, table_func) {

    $.ajax({
        url: url,
        type: 'GET',
        async: true,
        //或false,是否异步
        timeout: timeout,
        //超时时间
        dataType: 'json',
        //返回的数据格式：json/xml/html/script/jsonp/text
        beforeSend: function(xhr) {
            layer.load(1, {
                offset: 'auto',
                shadeClose: 'true'
            }); // 数据加载成功之前，使用loading组件
        },
        success: function(data, textStatus, jqXHR) {
            console.log(data);
            layer.closeAll('loading');
            if (data["error"] == 1) {
                layer.msg(data.msg);
            } else {
                table_func(data);
            }
        },
        error: function(xhr, textStatus) {
          console.log(xhr,textStatus);
                if (textStatus == 'timeout') {
                    console.log("timeout");
                    layer.closeAll('loading');
                    return
                }
           if (xhr.status==404){
               layer.msg("该记录不存在或被删除!");
           }else if(xhr.status == 401){
               layer.msg("没有权限!");
           }else if(xhr.status == 403){
               layer.msg("没有权限!");
           }else if(xhr.status == 500){
               layer.msg("系统错误!");
           }else if(xhr.status == 302){
               location.href = xhr.getResponseHeader("Location");
           }else if (xhr.responseText.search("login") != -1 && textStatus == "parsererror"){
               window.location.href="{% url 'accounts:logout' %}";
           } 
        },
        complete: function(XMLHttpRequest, status) {
            if (status == 'timeout') {
                layer.closeAll('loading');
                table_func("", 1);
            }
        }
    })

}


function ajax_confirm(url, timeout, data, confirminfo,okfunc) {
    layer.confirm(confirminfo,function(index){
        base_ajax(url, timeout, data,okfunc);
        layer.close(index);
      })
}

function getQueryString() {  
  var qs = location.search.substr(1), // 获取url中"?"符后的字串  
    args = {}, // 保存参数数据的对象
    items = qs.length ? qs.split("&") : [], // 取得每一个参数项,
    item = null,
    len = items.length;
 
  for(var i = 0; i < len; i++) {
    item = items[i].split("=");
    var name = decodeURIComponent(item[0]),
      value = decodeURIComponent(item[1]);
    if(name) {
      args[name] = value;
    }
  }
  return args;
}
function formatStrDate(strtime) { 
    var now = new Date(strtime);
    var year=now.getFullYear(); 
    var month=now.getMonth()+1 < 10 ? "0" + (now.getMonth()+1) : now.getMonth()+1; 
    var date=now.getDate() < 10 ? "0" + now.getDate() : now.getDate(); 
    var hour=now.getHours() < 10 ? "0" + now.getHours() : now.getHours() ; 
    var minute=now.getMinutes() < 10 ? "0" + now.getMinutes() : now.getMinutes()  ; 
    var second=now.getSeconds() < 10 ? "0" +  now.getSeconds() : now.getSeconds(); 
    return year+"-"+month+"-"+date+" "+hour+":"+minute+":"+second; 
}
function time_reversal(time)
{
    if (time==null)
    {
        return
    }else{
        return formatStrDate(time); 
    }
}
