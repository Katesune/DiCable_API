<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Log in </title>
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

  </style>
</head>

    <body>

        <div class="greet">
            <p> Authentication </p>
            <a class="button butt_theme" href="theme">
            <img class="icon_theme theme_icon_back"> </img>
        </a>
        </div>

        <!-- <header class="header">
                <div class="butts butts_left">
                    
                    <a class="button butt_href" href="docs/">
                        <img class="icon docs_icon_back"> </img>
                        <span class="href"> Docs </span>
                    </a>

                    <a class="button butt_href" href="data">
                        <img class="icon data_icon_back"> </img>
                        <span class="href"> Data </span>
                    </a>

                </div>

                <div class="butts butts_right">
                </div>

           </header> -->

           <div class="register_case">

                <form class="login_form login_form_register" method="POST" action="/auth/login">

                    <div class="auth_message">
                        <img class="user_icon" src = "{{url_for('static', filename='profile.png')}}">
                    </div>

                    {% if message %}
                        <div class="auth_message">
                            <span> {{ message }} </span>
                        </div>
                    {% endif %}

                    <div>
                        <input class=" form_item input is-large" type="email" name="email" placeholder="Your Email" autofocus="">
                    </div>
                
                    <div>
                        <input class="form_item input is-large" type="password" name="password" placeholder="Your Password">
                    </div>
                   
                    <div class="remember">
                        <input type="checkbox" class="choose"> 
                        <label class="checkbox remember_label">
                            <!-- <input type="checkbox" class="choose">  -->
                            Remember me
                        </label>
                    </div>

                    <button class="login_butt button">Login</button>

                </form>
        </div>

    </body>
</html>