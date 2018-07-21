/* =========================================================
# 作者：韩望、秦海荣
# 时间：2018-04-11
# 功能：数据库js主代码部分
# 版本: v 0.0.0.1
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================*/

//主测试程序
function daas_test(type,instance_id)
{
    alert("test for dass" + type +instance_id);
}

//实例操作代码
function instance_operate(type,instance_id)
{
    var token = getCookie('csrftoken')
    //询问框
    var conf_msg = ""
    if (type == "start")
    {
        conf_msg = "确定是否继续进行启动操作? "
    }
    else if (type == "stop")
    {
        conf_msg = "确定是否继续进行停止操作? "
    }
    else if (type == "restart")
    {
        conf_msg = "确定是否继续进行重启操作? "
    }
    else
    {
        conf_msg = "确定是否继续进行此次操作? "
    }
    layer.confirm(conf_msg, 
    {
        btn: ['确定','取消'] //按钮
    }, 
    function()
    {
        $.post("/daas/instance/operate",
        {
            csrfmiddlewaretoken: token,
            type:type,
            instance_id:instance_id,
        },
        function(data,status)
        {
            layer.msg(type+";"+instance_id + data.code + status + data.msg, {icon: 1});
            location.reload();
        });
    }, 
    function()
    {
        layer.msg("操作已取消...",{icon: 1});
    });
}


//通用实例库操作代码
function universal_instance_operate(obj,type,instance_id)
{
    var token = getCookie('csrftoken')
    //询问框
    var conf_msg = ""
    if (obj=='publishing_platform_manager_instance' && type == "delete")
    {
        conf_msg = "确定是否继续删除此实例? "
    }
    else if (obj == 'publishing_platform_server_address' && type == 'delete') 
    {
        conf_msg = "确定是否继续删除此机房?"
    }
    else if (obj == 'publishing_platform_user' && type == 'delete') 
    {
        conf_msg = "确定是否继续删除此用户?"
    }
    else if (obj == 'publishing_platform_group' && type == 'delete') 
    {
        conf_msg = "确定是否继续删除此组?"
    }
    else
    {
        conf_msg = "确定是否继续进行此次操作? "
    }
    layer.confirm(conf_msg, 
    {
        btn: ['确定','取消'] //按钮
    }, 
    function()
    {
        $.post("/daas/community/instance/operate",
        {
            csrfmiddlewaretoken: token,
            obj:obj,
            type:type,
            instance_id:instance_id,
        },
        function(data,status)
        {
            layer.msg(type+";"+instance_id + data.code + status + data.msg, {icon: 1});
            location.reload();
        });
    }, 
    function()
    {
        layer.msg("操作已取消...",{icon: 1});
    });
}

//测试数据库的连通性
function test_db_connection()
{
    var token = getCookie('csrftoken');
    var host =  $("#instance_host_ip").val();
    var port = $("#instance_port").val()
    var user = $("#instance_user_name").val()
    var pwd = $("#instance_user_pwd").val()
    //layer.msg(host + ":" + port + ":" + user + ":" + pwd)
    $.post("/daas/publishing/platform/instance/connection",
        {
            csrfmiddlewaretoken: token,
            host : host,
            port : port,
            user : user,
            pwd : pwd,
        },
        function(data,status)
        {
            if (data.state) 
            {
                layer.msg("数据库实例连通失败, " + data.msg, {icon: 1});
            }
            else
            {
                layer.msg("数据库实例连通成功!", {icon: 1});
            }
        });
}

//获取数据库实例中的所有数据库名称
function get_db_names_from_instance()
{
    var token = getCookie('csrftoken');
    var instance_id = $("#instance_id").val();
    $("#id_bundle").empty();
    $.post("/daas/community/get/db/names/from/instance/",
        {
            csrfmiddlewaretoken: token,
            instance_id : instance_id,
        },
        function(data,status)
        {
            if (data.state)
            {
                layer.msg("数据库实例连通失败, " + data.msg, {icon: 1});
            }
            else
            {
                // layer.msg("数据库实例连通成功," + data.length, {icon: 1});
                for ( db_name in data.db_names) {
                    var db_name = db_name
                    var str_option = "<option value='" + db_name +"'>" + db_name +"</option>"
                    $("#id_bundle").append(str_option);
                }
            }
        });
}