<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Ports </title>
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
    
  </style>
</head>

    <body>

    <div class="greet">
        <p> {{ ip }} </p>
        <a class="button butt_theme" href="../theme">
            <img class="icon_theme theme_icon_back"> </img>
        </a>
    </div>

        <header class="header">
                <div class="butts butts_left">

                    <a class="button butt_href" href="../docs/">
                        <img class="icon docs_icon_back"> </img>
                        <span class="href"> Docs </span>
                    </a>

                    <a class="button butt_href" href="../data">
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

        <div class="cards">
        {% for i in range(1, ports + 1) %}
            <div class="card port_card">
                <a href={{ip}}/{{i}} class="button">
                    <div class="port_line">
                        <img class="port_icon">
                        <p class="switch_label"> {{ i }} </p>
                    </div>
            </div>
            {% endfor %}
        </div>

    </body>
</html>