<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Account </title>
    <link href= "{{ url_for('static',filename='styles/style.css') }}" rel="stylesheet" type="text/css">
    {% if theme.theme_mode==1 %}
        <link href= "{{ url_for('static',filename='styles/colors_fiol.css') }}" rel="stylesheet" type="text/css">
    {% elif theme.theme_mode==2 %}
        <link href= "{{ url_for('static',filename='styles/colors_blue.css') }}" rel="stylesheet" type="text/css">
    {% else %}
        <link href= "{{ url_for('static',filename='styles/colors_dark.css') }}" rel="stylesheet" type="text/css">
    {% endif %}
    <link href="https://fonts.googleapis.com/css2?family=Mukta:wght@300&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
  <style>
        a:link {}
        a:visited {}
        a:hover {}

        .change_icon {background:url('/static/change_icon.png') no-repeat center center; background-size: auto 80%;}
        .remove_icon {background:url('/static/remove_icon.png') no-repeat center center; background-size: auto 80%;}
        .recover_icon {background:url('/static/recovery_icon.png') no-repeat center center; background-size: auto 80%;}
  </style>
</head>

    <body>

    <div class="greet">
        <p> Hello, {{current_user.username}} </p>
        <a class="button butt_theme" href="../api/theme">
            <img class="icon_theme theme_icon_back"> </img>
        </a>
    </div>

        <header class="header">
                <div class="butts butts_left">
                    
                    <a class="button butt_href" href="../api/docs/">
                        <img class="icon docs_icon_back"> </img>
                        <span class="href"> Docs </span>
                    </a>

                    <a class="button butt_href" href="../api/data">
                        <img class="icon data_icon_back"> </img>
                        <span class="href"> Data </span>
                    </a>

                </div>

                <div class="butts butts_right">

                    {% if current_user.type=="admin" %}
                        <a class="button butt_logout" href="../../../auth/admin">
                            <span class="href_logout"> Admin </span>
                            <img class="logout_icon admin_icon_back"> </img>
                        </a>
                    {% else %}
                        <a class="button butt_logout" href="../../../auth/account">
                            <span class="href_logout"> Account </span>
                            <img class="logout_icon admin_icon_back"> </img>
                        </a>
                    {% endif %}

                    <a class="button butt_logout" href="../../../auth/logout">
                        <span class="href_logout"> Logout </span>
                        <img class="logout_icon logout_icon_back"> </img>
                    </a>

                </div>
           </header>
    </body>

    <div class="register_case">

                <form class="login_form login_form_register" method="POST" action="/auth/account">

                    <div class="register_message">
                        <img class="user_icon" src = "{{url_for('static', filename='profile.png')}}">
                    </div>

                    <div class="register_message">
                        <span> {% if account_message %} {{account_message}} {% else %} Change your data {% endif %}</span>
                    </div>

                    <div>
                        <input class=" form input" type="email" name="email" value={{current_user.email}} placeholder={{current_user.email}} autofocus="">
                    </div>


                    <div>
                        <input class=" form input" type="username" name="username" value={{current_user.username}} placeholder={{current_user.username}} autofocus="">
                    </div>

                    <div class="field">
                        <div class="control">
                            <input class="form input" type="password" value={{current_user.password}} name="password" placeholder="Password">
                        </div>
                    </div>

                    {% if current_user.type=="admin" %}
                    <div>
                        <select class="type_form input" type="type" name="type" value={{current_user.type}} placeholder="Account Type" autofocus="">
                            <option value="admin">Admin</option>
                            <option value="employee">Employee</option>
                        </select>
                    </div>
                    {% endif %}

                    <button class="register_butt button">Change</button>

                </form>
        </div>
</html>