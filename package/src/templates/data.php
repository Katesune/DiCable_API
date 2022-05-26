<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Data switches </title>
    <link href= "{{ url_for('static',filename='styles/style.css') }}" rel="stylesheet" type="text/css">
    {% if theme.theme_mode==1 %}
        <link href= "{{ url_for('static',filename='styles/colors_fiol.css') }}" rel="stylesheet" type="text/css">
    {% elif theme.theme_mode==2 %}
        <link href= "{{ url_for('static',filename='styles/colors_blue.css') }}" rel="stylesheet" type="text/css">
    {% else %}
        <link href= "{{ url_for('static',filename='styles/colors_dark.css') }}" rel="stylesheet" type="text/css">
    {% endif %}
    <!-- <link href= "{{ url_for('static',filename='fonts/Noah-Bold.ttf') }}" rel="stylesheet" rel="stylesheet"> -->
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
        <p> Data switches </p>
        <a class="button butt_theme" href="theme">
            <img class="icon_theme theme_icon_back"> </img>
        </a>
    </div>

        <header class="header">
                
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
                        <!-- <img class="logout_icon log_test" src = "{{url_for('static', filename='logout_white.png')}}"> </img> -->
                    </a>
                </div>

           </header>

        <div class="date_label">
            <p> {{ date }} </p>
        </div>

        
            <div class="cards">
            {% for res in result %}
                <div class="card switch_card">
                    <table>

                        <thead>
                            <tr>
                                <th colspan="2"> 
                                    <img class="ip_icon" src = "{{url_for('static', filename='ip_icon_black.png')}}">
                                </th>                  
                            </tr>

                            <tr height="30%">
                                <th colspan="2" class="ip_line">
                                    <a href=data/{{res.ip}} class="switch_label"> {{ res.ip }} </a> 
                                </th>
                            </tr>
                        </thead>

                        <tbody>
                            {% for resp in res.answers %}
                                {% if resp.errorIndication %}
                                    <tr class="row"> 
                                        <td class="data"> errorIndication </td>
                                        <td class="data"> {{ resp.errorIndication }} </td>
                                    </tr>

                                {% elif resp.errorStatus %}
                                    <tr class="row"> 
                                        <td class="data"> errorStatus </td>
                                        <td class="data"> {{ resp.errorStatus }} </td>
                                    </tr> 

                                    <tr class="row"> 
                                        <td class="data"> errorIndex </td>
                                        <td class="data"> {{ resp.errorIndex }} </td>
                                    </tr>
                                    
                                {% else %}
                                    {% for final_answer in resp.final_answers %}
                                        <tr class="row"> 
                                            <td class="data"> {{ final_answer }} </td>
                                            <td class="data"> {{ resp.final_answers[final_answer] }} </td>
                                        </tr>
                                    {% endfor %}
                                {% endif %}

                            {% endfor %}

                        </tbody>
                    </table>
                </div>
            {% endfor %}
        </div>
    </body>
</html>