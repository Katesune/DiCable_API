<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Admin </title>
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
        <p> Admin Page </p>
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

                    <a class="button butt_logout" href="../../../auth/admin">
                        <span class="href_logout"> Admin </span>
                        <img class="logout_icon admin_icon_back"> </img>
                    </a>

                    <a class="button butt_logout" href="../../../auth/logout">
                        <span class="href_logout"> Logout </span>
                        <img class="logout_icon logout_icon_back"> </img>
                    </a>

                </div>


           </header>
        <div class="register_case">

                <form class="login_form login_form_register" method="POST" action="/auth/admin">

                    <div class="register_message">
                        <img class="user_icon" src = "{{url_for('static', filename='profile.png')}}">
                    </div>

                    <div class="register_message">
                        <span> {% if message %} {{message}} {% else %} Create a new user {% endif %}</span>
                    </div>

                    <div>
                        <input class=" form input" type="email" name="email" placeholder="Email" autofocus="">
                    </div>


                    <div>
                        <input class=" form input" type="username" name="username" placeholder="Name" autofocus="">
                    </div>


                    <div class="field">
                        <div class="control">
                            <input class="form input" type="password" name="password" placeholder="Password">
                        </div>
                    </div>

                    <div>
                        <select class="type_form input" type="type" name="type" placeholder="Account Type" autofocus="">
                            <option value="admin">Admin</option>
                            <option value="employee">Employee</option>
                        </select>
                    </div>

                    <button class="register_butt button">Register</button>

                </form>

                <div class="admins_cards">
                    <h1> Admins </h1>
                    {% if admins %}
                    {% for admin in admins %}
                        <form class="admin_card" method="POST" action="/auth/admin">
                     
                            <input class = "user_item_data username user_item_data" type="username" name="username" value={{admin.username}} placeholder={{admin.username}} autofocus=""  />
                        
                            <input class = "user_item_data email" type="email" name="email" value={{admin.email}} placeholder={{admin.email}} autofocus=""/>
                            
                            {% if admin == current_user %}
                                <input class = "user_item_data email" type="password" value={{admin.password}} name="password" placeholder={{admin.password}} autofocus=""/>
                            {% endif %}

                            <select class="user_item_data type" type="type" name="type" value={{admin.type}} placeholder={{admin.type}} autofocus="">
                                    <option value="admin" selected>Admin</option>
                                    <option value="employee">Employee</option>
                            </select>

                            <div class = "user_item_data remove">
                                {% if admin.remove %}
                                    Deleted
                                {% else %}
                                    Active
                                {% endif %}
                            </div>

                            <div class="action_butt">
                                <input class = "user_item_data action_icon change_icon" type="submit" name="change" value={{admin.id}} />
                            </div>

                            <div class="action_butt">
                                <input class = "user_item_data action_icon remove_icon" type="submit" name="remove" value={{admin.id}} />
                            </div>

                            <div class="action_butt">
                                <input class = "user_item_data action_icon recover_icon" type="submit" name="recover" value={{admin.id}} />
                            </div>
                            
                        </form>
                    {% endfor %}
                {% endif %}

            </div>

            
        
        <div class="employees_cards">
            <h1> Employees </h1>
            {% if employees %}
                {% for employee in employees %}
                    <form class="employee_card" method="POST" action="/auth/admin">

                        <input class = "user_item_data username" type="username" name="username" value={{employee.username}} placeholder={{employee.username}} autofocus=""  />
                       
                        <input class = "user_item_data email" type="email" name="email" value={{employee.email}} placeholder={{employee.email}} autofocus=""  />

                        <select class="user_item_data type" type="type" name="type"  value={{employee.type}} placeholder={{employee.type}} autofocus="">
                                <option value="admin">Admin</option>
                                <option value="employee" selected>Employee</option>
                        </select>

                        <div class = "user_item_data remove">
                            {% if employee.remove %}
                                Deleted
                            {% else %}
                                Active
                            {% endif %}
                        </div>

                        <div class="action_butt">
                            <input class = "user_item_data action_icon change_icon" type="submit" name="change" value={{employee.id}} />
                        </div>

                        <div class="action_butt">
                            <input class = "user_item_data action_icon remove_icon" type="submit" name="remove" value={{employee.id}} />
                        </div>

                        <div class="action_butt">
                            <input class = "user_item_data action_icon recover_icon" type="submit" name="recover" value={{employee.id}} />
                        </div>
                            
                    </form>
                {% endfor %}
            {% endif %}
        </div>
        </div>

    </body>
</html>